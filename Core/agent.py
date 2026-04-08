import json
import asyncio
from LLM_Gateway.provider_router import LLMGateway
from Memory.vector_memory import LongTermMemory
from Skills.registry import get_tools_definition, execute_skill

class ParmanaAgent:
    def __init__(self, config):
        self.config = config
        self.gateway = LLMGateway(config)
        self.memory = LongTermMemory(config)
        
        with open("system_prompt.txt", "r") as f:
            self.system_prompt = f.read()

    async def process_message(self, user_id, text, image_path=None):
        # 1. Get Memory Context
        context = self.memory.get_context(user_id, text)
        full_prompt = f"{self.system_prompt}\n{context}"
        
        # 2. Prepare Messages
        messages = [{"role": "system", "content": full_prompt}]
        
        if image_path:
            # Handle Vision
            from Vision.vision_handler import prepare_vision_payload
            messages.extend(prepare_vision_payload(image_path, text))
        else:
            messages.append({"role": "user", "content": text})

        # 3. Ask the Brain (with Skills)
        tools = get_tools_definition()
        response_message = self.gateway.generate_response(messages, tools=tools)

        # 4. Handle Tool Calls (If the AI wants to use a skill)
        if response_message.tool_calls:
            for tool_call in response_message.tool_calls:
                skill_name = tool_call.function.name
                arguments = json.loads(tool_call.function.arguments)
                result = execute_skill(skill_name, arguments)
                
                # Feed the result back to the AI
                messages.append(response_message)
                messages.append({"role": "tool", "tool_call_id": tool_call.id, "name": skill_name, "content": result})
                
            # Get the final answer after tool use
            response_message = self.gateway.generate_response(messages)

        # 5. Save what happened to Memory (Intellect)
        self.memory.store_fact(user_id, f"User asked: {text}. My answer: {response_message.content}")

        return response_message.content
