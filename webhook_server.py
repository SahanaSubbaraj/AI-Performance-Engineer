from fastapi import FastAPI, BackgroundTasks
import subprocess
import os
import sys

app = FastAPI()

def run_ai_pipeline(target):
    print(f"\n🚀 [EVENT] Webhook Triggered for: {target}", flush=True)
    
    # Use -u for unbuffered logs so they show in Render logs instantly
    try:
        subprocess.run(
            [sys.executable, "-u", "mvp_pipeline.py", target],
            check=True
        )
        print(f"✅ [DONE] Pipeline finished for {target}", flush=True)
    except Exception as e:
        print(f"❌ [ERROR] Pipeline failed: {str(e)}", flush=True)

@app.post("/trigger-test")
async def trigger_test(background_tasks: BackgroundTasks, data: dict):
    target = data.get("endpoint", "/posts/1") 
    print(f"\n[SERVER] Received request for: {target}", flush=True)
    background_tasks.add_task(run_ai_pipeline, target)
    return {"message": f"Cloud AI started testing {target}"}

@app.get("/")
def health_check():
    return {"status": "AI Pipeline Server is Online"}

if __name__ == "__main__":
    import uvicorn
    # Cloud platforms like Render provide a PORT env variable
    port = int(os.environ.get("PORT", 8000))
    # Binding to 0.0.0.0 is required for cloud access
    uvicorn.run(app, host="0.0.0.0", port=port)