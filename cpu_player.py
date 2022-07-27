import random


class Cpu:
    def __init__(self):
        self.options = ['ROCK', 'PAPER', 'SCISSOR']

    def generate_answer(self):
        self.answer = random.choice(self.options)
        return self.answer
