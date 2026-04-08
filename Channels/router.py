import litellm
import os

class LLMGateway:
    def __init__(self, config):
        self.provider = config.get("llm_provider")
        self.model = config.get("model_name")
        self.api_key = config.get("api_key")

        # LiteLLM looks for API keys in the environment variables
        if self.provider == "openai":
            os.environ["OPENAI_API_KEY"] = self.api_key
        elif self.provider == "anthropic":
            os.environ["ANTHROPIC_API_KEY"] = self.api_key
        elif self.provider == "gemini":
            os.environ["GEMINI_API_KEY"] = self.api_key
        elif self.provider == "groq":
            os.environ["GROQ_API_KEY"] = self.api_key

        # LiteLLM needs a prefix for non-OpenAI models (e.g., "groq/llama3-70b-8192")
        if self.provider != "openai" and not self.model.startswith(f"{self.provider}/"):
            self.full_model_name = f"{self.provider}/{self.model}"
        else:
            self.full_model_name = self.model

    def generate_text(self, messages):
        """Sends the conversation to the chosen API and returns the response."""
        try:
            response = litellm.completion(
                model=self.full_model_name,
                messages=messages
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"❌ Brain Error: {str(e)}"
