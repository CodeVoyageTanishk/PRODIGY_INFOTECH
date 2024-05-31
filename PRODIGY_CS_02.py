import re
def assess_password_strength(password):

    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None
    strength_score = 0
    if length_criteria:
        strength_score += 1
    if lowercase_criteria:
        strength_score += 1
    if uppercase_criteria:
        strength_score += 1
    if digit_criteria:
        strength_score += 1
    if special_char_criteria:
        strength_score += 1

    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Moderate"
    elif strength_score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, strength_score

def provide_feedback(password):
    feedback = []
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    if re.search(r'[a-z]', password) is None:
        feedback.append("Password should contain at least one lowercase letter.")
    if re.search(r'[A-Z]', password) is None:
        feedback.append("Password should contain at least one uppercase letter.")
    if re.search(r'\d', password) is None:
        feedback.append("Password should contain at least one digit.")
    if re.search(r'[\W_]', password) is None:
        feedback.append("Password should contain at least one special character (e.g., !, @, #, $, etc.).")

    return feedback
def main():
    password = input("Enter a password to assess: ")
    strength, score = assess_password_strength(password)
    feedback = provide_feedback(password)
    print(f"Password Strength: {strength} (Score: {score}/5)")
    if feedback:
        print("Feedback:")
        for comment in feedback:
            print(f" - {comment}")
if __name__ == "__main__":
    main()
