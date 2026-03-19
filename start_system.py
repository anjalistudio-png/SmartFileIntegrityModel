import subprocess

print("Starting File Monitoring System...")

# Start monitoring program
subprocess.Popen(["py", "monitor.py"])

# Start dashboard
subprocess.Popen(["py", "-m", "streamlit", "run", "dashboard.py"])