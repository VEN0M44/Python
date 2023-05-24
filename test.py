import random
import functools

number = functools.reduce(lambda x, y:x + y, range(10), [])

#print(*number, sep="\n")

print(number)