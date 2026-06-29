from typing import TypedDict, Any
from langgraph.graph import StateGraph,END
from Agents.retriever import retrieve_documents
from Agents.analyst import generate_answer
from Agents.verifier import verify_answer

class AgentState(TypedDict, total=False):
    question: str
    docs: Any
    answer: str
    validation: Any

def retrive(state):
    docs = retrieve_documents(state["question"])
    state["docs"] = docs
    return state

def analyze(state):
    context = "\n".join([doc.page_content for doc in state["docs"]])
    answer = generate_answer(context, state["question"])
    state["answer"] = answer
    return state

def verify(state):
    result = verify_answer(state["answer"], state["docs"])
    state["validation"] = result
    return state

workflow = StateGraph(AgentState)

workflow.add_node("Retrieve", retrive)
workflow.add_node("Analyze", analyze)
workflow.add_node("Verify", verify)

workflow.set_entry_point("Retrieve")

workflow.add_edge("Retrieve", "Analyze")
workflow.add_edge("Analyze", "Verify")
workflow.add_edge("Verify", END)

agent=workflow.compile()
