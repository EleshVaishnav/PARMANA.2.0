from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()
GLOBAL_AGENT = None

@app.post("/webhook")
async def whatsapp_webhook(request: Request):
    data = await request.form()
    user_id = data.get("From")
    user_msg = data.get("Body")
    
    # Process message via Agent
    response = await GLOBAL_AGENT.process_message(user_id, user_msg)
    
    # In a real scenario, you'd use Twilio/Meta API to send the response back here
    print(f"WhatsApp Response to {user_id}: {response}")
    return {"status": "success"}

async def start_whatsapp_webhook(token, agent):
    global GLOBAL_AGENT
    GLOBAL_AGENT = agent
    config = uvicorn.Config(app, port=5000, host="0.0.0.0")
    server = uvicorn.Server(config)
    await server.serve()
