import random

print("🎯 Welcome to the NUMBER GUESSING GAME!")

# Computer chooses a number
computer = random.randint(1, 20)

while True:
    try:
        user = int(input("Enter any number between 1 and 20: "))

        if user < 1 or user > 20:
            print("⚠️ Invalid number! Please enter a number between 1 and 20.")
            continue

        if user == computer:
            print("✅ RIGHT GUESS, YOU WON!")
            break
        elif user < computer:
            print("📉 Too low! Try again.")
        else:
            print("📈 Too high! Try again.")

    except ValueError:
        print("❌ Invalid input! Please enter a number.")
