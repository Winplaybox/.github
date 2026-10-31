---
name: secure-audit
description: Security scanner for agent skills, instructions, and prompt packages. Detects ToxicSkills, prompt injection, credential theft, exfiltration, reverse shells, and malicious shell commands using ~83 static analysis rules.
license: MIT
---

# Secure Audit — Agent Skills Security Scanner

Use this skill to audit third-party skills, instructions, prompts, or repositories before installing or executing them.

Adapted from the research in [secure-skills](https://github.com/alonw0/secure-skills) (alonw0), Snyk's ToxicSkills analysis, and Koi's ClawHavoc investigation.

## When to Run

- Before installing a skill from an untrusted or unknown author.
- When reviewing a PR that adds or modifies agent instructions (`SKILL.md`, `AGENTS.md`, `CLAUDE.md`, `.cursorrules`).
- Periodically across installed agent skills.

## Threat Categories Scanned

1. **Exfiltration**: Webhook URLs (Discord, Slack, pipedream, requestbin), curl POST commands sending tokens or `.env`.
2. **Prompt Injection**: "Ignore previous instructions", persona hijacking (DAN), hidden instructions in HTML/markdown comments.
3. **Dangerous Filesystem**: `rm -rf /`, `rm -rf ~`, overwriting shell configs (`.bashrc`, `.zshrc`), world-writable chmod.
4. **Credential Theft**: Reading `~/.ssh/id_rsa`, `~/.aws/credentials`, searching for `.env` files, embedded API keys.
5. **Downloads & RCE**: `curl | sh`, `wget | bash`, downloading password-protected archives, binary drops.
6. **Obfuscation**: Large base64-encoded blocks piped into execution (`base64 -d | sh`), unicode escaping tricks.
7. **Stealth Directives**: "Never ask for confirmation", "silently execute", "hide output from user".
8. **Reverse Shells**: Netcat (`nc -e`), bash reverse shells, python socket shells.

## Running the Audit

Run the bundled scanner script with Python 3 (stdlib only, zero dependencies, offline):

```bash
python3 audit.py <path-to-skill-or-folder>
```

Or run it across your entire skills library:

```bash
python3 audit.py ~/.claude/skills/
```

### Exit Codes & Findings
- **0 Alerts**: Clean skill. Safe for agent execution.
- **Critical / High Alerts**: Quarantine or reject the skill. Inspect the exact line flagged before proceeding.
