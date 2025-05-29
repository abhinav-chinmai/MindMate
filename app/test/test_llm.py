import pytest
from app.jobs.process import run_llm

def test_run_llm():
    response = run_llm("Answer in one word. Which country is Bhopal located in?")
    assert response.lower() == 'india'