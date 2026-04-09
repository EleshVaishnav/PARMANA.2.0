# PARMANA 2.0 🤖

Parmana is an open-source, API-agnostic, agentic AI. It supports multiple LLM providers (OpenAI, Anthropic, Gemini, Groq), uses tools/skills, has long-term memory, and connects directly to channels like Telegram and WhatsApp.

### macOS / Linux (bash)

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/EleshVaishnav/PARMANA.2.0/main/install.sh)"
```

### Linux (wget alternative)

```bash
bash -c "$(wget -qO- https://raw.githubusercontent.com/EleshVaishnav/PARMANA.2.0/main/install.sh)"
```

## ▶️ How to run it

### Option A: after one-line install

1. Go to the project folder:
   - Windows: `cd $HOME\PARMANA`
   - macOS/Linux: `cd ~/PARMANA.2.0` (or wherever you cloned it)
2. Start Parmana:

```bash
python main.py
```

### Option B: manual setup

1. Clone and enter the repo:

```bash
git clone https://github.com/EleshVaishnav/PARMANA.2.0.git
cd PARMANA.2.0
```

2. (Recommended) create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows PowerShell: .venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create your env file and set keys:

```bash
cp .env.example .env
```

5. Edit `config.yaml`:
   - choose `llm_provider` and `model_name`
   - set `api_key` (or keep `${OPENAI_API_KEY}` and put key in `.env`)
   - enable at least one channel (`telegram.enabled: true` or `whatsapp.enabled: true`)

6. Run:

```bash
python main.py
```

If no channels are enabled, Parmana exits with a message asking you to enable one in `config.yaml`.

## 🧠 Memory configuration

Parmana keeps long-term memory in the `memory` section of `config.yaml`:

- `enabled`: turn long-term memory on/off.
- `top_k`: number of memories injected into each prompt.
- `path`: local Chroma DB folder.
- `embedding_model`: HuggingFace model used when not using OpenAI embeddings.

=======

```

>>>>>>> main
## 🧩 Project Layout


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
