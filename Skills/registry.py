from Skills.calculator import calculate

def get_tools_definition():
    """Defines the skills in a format LLMs understand (JSON Schema)."""
    return [
        {
            "type": "function",
            "function": {
                "name": "calculate",
                "description": "Solve math problems or expressions",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expression": {"type": "string", "description": "The math expression, e.g. 5*5"}
                    },
                    "required": ["expression"]
                }
            }
        }
    ]

def execute_skill(name, arguments):
    """Runs the actual python code for a requested skill."""
    if name == "calculate":
        return calculate(arguments.get("expression"))
    return "Skill not found."
