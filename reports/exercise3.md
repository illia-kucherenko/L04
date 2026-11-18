# Bug reports for exercise3.py

Line: 3
Problem: The docstring states that an empty list has an average of 0, but the function divides by len(numbers), which raises a ZeroDivisionError for an empty list. The code does not handle the empty list case as specified.
Example: average([]) raises ZeroDivisionError, expected 0.
Fix: return sum(numbers) / len(numbers) if numbers else 0

Line: 8
Problem: The docstring states that the function returns "" if the text is empty, but splitting an empty string with split() returns an empty list, and accessing index 0 on an empty list raises IndexError. The code does not handle the empty text case as specified.
Example: first_word("") raises IndexError, expected "".
Fix: return text.split()[0] if text.split() else ""

Line: 12
Problem: The docstring states that if total is 0, the result is 0, but the function divides by total, which raises ZeroDivisionError when total is 0. The code does not handle the zero total case as specified.
Example: percent(5, 0) raises ZeroDivisionError, expected 0.
Fix: return part / total * 100 if total != 0 else 0
