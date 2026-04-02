from fastapi import FastAPI
from pydantic import BaseModel

from app.calculator import multiply, resta, sum

app = FastAPI(title="Calculator API")


class OperationInput(BaseModel):
    a: int
    b: int


class OperationOutput(BaseModel):
    result: int


@app.post("/sum", response_model=OperationOutput)
def sum_endpoint(payload: OperationInput) -> OperationOutput:
    return OperationOutput(result=sum(payload.a, payload.b))


@app.post("/resta", response_model=OperationOutput)
def resta_endpoint(payload: OperationInput) -> OperationOutput:
    return OperationOutput(result=resta(payload.a, payload.b))


@app.post("/multiply", response_model=OperationOutput)
def multiply_endpoint(payload: OperationInput) -> OperationOutput:
    return OperationOutput(result=multiply(payload.a, payload.b))