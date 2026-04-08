import os
from mem0 import Memory

class LongTermMemory:
    def __init__(self, config):
        # Configuration for Mem0
        mem_config = {
            "vector_store": {
                "provider": "chroma",
                "config": {
                    "path": "parmana_memory_db",
                }
            },
            "embedder": {
                "provider": "huggingface",
                "config": {
                    "model": "sentence-transformers/all-MiniLM-L6-v2"
                }
            }
        }

        # If the user actually chose OpenAI, we use it. 
        # Otherwise, we use the local HuggingFace embedder defined above.
        if config.get("llm_provider") == "openai":
            os.environ["OPENAI_API_KEY"] = config.get("api_key")
            # Remove the custom embedder to let it use OpenAI default
            del mem_config["embedder"]

        self.memory = Memory.from_config(mem_config)

    def store_fact(self, user_id, text):
        """Extracts and saves facts about the user."""
        try:
            self.memory.add(text, user_id=user_id)
        except Exception as e:
            print(f"Memory Store Error: {e}")

    def get_context(self, user_id, query):
        """Retrieves relevant facts about the user."""
        try:
            results = self.memory.search(query, user_id=user_id)
            if not results:
                return ""
            
            context = "\n[THINGS I REMEMBER ABOUT YOU]:\n"
            for res in results:
                context += f"- {res['memory']}\n"
            return context
        except:
            return ""
