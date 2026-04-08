def calculate(expression: str):
    """Solves mathematical expressions."""
    try:
        # Using a restricted eval for safety
        result = eval(expression, {"__builtins__": None}, {})
        return f"The result is {result}"
    except Exception as e:
        return f"Error calculating: {str(e)}"
