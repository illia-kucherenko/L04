import os
import sqlite3
import subprocess

import pytest

import exercise3
from exercise3 import *


# bug report 1
def test_r1_average_of_empty_list_is_0():
    """Docstring: "An empty list has average 0" (now: ZeroDivisionError)."""
    assert average([]) == 0


# bug report 2
def test_r2_first_word_of_empty_text_is_empty():
    """Docstring: 'or "" if the text is empty' (now: IndexError)."""
    assert first_word("") == ""


# bug report 3
def test_r3_percent_with_total_0_is_0():
    """Docstring: "If total is 0, the result is 0" (now: ZeroDivisionError)."""
    assert percent(5, 0) == 0
