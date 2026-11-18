import os
import subprocess

def ping_host(host):
    """Runs ping command on the host. Returns True if successful, False otherwise. Prevent arbitrary command injection!"""
    # Safe: Pass arguments as a list to subprocess without shell=True
    try:
        res = subprocess.run(["ping", "-c", "1", host], capture_output=True, text=True, check=True)
        return res.returncode == 0
    except Exception:
        return False

def read_relative_file(filename):
    """Reads contents of a file inside the '/tmp/safe_dir' folder. Prevent reading files outside this folder (no '..')."""
    safe_dir = os.path.abspath("/tmp/safe_dir")
    os.makedirs(safe_dir, exist_ok=True)
    
    # Safe: Resolve paths and verify target directory
    target_path = os.path.abspath(os.path.join(safe_dir, filename))
    if not target_path.startswith(safe_dir):
        raise ValueError("Directory Traversal attempt detected!")
        
    with open(target_path, 'r') as f:
        return f.read()
