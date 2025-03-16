def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18")
    return "Access Granted"

try:
    print(check_age(15))
    print(check_age(20))
except ValueError as e:
    print(e)