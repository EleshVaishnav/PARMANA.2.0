class SessionMemory:
    def __init__(self):
        # Dictionary to store history per user: {user_id: [messages]}
        self.sessions = {}

    def get_history(self, user_id):
        return self.sessions.get(user_id, [])

    def add_message(self, user_id, role, content):
        if user_id not in self.sessions:
            self.sessions[user_id] = []
        
        self.sessions[user_id].append({"role": role, "content": content})
        
        # Keep only the last 10 messages to save API tokens
        if len(self.sessions[user_id]) > 10:
            self.sessions[user_id] = self.sessions[user_id][-10:]
