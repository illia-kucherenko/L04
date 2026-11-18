# Bug reports for exercise4.py

Line: 4
Problem: The admin password "admin123" is hardcoded in the source code, which is a security vulnerability. Anyone who reads the code can immediately discover the password, making the system easily exploitable.
Example: An attacker can simply inspect the source code and see that the admin password is "admin123".
Fix: Replace the hardcoded password with a value from an environment variable: `ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "default_password")`

Line: 7
Problem: The docstring says "true if the password is the admin password", but the function returns `ADMIN_PASSWORD != "" and password == ADMIN_PASSWORD`. This condition is flawed because it allows any non-empty password to pass if it's not the correct one, and it incorrectly evaluates to True when the password is empty. Moreover, using `==` for password comparison leaks timing information, which can be exploited in timing attacks.
Example: check_admin("") returns True, which contradicts the expected behavior of only accepting "admin123". Also, an attacker could potentially infer the password through timing differences.
Fix: Replace the comparison with `hmac.compare_digest` to prevent timing attacks. However, since no HMAC key is provided, we must first fix the hardcoded password and then use secure comparison. The corrected function should be: `return hmac.compare_digest(password.encode(), ADMIN_PASSWORD.encode())`

Line: 14
Problem: The function uses string formatting with f-strings to build SQL queries directly from user input, which is vulnerable to SQL injection attacks. An attacker can inject malicious SQL by providing a username like "' OR '1'='1".
Example: find_user(db, "' OR '1'='1") returns a result that could allow unauthorized access or data leakage, such as bypassing authentication or retrieving all user data.
Fix: Replace the f-string with parameterized queries using ? placeholders: `return db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()`
