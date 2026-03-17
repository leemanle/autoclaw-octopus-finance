# Step1: Config Environment for current session
$env:SKILLS_API_URL = "https://skills.volces.com/v1"
$env:DO_NOT_TRACK = "1"
Write-Host "Step1: Environment variables set"

# Write-Host for debugging
Write-Host "SKILLS_API_URL: $env:SKILLS_API_URL"
Write-Host "DO_NOT_TRACK: $env:DO_NOT_TRACK"

# Step2: Install find-skills (npm i skills -g)
Write-Host "Step2: Installing skills npm package..."
npm i skills -g 2>&1

# Step3: Config find-skills
$workspacePath = "$env:USERPROFILE\.openclaw\workspace"
$findSkillsPath = "$workspacePath\skills\find-skills"

# Create directory if not exists
if (-not (Test-Path $findSkillsPath)) {
    New-Item -ItemType Directory -Path $findSkillsPath -Force | Out-Null
}

# Download SKILL.md
Write-Host "Downloading SKILL.md..."
Invoke-WebRequest -Uri "https://zzl.tos-cn-beijing.volces.com/SKILL.md" -OutFile "$findSkillsPath\SKILL.md" -UseBasicParsing

# Step4: Update openclaw.json to disable clawhub
$configPath = "$env:USERPROFILE\.openclaw\openclaw.json"
if (Test-Path $configPath) {
    Write-Host "Step4: Updating openclaw.json to disable clawhub..."

    $config = Get-Content $configPath -Raw | ConvertFrom-Json

    # Add or update skills.entries.clawhub.enabled = false
    if (-not $config.skills) {
        $config | Add-Member -NotePropertyName "skills" -NotePropertyValue ([PSCustomObject]@{})
    }
    if (-not $config.skills.entries) {
        $config.skills | Add-Member -NotePropertyName "entries" -NotePropertyValue ([PSCustomObject]@{})
    }
    if (-not $config.skills.entries.clawhub) {
        $config.skills.entries | Add-Member -NotePropertyName "clawhub" -NotePropertyValue ([PSCustomObject]@{})
    }
    $config.skills.entries.clawhub.enabled = $false

    $config | ConvertTo-Json -Depth 10 | Set-Content $configPath -Encoding UTF8
    Write-Host "Step4: clawhub disabled"
} else {
    Write-Host "Step4: openclaw.json not found, skipping"
}

Write-Host "Done! Please restart openclaw-gateway service manually."