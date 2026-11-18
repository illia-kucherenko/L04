import os
import sqlite3
import subprocess

import pytest

import exercise2
from exercise2 import *


# bug report 1
def test_r1_is_passing_at_exactly_5():
    """Docstring: "True if the grade is 5 or more" -> 5 must pass."""
    assert is_passing(5) == True


# bug report 2
def test_r2_password_with_exactly_8_characters_is_valid():
    """Docstring: "At least 8 characters" -> 8 characters with a digit is valid."""
    assert is_valid_password("abcdefg1") == True


# bug report 3
def test_r3_clamp_limits_to_high():
    """Docstring: "limited to the range from low to high" -> 15 in [0, 10] becomes 10."""
    assert clamp(15, 0, 10) == 10
