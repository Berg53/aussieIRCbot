import random


def random_line():
    with open("insult.txt") as f:
        return random.choice(list(f))


def random_text():
    with open("random.txt") as f:
        return random.choice(list(f))
