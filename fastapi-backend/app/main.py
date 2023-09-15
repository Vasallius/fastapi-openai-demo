import credentials
import openai
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

# make sure you have credentials.py with api_key
openai.api_key = credentials.api_key

app = FastAPI()

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
    return StreamingResponse(get_openai_generator(f"Give me three recommendations of things to do in {country} during {season}"), media_type='text/event-stream')
