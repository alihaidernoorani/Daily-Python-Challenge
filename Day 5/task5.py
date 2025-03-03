import random

correct = random.randint(1, 100)
for num in range(1, 8):
  try:
    guess = int(input("Guess the number (between 1 and 100): "))
  except ValueError:
    print("Error: Enter a valid number")
    continue
  if guess == correct:
    print("Congratulations! You guessed the correct number")
    break
  elif guess < correct:
    print("Too low! Try again.")
  elif guess > correct:
    print("Too high! Try again.")
else:
  print("Game over")
  print(f"The correct answer is {correct}")

