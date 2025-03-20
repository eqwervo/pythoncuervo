import random

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# union de cada conjunto pregunta, respuesta, indice. 
# Reemplazo random.choise por random.sample que no repite ocurrencias
questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)

# puntuaje del usuario
user_points = float(0)

# El usuario deberá contestar 3 preguntas. Se reemplaza el range por un for 
# que itera sobre el conjunto (Preg,Res,Ind) que fueron unidas en el zip y dado k=3 son tres preguntas
for quest, answ, ind in questions_to_ask:
   
# Se muestra la pregunta y las respuestas posibles
    print(quest)
    for i,answer in enumerate(answ):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente

    for intento in range(2):
            # Comprueba que sea numerico y que esté entre los valores de respuesta posibles
            user_answer = input("Respuesta: ")
            if user_answer.isnumeric():
                user_answer = int(user_answer) - 1
                if 0 <= user_answer < len(answ):
                    if user_answer == ind:
                        print("¡Correcto!")
                        user_points += 1
                        break
                    else:
                        user_points -= 0.5
                else:
                    print("Ingrese una respuesta válida.")
            else: 
                print("Ingrese una respuesta válida.")
    # si no logra en dos intentos responder correctamente entra en el else
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        #user_points -= 0.5
        print(answ[ind])


    # Se imprime un blanco al final de la pregunta
    print()
print(f"Su puntaje fue:  {user_points}")