Autonomous AI Performance Engineering Pipeline 🤖🚀
An end-to-end, autonomous system that utilizes Agentic AI to automate the entire software performance testing lifecycle—from script generation to root-cause analysis.
🌟 Overview
Traditional performance testing is a manual, time-consuming process. This project introduces a "Self-Testing" CI/CD pipeline where AI agents handle the technical heavy lifting. When a developer triggers the system via a webhook, the AI independently writes testing code, executes stress tests, analyzes the results, and reports bugs.
🛠️ The 6-Step Autonomous Workflow
The Trigger: A FastAPI webhook receives a signal (simulating a GitHub push or CI/CD event).
Agent 1 (The Coder): A LLM (Google Gemini) analyzes the target endpoint and dynamically writes a custom Locust performance script in Python.
Execution: The system initiates a Headless Locust stress test, simulating virtual users and generating raw performance data (CSV).
Agent 2 (The Analyst): The AI analyst reads the CSV results, identifies latency spikes or failures, and performs a Root Cause Analysis (RCA).
Agent 3 (The Reporter): The AI synthesizes the findings into a technical summary, categorizing the system health.
Integration: The system utilizes the GitHub API to automatically prepare/open a bug ticket if a performance regression is detected.
🚀 Tech Stack
AI Orchestration: Python & Google GenAI (Gemini 1.5 Flash / 2.0)
Performance Engine: Locust (Load & Stress Testing)
API Framework: FastAPI & Uvicorn (Webhook Server)
Data Science: Pandas (CSV Analysis)
Cloud Ready: Environment variable management via python-dotenv
📦 Installation & Setup
Clone the repository:
code
Bash
git clone https://github.com/SahanaSubbaraj/AI-Performance-Engineer.git
cd AI-Performance-Engineer
Set up Virtual Environment:
code
Bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Configure Environment Variables:
Create a .env file in the root directory:
code
Text
GEMINI_API_KEY=your_google_ai_studio_key
GITHUB_TOKEN=your_personal_access_token
🎮 How to Run (Demo)
1. Start the Webhook Server
code
Powershell
python -m uvicorn webhook_server:app --port 8001
2. Trigger the Autonomous Pipeline
In a second terminal, simulate a developer "Push" event:
code
Powershell
Invoke-RestMethod -Uri http://localhost:8001/trigger-test -Method Post -Body '{"endpoint": "/users"}' -ContentType "application/json"
📈 Key Achievements
Autonomous Coding: Successfully moved from static testing to dynamic AI-generated test suites.
Diagnostic Intelligence: Implemented an AI analyst capable of interpreting raw performance metrics into actionable engineering insights.
Professional Integration: Built a cloud-ready architecture capable of being deployed to platforms like Render or AWS.
