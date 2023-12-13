class Question:
    def __init__(self, text, answers):
        self.text = text
        self.answers = answers

    def __str__(self):
        return f"Fragetext: {self.text}\nGültige Antworten: {', '.join(self.answers)}\n"
