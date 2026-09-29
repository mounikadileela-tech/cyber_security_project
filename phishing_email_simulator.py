print("=== Phishing Email Simulation ===")

email = input("Enter a sample email message: ")

score = 0

# Check for common phishing warning signs
if "urgent" in email.lower():
    score += 1

if "verify your account" in email.lower():
    score += 1

if "click here" in email.lower():
    score += 1

if "password" in email.lower():
    score += 1

if "free" in email.lower():
    score += 1

print("\n=== Analysis Result ===")

if score >= 3:
    print("Warning: This email has several phishing indicators.")
elif score >= 1:
    print("Caution: This email contains some suspicious indicators.")
else:
    print("No common phishing indicators detected.")

print("Phishing indicator score:", score)

