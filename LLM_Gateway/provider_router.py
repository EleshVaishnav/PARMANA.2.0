import litellm
import os

class LLMGateway:
    def __init__(self, config):
        self.provider = config.get("llm_provider")
        self.model = config.get("model_name")
        self.api_key = config.get("api_key")
        os.environ[f"{self.provider.upper()}_API_KEY"] = self.api_key
        
        self.full_model = f"{self.provider}/{self.model}" if self.provider != "openai" else self.model

    def generate_response(self, messages, tools=None):
        """Sends everything to the API (Supports Tools & Vision)."""
        try:
            response = litellm.completion(
                model=self.full_model,
                messages=messages,
                tools=tools,
                tool_choice="auto" if tools else None
            )
            return response.choices[0].message
        except Exception as e:
            print(f"Gateway Error: {e}")
            return None
