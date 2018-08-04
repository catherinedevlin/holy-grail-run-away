import re
import random
import enquiries

blankline = re.compile(r'\n\s*\n', re.DOTALL)

SOURCE = 'trivia.txt'

with open(SOURCE) as infile:
    content = infile.read()


class Question:
    def __init__(self, raw):
        self.raw = raw
        lines = raw.splitlines()
        self.question = lines.pop(0)
        self.lines = lines
        self.correct = lines[0]

    def dict(self):
        options = self.lines.copy()
        random.shuffle(options)
        return {
            'question': self.question,
            'choices': options,
            'answer': self.answer
        }

    def ask(self):
        options = self.lines.copy()
        random.shuffle(options)
        answer = enquiries.choose(self.question, options)
        return answer == self.correct


def load():
    raw_questions = blankline.split(content)
    return [Question(r) for r in raw_questions]


if __name__ == '__main__':
    questions = load()
    while True:
        question = random.choice(questions)
        print(question.ask())
