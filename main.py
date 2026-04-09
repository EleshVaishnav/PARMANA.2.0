import asyncio
import sys
from pathlib import Path

import yaml
from dotenv import load_dotenv

from Channels.telegram import start_telegram_bot
from Channels.whatsapp import start_whatsapp_webhook
from Core.agent import ParmanaAgent

CONFIG_PATH = Path("config.yaml")


def load_config(path: Path = CONFIG_PATH) -> dict:
    """Load runtime configuration from YAML."""
    if not path.exists():
        print(f"Error: {path} not found. Please create it before starting Parmana.")
        sys.exit(1)

    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    return data


async def main() -> None:
    load_dotenv()
    print("Initializing Parmana 2.0...")
    config = load_config()

    agent = ParmanaAgent(config)
    print(f"Loaded LLM Provider: {config.get('llm_provider')} ({config.get('model_name')})")

    tasks = []
    channels = config.get("channels", {})

    telegram_config = channels.get("telegram", {})
    if telegram_config.get("enabled"):
        print("Starting Telegram Channel...")
        tasks.append(start_telegram_bot(telegram_config.get("token", ""), agent))

    whatsapp_config = channels.get("whatsapp", {})
    if whatsapp_config.get("enabled"):
        print("Starting WhatsApp Channel... (FastAPI)")
        tasks.append(start_whatsapp_webhook(whatsapp_config.get("token", ""), agent))

    if not tasks:
        print("No channels enabled! Please enable at least one channel in config.yaml.")
        sys.exit(0)

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    if sys.platform.startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nParmana AI shutting down...")
