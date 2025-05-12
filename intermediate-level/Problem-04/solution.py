# Validate Email Format
import re
def validate_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(regex, email))

if __name__ == "__main__":
    email = "test@domain.com"
    print(f"Is valid email: {validate_email(email)}")