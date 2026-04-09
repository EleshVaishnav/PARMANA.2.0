import os

from mem0 import Memory


class LongTermMemory:
    def __init__(self, config):
        memory_cfg = config.get("memory", {}) if isinstance(config, dict) else {}

        self.enabled = memory_cfg.get("enabled", True)
        self.top_k = int(memory_cfg.get("top_k", 5))

        vector_path = memory_cfg.get("path", "parmana_memory_db")
        embedder_model = memory_cfg.get(
            "embedding_model", "sentence-transformers/all-MiniLM-L6-v2"
        )

        # Default: local Chroma + local embedding model.
        mem_config = {
            "vector_store": {
                "provider": "chroma",
                "config": {
                    "path": vector_path,
                },
            },
            "embedder": {
                "provider": "huggingface",
                "config": {
                    "model": embedder_model,
                },
            },
        }

        # If OpenAI is used, let mem0 use OpenAI embeddings.
        if config.get("llm_provider") == "openai" and config.get("api_key"):
            os.environ["OPENAI_API_KEY"] = config.get("api_key")
            mem_config.pop("embedder", None)

        self.memory = Memory.from_config(mem_config) if self.enabled else None

    def store_fact(self, user_id, text):
        """Extracts and saves facts about the user."""
        if not self.enabled or not self.memory:
            return

        try:
            self.memory.add(text, user_id=user_id)
        except Exception as e:
            print(f"Memory Store Error: {e}")

    def get_context(self, user_id, query):
        """Retrieves relevant facts about the user."""
        if not self.enabled or not self.memory:
            return ""

        try:
            results = self.memory.search(query, user_id=user_id, limit=self.top_k)
            if not results:
                return ""

            context = "\n[THINGS I REMEMBER ABOUT YOU]:\n"
            for res in results:
                context += f"- {res['memory']}\n"
            return context
        except Exception:
            return ""
