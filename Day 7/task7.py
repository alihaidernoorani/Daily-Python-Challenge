import time
import random

questions = [
    {
        "question": "What is the standard room temperature in Kelvin?",
        "options": ["A) 98 K", "B) 198 K", "C) 273 K", "D) 373 K"],
        "answer": "C"
    },
    {
        "question": "Fathometer is used to measure:",
        "options": ["A) Earthquakes", "B) Rainfall", "C) Ocean depth", "D) Sound intensity"],
        "answer": "C"
    },
    {
        "question": "What gas do plants absorb from the atmosphere?",
        "options": ["A) Oxygen", "B) Carbon dioxide", "C) Nitrogen", "D) Hydrogen"],
        "answer": "B"
    },
    {
        "question": "What planet is known as the Red Planet?",
        "options": ["A) Venus", "B) Jupiter", "C) Mars", "D) Saturn"],
        "answer": "C"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A) CO2", "B) H2O", "C) O2", "D) NaCl"],
        "answer": "B"
    },
    {
        "question": "What is 12 × 8?",
        "options": ["A) 96", "B) 92", "C) 88", "D) 100"],
        "answer": "A"
    },
    {
        "question": "What is the square root of 144?",
        "options": ["A) 10", "B) 12", "C) 14", "D) 16"],
        "answer": "B"
    },
    {
        "question": "Solve: 15 + (6 ÷ 2) * 3",
        "options": ["A) 24", "B) 27", "C) 30", "D) 33"],
        "answer": "B"
    },
    {
        "question": "If a triangle has angles 50° and 60°, what is the third angle?",
        "options": ["A) 70°", "B) 80°", "C) 90°", "D) 100°"],
        "answer": "B"
    },
    {
        "question": "What is the value of π (pi) to two decimal places?",
        "options": ["A) 3.12", "B) 3.14", "C) 3.16", "D) 3.18"],
        "answer": "B"
    }
]

random.shuffle(questions)  # Shuffle the questions
points = 0

# Ask 5 random questions
for questionNumber, q in enumerate(questions[:5], 1):
    start = time.time()

    # Display question and options
    print(f"\nQ{questionNumber}: {q['question']}")
    for option in q["options"]:
        print(option)

    # Get user's answer
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    end = time.time()
    time_taken = end - start

    # Check time limit
    if time_taken > 10:
        print(f"\n⏳ Time up! The correct answer is {q['answer']}\n")
    else:
        # Check if the answer is correct
        if answer == q['answer']:
            print("\n✅ Correct! 🎉\n")
            points += 1
        else:
            print(f"\n❌ Incorrect! The correct answer is {q['answer']}\n")

# Display final score
print(f"🎯 Final Score: {points}/5")
