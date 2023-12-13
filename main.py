
from quiz import Quiz
from question import Question
from helpers import get_non_empty_input, build_multiline_input_string, build_multiline_input_list


def play_quiz():
    quizzes = Quiz.load_existing_data()

    if not quizzes:
        print("Es gibt keine gespeicherten Quizzes.")
        return

    print("Verfügbare Quizzes:")
    for idx, quiz in enumerate(quizzes, start=1):
        print(f"{idx}. {quiz['name']}")

    print("\nWelches Quiz möchtest du spielen? Bitte wähle die Nummer:")
    quiz_index = get_non_empty_input(1, "> ")

    try:
        selected_quiz_data = quizzes[int(quiz_index) - 1]
        quiz = Quiz(selected_quiz_data['name'], [])

        for question_data in selected_quiz_data['questions']:
            question = Question(question_data['question'], question_data['answers'])
            quiz.add_question(question)

        quiz.play()

    except (IndexError, ValueError):
        print("Ungültige Eingabe.")


def create_quiz():
    print("\nBitte gib einen Namen für dein Quiz ein (mindestens 2 Zeichen)")
    quiz_name = get_non_empty_input(2, "> ")
    questions = []

    while True:
        print("Bitte gib eine Frage ein (Abbruch mit 'question -f' oder 'question --finish'):")
        question_text = build_multiline_input_string(['question -f', 'question --finish'], "> ")

        print("Bitte gib die gültige(n) Antwort(en) ein (Abbruch mit 'answers -f' oder 'answers --finish'):")
        answer_options = build_multiline_input_list(['answers -f', 'answers --finish'], "> ")

        questions.append(Question(question_text, answer_options))

        print("Möchtest du eine weitere Frage hinzufügen? (Ja/Nein)")
        add_another = get_non_empty_input(1)
        if add_another.lower() == 'ja':
            continue
        elif add_another.lower() == 'nein':
            break
        else:
            print('Ungültige Eingabe. Deine Antwort wurde als \'Ja\' gewertet.')

    if len(questions) < 3:
        print("Konnte das Quiz nicht hinzufügen: Das Quiz muss mindestens 3 Fragen beinhalten.")
        return

    quiz = Quiz(quiz_name, questions)
    quiz.save_to_file()

    print(f"\nQuiz '{quiz_name}' wurde erstellt und zu 'quiz.json' hinzugefügt:\n")
    for idx, question in enumerate(questions, start=1):
        print(f"Fragetext {idx}: {question.text}")
        print(f"Gültige Antworten {idx}: {', '.join(question.answers)}\n")


def delete_quiz():
    quizzes = Quiz.load_existing_data()

    if not quizzes:
        print("Es gibt keine gespeicherten Quizzes.")
        return

    print("Verfügbare Quizzes zum Löschen:")
    for idx, quiz in enumerate(quizzes, start=1):
        print(f"{idx}. {quiz['name']}")

    print("\nWelches Quiz möchtest du löschen? Bitte wähle die Nummer:")
    quiz_index = get_non_empty_input(1, "> ")

    try:
        selected_quiz = quizzes.pop(int(quiz_index) - 1)
        Quiz.save_quiz_to_file(quizzes)
        print(f"\nQuiz '{selected_quiz['name']}' wurde gelöscht.")
    except (IndexError, ValueError):
        print("Ungültige Eingabe.")


def main():
    while True:
        print("\nWas möchtest du tun?\n1. Quiz spielen\n2. Quiz erstellen\n3. Quiz löschen\n4. Beenden")
        print("\nBitte wähle eine Option (1/2/3/4):")

        choice = get_non_empty_input(1, "> ")

        if choice == '1':
            play_quiz()
        elif choice == '2':
            create_quiz()
        elif choice == '3':
            delete_quiz()
        elif choice == '4':
            print("Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe. Bitte wähle eine der verfügbaren Optionen.")


if __name__ == "__main__":
    main()
