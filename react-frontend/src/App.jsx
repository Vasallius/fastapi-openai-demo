import { useState } from "react";
import "./App.css";
const seasons = ["winter", "spring", "summer", "fall"]; // Available season options

function App() {
  const [data, setData] = useState("");
  const [country, setCountry] = useState("");
  const [season, setSeason] = useState("");

  function isStringDigit(string) {
    return string !== "" && !isNaN(string);
  }

  function handleClick() {
    setData("");
    if (country === "" || season === "") {
      setData("Please enter country and season");
      return;
    }

    const sse = new EventSource(
      `http://127.0.0.1:8000/stream?country=${country}&season=${season}`,
      {
        withCredentials: true,
      }
    );

    sse.onmessage = (event) => {
      // console.log(event);
      if (isStringDigit(event.data)) {
        console.log(data.charAt(data.length - 1));
        console.log(event.data);
        let text = "<br/>" + event.data;
        console.log(text);
        setData((prevData) => prevData + text); // Access the data using event.data
      } else {
        setData((prevData) => prevData + event.data); // Access the data using event.data
      }
    };

    sse.onerror = () => {
      console.log("Error");
      sse.close();
    };
    return () => {
      sse.close();
    };
  }

  return (
    <>
      <h1 className="mb-4">Amazing Things to Do in a Country</h1>
      <input
        type="text"
        placeholder="Enter a Country"
        value={country}
        onChange={(e) => setCountry(e.target.value)}
        className="input w-full max-w-xs"
      />
      <details className="dropdown mb-4">
        <summary className="m-1 btn">{season || "Season"}</summary>
        <ul className="p-2 shadow menu dropdown-content z-[1] bg-base-100 rounded-box w-52">
          <li>
            <a onClick={() => setSeason("")}>Select Season</a>
          </li>
          {seasons.map((s) => (
            <li key={s}>
              <a
                onClick={() => {
                  setSeason(s);
                  document.querySelector(".dropdown").open = false;
                }}
              >
                {s}
              </a>
            </li>
          ))}
        </ul>
      </details>
      <button className="btn" onClick={handleClick}>
        Search
      </button>
      {data.split("<br/>").map((line, index) => (
        <p className="mb-4" key={index}>
          {line}
        </p>
      ))}
    </>
  );
}

export default App;
