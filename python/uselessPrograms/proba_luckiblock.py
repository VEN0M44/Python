import random

essais = 10000
tentative = 0

for i in range(essais):
    passed_events = []
    while len(passed_events) != 100:
        tentative += 1
        random_event = random.randint(0,99)
        if random_event not in passed_events:
            passed_events.append(random_event)

print(tentative / essais)