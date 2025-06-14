def plan_goal(goal: str):
    goal = goal.lower()
    if "spacex" in goal and "weather" in goal:
        return ["launch_agent", "weather_agent", "summary_agent"]
    return []
