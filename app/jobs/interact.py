import chainlit as cl
from app.jobs.process import run_llm
from app.core.constants import PROMPT, Questions

responses = []

@cl.on_chat_start
async def start():
    responses.clear()
    await cl.Message(content="Hello, I am MindMate, your personal mental health screening chatbot. Kindly answer the following questions for your mental health screening.").send()

    for question in Questions:
        res = await cl.AskUserMessage(content=question, timeout=500).send()
        answer = res.get("output") if res else None
        responses.append(answer if answer is not None else "No response")
    summary = "\n".join(f"{q} {a}" for q, a in zip(Questions, responses))
    # Run the LLaMa model using the summary
    await cl.Message(content="Analyzing your responses...").send()
    analysis = run_llm(summary = summary)
    # Show the LLaMa response
    await cl.Message(content=f"{analysis}").send()
    await cl.Message(content="Refresh page for a new session").send()
