from fastapi import FastAPI
from pydantic import BaseModel
from graph import agent

app = FastAPI()

class Query(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "Welcome to the Enterprise Knowledge Agent!"}

@app.post("/ask")
def ask(query: Query):
    result = agent.invoke({"question": query.question})
    return {"answer": result["answer"], 
            "validation": result["validation"],
            "agent_flow":[
                "Retrieve",
                "Analyze",
                "Verify"
            ]}