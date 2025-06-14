# core/agent_pipeline.py
from agents.planner_agent import plan_goal
from agents.launch_agent import get_next_launch
from agents.weather_agent import get_weather_at_location
from agents.summary_agent import summarize_launch_status

def run_agent_pipeline(user_goal):
    print(f"[Goal Received] {user_goal}")
    agent_plan = plan_goal(user_goal)
    print(f"[Planner Output] Agent sequence: {agent_plan}")

    context = {}
    for agent in agent_plan:
        print(f"[Running Agent] {agent}")
        if agent == "launch_agent":
            try:
                context["launch_info"] = get_next_launch(retries=3)
                print(f"[Launch Info] {context['launch_info']}")
            except Exception as e:
                print(f"[Error in Launch Agent] {e}. Trying fallback.")
                context["launch_info"] = {
                    "location": {"name": "Fallback Launch Site", "latitude": 28.5, "longitude": -80.5},
                    "date": "Fallback Date"
                }
        elif agent == "weather_agent":
            try:
                location = context["launch_info"]["location"]
                context["weather"] = get_weather_at_location(location, retries=3)
                print(f"[Weather Info] {context['weather']}")
            except Exception as e:
                print(f"[Error in Weather Agent] {e}. Unable to fetch weather after retries.")
                context["summary"] = "Unable to fetch weather data."
                break
        elif agent == "summary_agent":
            try:
                context["summary"] = summarize_launch_status(context.get("weather"))
                print(f"[Summary] {context['summary']}")
            except Exception as e:
                print(f"[Error in Summary Agent] {e}")
                return

    print("\n[Final Summary]\n", context.get("summary", "No summary generated."))
