#  Multi-Agent System for Launch & Weather Evaluation

This project demonstrates a modular multi-agent AI system using Python that can interpret user goals, route them through a planner, gather live data using public APIs (SpaceX Launch Library & OpenWeatherMap), and summarize whether the next rocket launch may be affected by weather.

# System Architecture

Agents:

Planner Agent: Converts natural-language goal into a sequence of agent calls.

Launch Agent: Retrieves the next rocket launch using the SpaceX API.

Weather Agent: Fetches weather data for the launch location using OpenWeatherMap API.

Summary Agent: Evaluates if weather conditions are suitable for launch.

Pipeline:

User Goal ➔ Planner ➔ Launch Info ➔ Weather Info ➔ Summary

# Features

✅ Agent Chaining via a planner

✅ Retry Logic for API robustness

✅ Fallback Handling for Launch Agent

✅ Context Passing between agents

✅ Evaluation Suite to test agent reasoning

✅ Environment variable loading via .env

# Evaluation Logic

Your system is tested on:

Agent Chaining & Data Enrichment

Planner’s Routing Logic

Iterative Refinement to Goal➤ Retry logic and fallback mechanisms ensure resilience to failures.

Evaluation is run automatically at the end via:

run_eval_tests()

# Project Structure

```multi_agent_system_updated/
├── agents/
│   ├── planner_agent.py
│   ├── launch_agent.py
│   ├── weather_agent.py
│   └── summary_agent.py
├── eval/
│   └── eval_runner.py
├── main.py
├── run_eval_tests.py
└── .env
```

# Setup & API Keys

Create a .env file in the root directory:

WEATHER_API_KEY=your_openweathermap_key

# Running the System

python main.py

This will:

Run the full agent pipeline on the default goal.

Execute evaluation tests.

## Sample Goal

"Check if the next SpaceX launch might be delayed due to weather."

## Sample Output
![image](https://github.com/user-attachments/assets/05bfbc1b-cba9-4bd0-847e-b6c344f52af7)


# Requirements

Install dependencies using:

pip install (Include requests, python-dotenv, etc.)
