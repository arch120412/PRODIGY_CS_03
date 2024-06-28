import re

def assess_password_strength(password):
    # Initialize score and feedback list
    score = 0
    feedback = []

    # Criteria 1: Length of the password
    length = len(password)
    if length >= 8:
        score += 2
    elif 5 <= length < 8:
        score += 1
    feedback.append(f"Length: {length} characters")

    # Criteria 2: Presence of uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("Contains uppercase letters")
    else:
        feedback.append("Missing uppercase letters")

    # Criteria 3: Presence of lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("Contains lowercase letters")
    else:
        feedback.append("Missing lowercase letters")

    # Criteria 4: Presence of numbers
    if re.search(r'\d', password):
        score += 1
        feedback.append("Contains numbers")
    else:
        feedback.append("Missing numbers")

    # Criteria 5: Presence of special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
        feedback.append("Contains special characters")
    else:
        feedback.append("Missing special characters")

    # Determine the strength of the password based on the score
    if score >= 6:
        strength = "Very Strong"
    elif 4 <= score < 6:
        strength = "Strong"
    elif 3 <= score < 4:
        strength = "Moderate"
    elif 1 <= score < 3:
        strength = "Weak"
    else:
        strength = "Very Weak"

    feedback.append(f"Overall strength: {strength}")

    # Provide feedback
    return strength, feedback


password = input("Enter your password: ")
strength, feedback = assess_password_strength(password)
for line in feedback:
    print(line)
