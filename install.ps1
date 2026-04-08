Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "    Welcome to PARMANA 2.0 Setup (Windows)" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

$installDir = "$HOME\PARMANA"

# 1. Download the code via Git
if (Test-Path $installDir) {
    Write-Host "PARMANA directory already exists at $installDir. Pulling latest updates..." -ForegroundColor Yellow
    Set-Location $installDir
    git pull
} else {
    Write-Host "Downloading PARMANA to $installDir..." -ForegroundColor Green
    git clone https://github.com/EleshVaishnav/PARMANA.2.0.git $installDir
    Set-Location $installDir
}

# 2. Install requirements
Write-Host "`nInstalling Python dependencies..." -ForegroundColor Green
pip install -r requirements.txt

# 3. Ask Setup Questions
Write-Host "`nWhich LLM provider do you want to use?" -ForegroundColor Cyan
Write-Host "1) OpenAI (GPT-4o)"
Write-Host "2) Anthropic (Claude 3.5)"
Write-Host "3) Gemini (Google)"
Write-Host "4) Groq (Llama 3)"
$provider_choice = Read-Host "Select a number (1-4)"

switch ($provider_choice) {
    '1' { $provider = "openai"; $model = "gpt-4o" }
    '2' { $provider = "anthropic"; $model = "claude-3-5-sonnet-20240620" }
    '3' { $provider = "gemini"; $model = "gemini-1.5-pro" }
    '4' { $provider = "groq"; $model = "llama3-70b-8192" }
    Default { $provider = "openai"; $model = "gpt-4o" }
}

$api_key = Read-Host "Enter your API Key for $provider"

Write-Host "`nEnable Telegram Bot? (y/n)" -ForegroundColor Cyan
$use_tg = Read-Host
if ($use_tg -eq 'y') {
    $tg_token = Read-Host "Enter Telegram Bot Token"
    $tg_enabled = "true"
} else {
    $tg_token = ""
    $tg_enabled = "false"
}

Write-Host "`nWhat will you use PARMANA for? (Choose active skills)" -ForegroundColor Cyan
Write-Host "1) Coding & System"
Write-Host "2) Research"
Write-Host "3) Both"
$skill_choice = Read-Host "Select a number (1-3)"

switch ($skill_choice) {
    '1' { $skills = '"coding", "file_system"' }
    '2' { $skills = '"web_search", "calculator"' }
    '3' { $skills = '"coding", "file_system", "web_search", "calculator"' }
    Default { $skills = '' }
}

# 4. Generate config.json
Write-Host "`nGenerating config.json..." -ForegroundColor Green

$configJson = @"
{
  "llm_provider": "$provider",
  "model_name": "$model",
  "api_key": "$api_key",
  "channels": {
    "telegram": {
      "enabled": $tg_enabled,
      "token": "$tg_token"
    },
    "whatsapp": {
      "enabled": false,
      "token": ""
    }
  },
  "active_skills": [$skills]
}
"@

Set-Content -Path "config.json" -Value $configJson

Write-Host "`n✅ Setup Complete!" -ForegroundColor Green
Write-Host "PARMANA 2.0 has been installed to: $installDir"
Write-Host "To start the agent, run:" -ForegroundColor Yellow
Write-Host "cd $HOME\PARMANA"
Write-Host "python main.py"
