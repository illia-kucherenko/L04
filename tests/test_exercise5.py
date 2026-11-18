import os
import pytest
import exercise5
from exercise5 import *

def test_r1_ping_host_blocks_injection():
    # Attempt injection to create a file
    flag_file = "/tmp/injected_test_5"
    if os.path.exists(flag_file):
        os.remove(flag_file)
    
    # If vulnerable, this will run "touch" command
    ping_host(f"127.0.0.1; touch {flag_file}")
    
    assert not os.path.exists(flag_file), "Vulnerable to command injection!"

def test_r2_read_relative_file_blocks_traversal():
    # Attempt directory traversal out of safe_dir
    with open("/tmp/secret_file.txt", "w") as f:
        f.write("secret_data")
        
    with pytest.raises(ValueError):
        read_relative_file("../secret_file.txt")
