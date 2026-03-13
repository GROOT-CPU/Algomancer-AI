from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CodeInput(BaseModel):
    code: str
    language: str

def optimize_java(code):
    lines = code.split("\n")
    optimized = []

    for line in lines:
        line = line.strip()

        # Example optimization
        if "System.out.print(" in line:
            line = line.replace("print(", "println(")

        optimized.append(line)

    return "\n".join(optimized)

@app.post("/optimize")
def optimize(data: CodeInput):

    if data.language == "Java":
        result = optimize_java(data.code)
    else:
        result = data.code

    return {"optimized_code": result}