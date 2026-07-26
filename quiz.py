import random as r

questions = [
    "What is the capital city of Australia?",
    "Which planet is known as the Red Planet?",
    "Who wrote the famous play Romeo and Juliet?",
    "What is the largest ocean on Earth?",
    "How many continents are there in the world?",
    "Which is the largest mammal in the world?",
    "What is the chemical symbol for gold?",
    "Who was the first person to walk on the Moon?",
    "What is the national animal of India?",
    "Which gas do humans need to breathe to survive?"
]

answers = [
    "Canberra",
    "Mars",
    "William Shakespeare",
    "Pacific Ocean",
    "7",
    "Blue whale",
    "Au",
    "Neil Armstrong",
    "Bengal Tiger",
    "Oxygen"
]

score = 0

questions_list = list(range(len(questions)))

r.shuffle(questions_list)

for i in questions_list:
    print("\n" + questions[i])

    user_answer = input("Your answer: ")

    if user_answer.lower() == answers[i].lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("The correct answer is:", answers[i])

print("\nYour final score is:", score, "out of", len(questions))
if score == len(questions):
    print("===========>YOU WIN<=============\n","Congratulations! You got a perfect score!")