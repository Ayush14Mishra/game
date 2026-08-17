import random

choices = ["rock", "paper", "scissors"]

wins = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

shortcuts = {
    "r": "rock",
    "p": "paper",
    "s": "scissors"
}

emoji = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

print("=" * 40)
print("      ROCK PAPER SCISSORS")
print("=" * 40)

while True:
    try:
        best_of = int(input("\nPlay best of 3, 5, or 7: "))
        if best_of in [3, 5, 7]:
            break
        print("Please choose 3, 5, or 7.")
    except ValueError:
        print("Enter a valid number.")

score = {"you": 0, "computer": 0}
history = []
streak = 0
needed_wins = best_of // 2 + 1

while score["you"] < needed_wins and score["computer"] < needed_wins:
    print("\n" + "-" * 40)
    print(f"Score → You: {score['you']} | Computer: {score['computer']}")
    print(f"First to {needed_wins} wins the match")
    print("Choose rock / paper / scissors")
    print("Shortcuts: r / p / s | Type quit to exit")

    user = input("Your choice: ").strip().lower()

    if user == "quit":
        print("\nGame ended by user.")
        break

    if user in shortcuts:
        user = shortcuts[user]

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print(f"You chose:      {emoji[user]} {user}")
    print(f"Computer chose: {emoji[computer]} {computer}")

    if user == computer:
        result = "Tie"
        print("It's a TIE!")
        streak = 0

    elif wins[user] == computer:
        result = "You won"
        score["you"] += 1
        streak += 1
        print("You WIN!")

        if streak >= 2:
            print(f"🔥 Winning streak: {streak}")

    else:
        result = "Computer won"
        score["computer"] += 1
        streak = 0
        print("Computer WINS!")

    history.append({
        "you": user,
        "computer": computer,
        "result": result
    })

print("\n" + "=" * 40)
print("             FINAL RESULT")
print("=" * 40)
print(f"You      : {score['you']}")
print(f"Computer : {score['computer']}")

if score["you"] > score["computer"]:
    print("\n🏆 You won the match!")
elif score["computer"] > score["you"]:
    print("\n🤖 Computer won the match!")
else:
    print("\nMatch ended without a winner.")

total_decisions = score["you"] + score["computer"]

if total_decisions > 0:
    win_percentage = (score["you"] / total_decisions) * 100
    print(f"Your win percentage: {win_percentage:.1f}%")

print("\nMatch History:")
for number, game in enumerate(history, start=1):
    print(
        f"{number}. You: {game['you']} | "
        f"Computer: {game['computer']} | "
        f"Result: {game['result']}"
    )
