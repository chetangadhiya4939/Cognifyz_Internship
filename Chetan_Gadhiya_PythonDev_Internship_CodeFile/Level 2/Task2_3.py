import re


def pass_strenth_check(password):

    criteria = {
        "length>=8": len(password) >= 8,
        "is_Upper": bool(re.search(r"[A-Z]", password)),
        "is_Lower": bool(re.search(r"[a-z]", password)),
        "is_digit": bool(re.search(r"\d", password)),
        "special_char": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
    }
    strength_score = 0

    for crit, met in criteria.items():
        if met:
            strength_score += 1

    if strength_score < 3:
        stength = "Weak"
    elif strength_score < 5:
        stength = "Moderate"
    else:
        stength = "Strong"

    print("Password Stength: ", stength)
    print("Criteria met: ")
    for crit, met in criteria.items():
        print(f"{crit.replace("_"," ").capitalize()}: {"✔" if met else "✘"}")


password = input("Enter your password: ")
pass_strenth_check(password)
