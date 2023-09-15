import credentials
import openai
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

app = FastAPI()

openai.api_key = credentials.api_key

app = FastAPI()
# Replace with the actual origin of your React app
origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def starts_with_number(string):
    if len(string) > 0:

        return string[0].isdigit()


def get_openai_generator(prompt: str):
    openai_stream = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
        stream=True,
    )
    for event in openai_stream:
        if "content" in event["choices"][0].delta:
            current_response = event["choices"][0].delta.content
            yield "data: " + current_response + "\n\n"


@app.get('/stream')
async def stream(country: str, season: str):
    return StreamingResponse(get_openai_generator(f"Give me three recommendations of things to di in {country} during {season}"), media_type='text/event-stream')
