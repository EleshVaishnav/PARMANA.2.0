# PARMANA 2.0 🤖

Parmana is an open-source, API-agnostic, agentic AI. It supports multiple LLM providers (OpenAI, Anthropic, Gemini, Groq), uses tools/skills, has long-term memory, and connects directly to channels like Telegram and WhatsApp.

## 🚀 Quick Install (Windows)

Open PowerShell and paste this command to automatically download, configure, and install Parmana:

```powershell
powershell -c "irm https://raw.githubusercontent.com/EleshVaishnav/PARMANA.2.0/main/install.ps1 | iex"

```

## 🧩 Project Layout

```
Parmana 2.0/
├── main.py              ← Entry point
├── config.yaml          ← API settings
├── .env.example         ← API keys template
├── requirements.txt     ← Dependencies
├── system_prompt.txt    ← Personality
├── LLM_Gateway/
│   └── provider_router.py  ← OpenAI/Claude/Gemini/Groq
├── Core/
│   ├── agent.py            ← Brain loop
│   └── prompt_manager.py   ← Memory inject
├── Memory/
│   ├── session_memory.py   ← Short-term
│   └── vector_memory.py    ← Long-term
├── Skills/
│   ├── web_search.py       ← DuckDuckGo
│   ├── calculator.py       ← Math
│   └── registry.py         ← Tool manager
├── Vision/
│   └── vision_handler.py   ← Image processing
└── Channels/
    ├── telegram.py         ← Telegram bot
    └── whatsapp.py         ← WhatsApp (ready)
```
