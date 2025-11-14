def categorize_by_age(age):
    if age < 0:
        return "Invalid age"
    elif age <= 9:
        return "Child"
    elif age <= 18:
        return "Teenager"
    elif age <= 64:
        return "Adult"
    else:
        return "Senior"