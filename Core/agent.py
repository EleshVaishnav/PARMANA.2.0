class ParmanaAgent:
    def __init__(self, config):
        self.config = config
        self.provider = config.get("llm_provider")
        self.model = config.get("model_name")
        self.skills = config.get("active_skills", [])

    async def process_message(self, user_id, text, image=None):
        """This is where the magic will happen later."""
        return f"Parmana received your message: '{text}'. (Brain is under construction!)"
