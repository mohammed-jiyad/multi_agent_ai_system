# main.py
import os
from dotenv import load_dotenv
from core.agent_pipeline import run_agent_pipeline
from run_eval_tests import run_eval_tests

load_dotenv()

if __name__ == "__main__":
    goal = "Check if the next SpaceX launch might be delayed due to weather."
    run_agent_pipeline(goal)
    run_eval_tests()
