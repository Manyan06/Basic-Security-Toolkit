import re

def has_repeated_chars(password):
    """
    Detects sequences like 'aaaa', '1111', etc.
    """
    return re.search(r"(.)\1{2,}", password)  # 3+ repeated chars


def has_keyboard_pattern(password):
    """
    Detects common keyboard sequences
    """
    patterns = [
        "qwerty", "asdf", "zxcvbn",
        "12345", "abcd", "qaz", "wsx"
    ]

    password_lower = password.lower()

    for pattern in patterns:
        # Check forward and reversed patterns
        if pattern in password_lower or pattern[::-1] in password_lower:
            return pattern
    return None


def check_password_strength(password):
    score = 0
    feedback = []

    length = len(password)

    # Length check
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        feedback.append("Password is too short (min 8, recommended 12+)")

    # Character checks
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character")

    # ---------------------------
    # NEW: Repeated characters
    # ---------------------------
    if has_repeated_chars(password):
        score -= 1
        feedback.append("Avoid repeated characters (e.g., 'aaa', '111')")

    # ---------------------------
    # NEW: Keyboard patterns
    # ---------------------------
    pattern = has_keyboard_pattern(password)
    if pattern:
        score -= 1
        feedback.append(f"Avoid keyboard pattern: '{pattern}'")

    # ---------------------------
    # Common weak words
    # ---------------------------
    common_patterns = ["password", "admin", "letmein"]
    for p in common_patterns:
        if p in password.lower():
            score -= 1
            feedback.append(f"Avoid common word: '{p}'")

    # Strength rating
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, score, feedback


# ---------------------------
# Main Program
# ---------------------------
if __name__ == "__main__":
    print("=== Password Strength Checker ===")

    password = input("Enter your password: ")

    strength, score, feedback = check_password_strength(password)

    print("\nStrength:", strength)
    print("Score:", score, "/ 6")

    if feedback:
        print("\nSuggestions:")
        for tip in feedback:
            print("-", tip)
    else:
        print("\nGood password 👍")


# Output:

# === Password Strength Checker ===
# Enter your password: Passsss

# Strength: Weak
# Score: 1 / 6

# Suggestions:
# - Password is too short (min 8, recommended 12+)
# - Include at least one number
# - Include at least one special character
# - Avoid repeated characters (e.g., 'aaa', '111')


# === Password Strength Checker ===
# Enter your password: Password@123

# Strength: Strong
# Score: 5 / 6

# Suggestions:
# - Avoid common word: 'password'