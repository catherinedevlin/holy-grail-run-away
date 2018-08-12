import re
import random
import subprocess
import enquiries

blankline = re.compile(r'\n\s*\n', re.DOTALL)

SOURCE = 'trivia.txt'

with open(SOURCE) as infile:
    content = infile.read()

class Question:

    def __init__(self, raw):
        self.raw = raw
        lines = self.raw.splitlines()
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
        subprocess.run('clear')
        answer = enquiries.choose(self.question, options)
        result = answer == self.correct
        try:
            if result:
                subprocess.run(('xplayer', 'video/correct.mp4'), timeout=6)
            else:
                subprocess.run(('xplayer', 'video/wrong.mp4'), timeout=6)
        except subprocess.TimeoutExpired:
            pass
        return result


def load():
    raw_questions = blankline.split(content)
    return [Question(r) for r in raw_questions]


if __name__ == '__main__':
    questions = load()
    streak = 0
    while True:
        print('\n\nYour winning streak is {} questions long.\n\n'.format(streak))
        question = random.choice(questions)
        result = question.ask()
        if result:
            streak += 1
        else:
            streak = 0
