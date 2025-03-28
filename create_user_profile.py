def create_user_profile(**kwargs):
    if "name" not in kwargs or "email" not in kwargs:
        raise ValueError("Die Eigenschaften 'name' und 'email' sind erforderlich.")

    profile = {}
    for key, value in kwargs.items():
        profile[key] = value

    return profile

# Beispielverwendung:
alice = create_user_profile(name="Alice", email="alice@example.com", age=33, city="New York")
bob = create_user_profile(name="Bob", email="bob@example.com", last_name="Smith", age=22, phone_number=1234567890)

print(alice)
print(bob)