import random

def random_line():
    return(random.choice(list(open('insult.txt'))))

def random_text(): 
    return(random.choice(list(open('random.txt'))))
