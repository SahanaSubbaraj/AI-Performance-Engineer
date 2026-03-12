import os
import subprocess
import pandas as pd
import sys
from google import genai
from dotenv import load_dotenv

# 1. Setup
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("❌ ERROR: GEMINI_API_KEY missing in Environment Variables")
    sys.exit(1)

client = genai.Client(api_key=api_key)
MODEL_NAME = "gemini-flash-latest"

# --- Agent 1: The Coder ---
def agent_1_generate_script(target_url):
    print(f"--- Agent 1: Generating Script for {target_url} ---", flush=True)
    prompt = f"Write a Locust script for {target_url}. Include: from locust import HttpUser, task, between. Output ONLY raw python code."
    
    response = client.models.generate_content(model=MODEL_NAME, contents=prompt)
    code = response.text.strip().replace("```python", "").replace("```", "")
    
    # Force imports if missing
    if "from locust import" not in code:
        code = "from locust import HttpUser, task, between\n" + code
        
    with open("locustfile.py", "w") as f: 
        f.write(code.strip())
    print("✅ locustfile.py created.", flush=True)

# --- Step 3: Execution ---
def run_locust_test():
    print("--- Step 3: Executing Locust ---", flush=True)
    # Using python -m locust is the most stable way for cloud servers (Linux)
    cmd = f'"{sys.executable}" -m locust -f locustfile.py --headless -u 5 -r 1 -t 10s --csv=results --host=https://jsonplaceholder.typicode.com'
    
    try:
        subprocess.run(cmd, shell=True, check=True)
        print("✅ Performance test complete.", flush=True)
    except Exception as e:
        print(f"❌ Locust failed: {e}", flush=True)

# --- Agent 2: The Analyst ---
def agent_2_analyze_results():
    print("--- Agent 2: Analyzing CSV Data ---", flush=True)
    if not os.path.exists("results_stats.csv"):
        return "Error: No performance data found."

    df = pd.read_csv("results_stats.csv")
    summary_data = df.tail(1).to_string()

    prompt = f"Analyze these performance results and identify any bottlenecks: {summary_data}"
    response = client.models.generate_content(model=MODEL_NAME, contents=prompt)
    
    analysis = response.text
    print(f"✅ Analysis Complete:\n{analysis}", flush=True)
    return analysis

# --- MAIN FLOW ---
if __name__ == "__main__":
    target_endpoint = sys.argv[1] if len(sys.argv) > 1 else "/posts/1"
    agent_1_generate_script(target_endpoint) 
    run_locust_test()
    report = agent_2_analyze_results()
    print("\n--- FINAL CLOUD REPORT ---")
    print(report)