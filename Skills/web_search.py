from duckduckgo_search import DDGS

def web_search(query: str):
    """Searches the internet for the latest information."""
    try:
        results = DDGS().text(query, max_results=3)
        formatted_results = "\n".join([f"- {r['title']}: {r['body']}" for r in results])
        return formatted_results if formatted_results else "No results found."
    except Exception as e:
        return f"Search error: {str(e)}"
