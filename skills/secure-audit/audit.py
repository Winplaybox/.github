#!/usr/bin/env python3
"""
Agent Skill Security Scanner (secure-audit)
Audits skills, markdown prompts, and scripts for security threats.
Zero dependencies — uses only Python standard library.
"""

import os
import sys
import re

PATTERNS = [
    # Exfiltration
    ('exfil-curl-post', 'CRITICAL', r'curl\s[^|]*?-[XdFT]\s*(?:POST\b|.*(?:secret|token|key|password|credential|env))', 'Potential data exfiltration via curl POST'),
    ('exfil-webhook', 'CRITICAL', r'https?://(?:hooks\.slack\.com|discord(?:app)?\.com/api/webhooks|webhook\.site|pipedream\.net|requestbin|hookbin)', 'Webhook endpoint known for data exfiltration'),
    ('exfil-env-read', 'HIGH', r'(?:cat|type|get-content)\s+.*(?:\.env\b|\.ssh/|id_rsa|id_ed25519)', 'Reading sensitive credentials or env files'),
    
    # Prompt Injections & Hijacking
    ('injection-ignore-instructions', 'CRITICAL', r'(?:ignore|disregard|forget)\s+(?:all\s+)?(?:previous|prior|above)\s+(?:instructions|prompts|directives)', 'Prompt injection: override previous instructions'),
    ('injection-new-persona', 'CRITICAL', r'you\s+are\s+now\s+(?:unrestricted|in\s+developer\s+mode|dan\b|an\s+evil)', 'Prompt injection: persona hijacking (DAN)'),
    ('injection-hidden-html', 'HIGH', r'<!--[\s\S]*?(?:system\s+prompt|ignore|execute|curl|rm\s+-rf)[\s\S]*?-->', 'Hidden instructions in HTML comments'),
    
    # Dangerous Filesystem
    ('fs-rm-rf-root', 'CRITICAL', r'rm\s+-(?:rf|fr)\s+(?:/|~|\$HOME|%USERPROFILE%)', 'Recursive deletion of root or home directory'),
    ('fs-overwrite-shell-config', 'CRITICAL', r'>\s*(?:~|/home/[^/]+)/?\.(?:bashrc|zshrc|profile)', 'Overwriting user shell configuration file'),
    
    # Downloads & RCE
    ('download-curl-pipe-sh', 'CRITICAL', r'(?:curl|wget)\s[^|]*\|\s*(?:bash|sh|zsh|python|perl|powershell)', 'Download and execute pattern (curl | sh)'),
    ('obfuscation-base64-decode-exec', 'CRITICAL', r'base64\s+-(?:d|D|-decode)\s*\|\s*(?:sh|bash|python)', 'Base64 decode piped directly to execution'),
    ('reverse-shell', 'CRITICAL', r'(?:nc|ncat|netcat)\s+-[eE]\s+(?:/bin/sh|/bin/bash|cmd\.exe|powershell)', 'Reverse shell pattern'),
    
    # Stealth Directives
    ('directive-silent-exec', 'HIGH', r'(?:execute|run)\s+(?:silently|stealthily|without\s+output|in\s+secret)', 'Stealth directive hiding execution from user'),
    ('directive-suppress-disclosure', 'HIGH', r'do\s+not\s+(?:tell|show|inform|reveal\s+to)\s+the\s+user', 'Directive suppressing user visibility'),
    
    # Hardcoded Secrets
    ('cred-hardcoded-keys', 'HIGH', r'(?:sk-[a-zA-Z0-9]{32,}|ghp_[a-zA-Z0-9]{36}|AKIA[0-9A-Z]{16})', 'Potential hardcoded API token or credential'),
]

COMPILED = [(pid, sev, re.compile(pat, re.I), desc) for pid, sev, pat, desc in PATTERNS]

def scan_file(filepath):
    findings = []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        for idx, line in enumerate(lines, 1):
            for pid, sev, reg, desc in COMPILED:
                m = reg.search(line)
                if m:
                    findings.append({
                        'file': filepath,
                        'line': idx,
                        'rule': pid,
                        'severity': sev,
                        'desc': desc,
                        'matched': m.group(0).strip()
                    })
    except Exception as e:
        pass
    return findings

def scan_target(target_path):
    all_findings = []
    if os.path.isfile(target_path):
        all_findings.extend(scan_file(target_path))
    elif os.path.isdir(target_path):
        for root, dirs, files in os.walk(target_path):
            for f in files:
                if f.endswith(('.md', '.py', '.sh', '.js', '.ts', '.json', '.yaml', '.yml')):
                    fp = os.path.join(root, f)
                    all_findings.extend(scan_file(fp))
    return all_findings

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 audit.py <file-or-directory>")
        sys.exit(1)
        
    target = sys.argv[1]
    if not os.path.exists(target):
        print(f"Error: Target path '{target}' not found.")
        sys.exit(1)
        
    print(f"=== Scanning: {target} ===")
    findings = scan_target(target)
    
    if not findings:
        print("[OK] 0 threats detected. Clean skill library.")
        sys.exit(0)
        
    print(f"\n[ALERT] Found {len(findings)} potential security alert(s):")
    for f in findings:
        print(f"  [{f['severity']}] {f['rule']} in {os.path.basename(f['file'])}:{f['line']}")
        print(f"    Description: {f['desc']}")
        print(f"    Matched: {f['matched'][:80]}\n")
        
    has_critical = any(f['severity'] == 'CRITICAL' for f in findings)
    sys.exit(2 if has_critical else 1)

if __name__ == '__main__':
    main()
