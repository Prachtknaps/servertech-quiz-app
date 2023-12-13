import json
import random

from question import Question
from helpers import get_non_empty_input


class Quiz:
    def __init__(self, name: str, questions: list[Question]):
        self.name = name
        self.questions = questions

    def add_question(self, question):
        self.questions.append(question)

    def to_json(self):
        quiz_data = {'name': self.name, 'questions': []}
        for question in self.questions:
            quiz_data['questions'].append({'question': question.text, 'answers': question.answers})
        return quiz_data

    def save_to_file(self):
        existing_data = self.load_existing_data()
        existing_data.append(self.to_json())
        self.save_quiz_to_file(existing_data)

    def play(self):
        print(f"\nDu spielst jetzt das Quiz '{self.name}':\n")
        correct_answers = 0

        shuffled_questions = random.sample(self.questions, len(self.questions))

        for idx, question in enumerate(shuffled_questions, start=1):
            print(f"{question.text}")

            user_answer = get_non_empty_input(1, "> ")

            if user_answer.lower() in [answer.lower() for answer in question.answers]:
                print("Richtig!\n")
                correct_answers += 1
            else:
                correct_answer = question.answers[0]
                print(f"Falsch! Die richtige Antwort ist: {correct_answer}\n")

        print(f"Quiz '{self.name}' beendet. Du hast {correct_answers} von {len(self.questions)} Fragen richtig beantwortet.")

    @staticmethod
    def load_existing_data():
        existing_data = []
        try:
            with open('quiz.json', 'r', encoding='utf-8') as file:
                file_content = file.read()
                if file_content.strip():
                    file.seek(0)
                    existing_data = json.load(file)
        except FileNotFoundError:
            pass

        return existing_data

    @staticmethod
    def save_quiz_to_file(quiz_data):
        with open('quiz.json', 'w', encoding='utf-8') as file:
            json.dump(quiz_data, file, ensure_ascii=False, indent=2)