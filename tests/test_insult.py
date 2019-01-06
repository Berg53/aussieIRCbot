import random
from mock import patch

from src.modules.insult import Insult

random.seed(1)


@patch('src.modules.insult.random', random)
def test_insult_user():
    i = Insult()
    assert i.run('Berg') == 'Berg, you nitwit'


def test_inult_empty():
    i = Insult()
    assert i.run('') == 'Nincompoop'
