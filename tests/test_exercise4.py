import os
import sqlite3
import subprocess

import pytest

import exercise4
from exercise4 import *


# bug report 1
def test_r1_admin_password_not_in_source_code():
    """The admin password must not be written in the code: anyone who reads the repo knows it."""
    import inspect
    assert "admin123" not in inspect.getsource(exercise4)


# bug report 2
def test_r2_check_admin_uses_constant_time_compare():
    """Comparing a secret with == leaks timing information: use hmac.compare_digest."""
    import inspect
    assert "compare_digest" in inspect.getsource(check_admin)


# bug report 3
def test_r3_find_user_blocks_sql_injection():
    """An attack input must not return a row: "' OR '1'='1" is not a username."""
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE users (username TEXT, email TEXT)")
    db.execute("INSERT INTO users VALUES ('ana', 'ana@mail.com')")
    assert find_user(db, "x' OR '1'='1") is None
