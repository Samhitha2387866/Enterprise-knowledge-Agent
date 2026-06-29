from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from graph import agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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