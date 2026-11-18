# Bug reports for exercise2.py

Line: 3
Problem: The docstring says "True if the grade is 5 or more", which means grade >= 5, but the function uses grade > 5, making it false for grade exactly 5.
Example: is_passing(5) returns False, expected True.
Fix: return grade >= 5

Line: 8
Problem: The docstring says "At least 8 characters", which means length >= 8, but the function uses len(password) > 8, making it false for exactly 8 characters.
Example: is_valid_password("abcdefgh") returns False, expected True.
Fix: return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 12
Problem: The function clamp returns max(low, min(x, low)), which incorrectly uses low twice. It should return max(low, min(x, high)) to properly clamp between low and high.
Example: clamp(3, 1, 5) returns 3, which is correct, but clamp(7, 1, 5) returns 5, which is correct; however, clamp(0, 1, 5) returns 1, which is correct, but the logic is flawed because min(x, low) will always be low, making it redundant. The correct behavior should be min(max(x, low), high).
Example: clamp(0, 1, 5) returns 1, which is correct, but the function incorrectly returns max(low, min(x, low)) which simplifies to max(low, low) = low, which is correct only if x < low. For x > high, it fails. For example, clamp(10, 1, 5) returns max(1, min(10, 1)) = 1, but should return 5.
Example: clamp(10, 1, 5) returns 1, expected 5.
Fix: return max(low, min(x, high))
