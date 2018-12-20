import random
import os.path


def random_line(insult_file=None):
    if insult_file is None:
        insult_file = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "data", "insult.txt"
        )
    with open(insult_file) as f:
        return random.choice(list(f))


def random_text(random_file=None):
    if random_file is None:
        random_file = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "data", "random.txt"
        )
    with open(random_file) as f:
        return random.choice(list(f))
