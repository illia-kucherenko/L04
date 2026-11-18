import hmac
import os


# The password is not in the code anymore: it comes from an environment variable.
# If the variable is not set, ADMIN_PASSWORD is "" and nobody can log in as admin.
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "")


def check_admin(password):
    """true if the password is the admin password"""
    # compare_digest takes the same time whether the first or the last character is wrong
    return ADMIN_PASSWORD != "" and hmac.compare_digest(password.encode(), ADMIN_PASSWORD.encode())


def find_user(db, username):
    """The user's row, or None if the username does not exist"""
    # parameterized query: username is passed as data, never pasted into the SQL text
    return db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
