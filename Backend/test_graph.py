from graph import agent
result=agent.invoke(
    {
        "question": "Explain leave policy"
    }
)

print(result["answer"])
print(result["validation"])