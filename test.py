""" Quiz and score test with python requesting api """

import requests

response = requests.get("https://opentdb.com/api.php?amount=5&category=18&difficulty=medium&type=multiple&encode=url3986")

data = response.json()

questions = data["questions"]

current_question = 0
display_question(questions[current_question])

def display_question(question):
    print(question["text"])

    for i, choice in enumerate(question["choices"]):
        print(f"{i + 1}. {choice}")

    answer = input("Enter your answer (1, 2, 3, or 4):")

    if answer == str(question["answer"]):
        print("Correct!")
    else:
        print("Incorrect.")

    global current_question
    current_question += 1
    if current_question < len(questions):
        display_question(questions[current_question])
    else:
        print("The game is over.")