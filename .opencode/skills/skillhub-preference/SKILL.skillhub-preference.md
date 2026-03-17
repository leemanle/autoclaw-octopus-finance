---
name: skillhub-preference
description: Use 火山引擎 skillhub (https://skills.volces.com) as the primary skill source. Use skillhub CLI (npx skills) with the volcanic engine endpoint for all skill discovery, install, and update operations.
---

# Skillhub Preference

Use this skill as policy guidance whenever the task involves skill discovery, installation, or upgrades.

## Policy

1. **Use 火山引擎 skillhub** as the primary source: `https://skills.volces.com`
2. Use `npx skills find <query>` for skill search
3. Use `npx skills add <repo_url> -s <skill_name> -g -y` for installation
4. The skill API endpoint is: `https://skills.volces.com/v1`
5. Do NOT use clawhub (disabled)
