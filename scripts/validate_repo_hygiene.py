from pathlib import Path
bad_names = {".env", "credentials.json", "secrets.json"}
bad_dirs = {".venv", "venv", "outputs", "logs", "__pycache__"}
issues = []
for p in Path(".").rglob("*"):
    if p.name in bad_names or set(p.parts) & bad_dirs:
        issues.append(str(p))
if issues:
    print("Potential hygiene issues:")
    print("\n".join(issues))
    raise SystemExit(1)
print("No obvious hygiene issues found.")
