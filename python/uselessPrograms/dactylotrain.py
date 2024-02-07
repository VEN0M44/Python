import random

inp = '.'

while 1:
    char = random.choice(['ô','î','û','ù','ê','è','é','à','â','ç'])
    while char not in inp:
        inp = input(char + " : ")