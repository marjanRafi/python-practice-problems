# Password Validator (Security Utility)

def validate_password(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in "!@#$%^&*()" for char in password):
        return False
    return True

if __name__ == "__main__":
    password = "Test@1234"
    print(f"Is valid password: {validate_password(password)}")