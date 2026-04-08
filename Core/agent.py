from LLM_Gateway.provider_router import LLMGateway

class ParmanaAgent:
    def __init__(self, config):
        self.config = config
        self.gateway = LLMGateway(config) # Connect to the Brain
        self.skills = config.get("active_skills", [])

        # Load the personality/rules
        try:
            with open("system_prompt.txt", "r", encoding="utf-8") as f:
                self.system_prompt = f.read()
                if not self.system_prompt.strip():
                    self.system_prompt = "You are Parmana, a highly intelligent and helpful AI assistant."
        except FileNotFoundError:
            self.system_prompt = "You are Parmana, a highly intelligent and helpful AI assistant."

    async def process_message(self, user_id, text, image=None):
        """Processes the user's text and asks the LLM for a reply."""
        
        # Format the memory/conversation for the AI
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": text}
        ]

        # Send to the API and wait for the answer
        # Note: We run it in a thread so it doesn't freeze the Telegram bot
        import asyncio
        loop = asyncio.get_event_loop()
        reply = await loop.run_in_executor(None, self.gateway.generate_text, messages)
        
        return reply
