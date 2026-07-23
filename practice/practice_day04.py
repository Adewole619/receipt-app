print("=== Age Validation ===")

age = int(input("Your age: "))
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")

print("=== Score Validation ===")

score = int(input("Enter a score: "))
if score > 90:
    print("Excellent")
elif score >= 70 and score <= 89:
    print("Good")
elif score >= 50 and score<= 68:
    print("Pass")
else:
    print("Fail")