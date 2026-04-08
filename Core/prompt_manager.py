class PromptManager:
    def __init__(self, system_prompt_path="system_prompt.txt"):
        with open(system_prompt_path, "r", encoding="utf-8") as f:
            self.base_prompt = f.read()

    def build_full_prompt(self, user_facts):
        """Combines the system rules with facts from Long-Term Memory."""
        full_prompt = self.base_prompt
        if user_facts:
            full_prompt += f"\n\n[USER INTELLECT/MEMORIES]:\n{user_facts}"
        return full_prompt
