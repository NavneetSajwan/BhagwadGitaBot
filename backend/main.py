from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from predict import answer_me

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/endpoint")
async def endpoint(input: dict):
    # Handle input and generate response here
    print("input: ", input)
    output = get_prediciton(input["input"])
    response = {"message": f"{output}"}
    return response

def get_prediciton(input):
    return answer_me(input)
