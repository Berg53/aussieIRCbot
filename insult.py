import random

def random_line():
    print 'debug insult'
    return(random.choice(list(open('insult.txt'))))
