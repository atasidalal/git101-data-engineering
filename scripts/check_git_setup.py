import subprocess
for cmd in ["git --version", "git config --global user.name", "git config --global user.email"]:
    try:
        print(cmd, "=>", subprocess.check_output(cmd, shell=True, text=True).strip())
    except subprocess.CalledProcessError:
        print(cmd, "=> not configured")
