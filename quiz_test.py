""" quiz and score test with python without api url """

questions = [
    {
        "question": "¿Cuál es el capital de Francia?",
        "options": ["Paris", "Londres", "Berlín", "Roma"],
        "answer": 0
    },
    {
        "question": "¿Cuál es la moneda de España?",
        "options": ["Euro", "Libra", "Dólar", "Franco Suizo"],
        "answer": 0
    },
    {
        "question": "¿Cuál es la altura del Monte Everest?",
        "options": ["8.848 metros", "7.708 metros", "6.962 metros", "9.167 metros"],
        "answer": 0
    }
]

SCORE = 0
for i, question in enumerate(questions):
    print(f"Pregunta {i + 1}: {question['question']}")
    for j, option in enumerate(question["options"]):
        print(f"{j + 1}. {option}")
    user_answer = int(input("Seleccione la opción correcta: ")) - 1
    if user_answer == question["answer"]:
        print("Respuesta correcta!")
        SCORE += 1
    else:
        print("Respuesta incorrecta.")
    print(f"Puntos: {SCORE}")

    print("")

print(f"Juego terminado! Puntos totales: {SCORE}")
