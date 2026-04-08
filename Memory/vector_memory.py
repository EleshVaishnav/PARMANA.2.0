
from mem0 import Memory

class LongTermMemory:
    def __init__(self, config):
        # Initialize Mem0
        # It will automatically extract facts from conversations
        self.memory = Memory()

    def store_fact(self, user_id, text):
        """Extracts and saves facts about the user."""
        self.memory.add(text, user_id=user_id)

    def get_context(self, user_id, query):
        """Retrieves relevant facts about the user for a specific query."""
        results = self.memory.search(query, user_id=user_id)
        if not results:
            return ""
        
        context = "\nThings I remember about you:\n"
        for res in results:
            context += f"- {res['memory']}\n"
        return context
