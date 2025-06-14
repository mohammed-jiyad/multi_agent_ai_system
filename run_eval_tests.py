
from core.agent_pipeline import run_agent_pipeline

def run_eval_tests():
    print("\n[Running Eval Test 1]")
    run_agent_pipeline("Check if the next SpaceX launch might be delayed due to weather.")

    print("\n[Running Eval Test 2]")
    run_agent_pipeline("Will the weather affect a rocket launch today?")
