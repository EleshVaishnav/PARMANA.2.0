
#!/bin/bash

# ── Banner ──────────────────────────────
echo ""
echo "${BOLD}${BLUE}"
echo "  ██████╗  █████╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗ █████╗ "
echo "  ██╔══██╗██╔══██╗██╔══██╗████╗ ████║██╔══██╗████╗  ██║██╔══██╗"
echo "  ██████╔╝███████║██████╔╝██╔████╔██║███████║██╔██╗ ██║███████║"
echo "  ██╔═══╝ ██╔══██║██╔══██╗██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║"
echo "  ██║     ██║  ██║██║  ██║██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║"
echo "  ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝"
echo "${RESET}"
echo "  ${BOLD}Har Bar Naya${RESET} — Free, Local, Limitless AI"
echo "  Version: ${PARMANA_VERSION}"
echo ""

# 1. Ask for LLM Provider
echo "Which LLM provider do you want to use?"
echo "1) OpenAI (GPT-4o)"
echo "2) Anthropic (Claude 3.5)"
echo "3) Gemini (Google)"
echo "4) Groq (Llama 3)"
read -p "Select a number (1-4): " provider_choice

case $provider_choice in
  1) provider="openai"; default_model="gpt-4o" ;;
  2) provider="anthropic"; default_model="claude-3-5-sonnet-20240620" ;;
  3) provider="gemini"; default_model="gemini-1.5-pro" ;;
  4) provider="groq"; default_model="llama3-70b-8192" ;;
  *) provider="openai"; default_model="gpt-4o" ;;
esac

read -p "Enter your API Key for $provider: " api_key

# 2. Ask for Channels
echo ""
echo "Which channels do you want to enable?"
read -p "Enable Telegram? (y/n): " use_telegram
if [ "$use_telegram" == "y" ]; then
    read -p "Enter Telegram Bot Token: " telegram_token
    tg_enabled="true"
else
    telegram_token=""
    tg_enabled="false"
fi

# 3. Ask for Skills
echo ""
echo "What will you use Parmana for? (Choose active skills)"
echo "1) Coding & System (Code execution, file reading)"
echo "2) Research (Web search, calculator)"
echo "3) Both"
read -p "Select a number (1-3): " skill_choice

case $skill_choice in
  1) skills="[\"coding\", \"file_system\"]" ;;
  2) skills="[\"web_search\", \"calculator\"]" ;;
  3) skills="[\"coding\", \"file_system\", \"web_search\", \"calculator\"]" ;;
  *) skills="[]" ;;
esac

# 4. Generate config.json
echo ""
echo "Generating config.json..."

cat <<EOF > config.json
{
  "llm_provider": "$provider",
  "model_name": "$default_model",
  "api_key": "$api_key",
  "channels": {
    "telegram": {
      "enabled": $tg_enabled,
      "token": "$telegram_token"
    },
    "whatsapp": {
      "enabled": false,
      "token": ""
    }
  },
  "active_skills": $skills
}
EOF

echo "Setup Complete! To start Parmana, run: python main.py"
