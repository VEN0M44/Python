import random

#programme obsolète

#calcul les probabilitées de réussite d'un opener sur tetris

dependencies = [    #chaque élément contient un string correspondant à une dépendance de l'opener
    "Z>O",
    "S>O",
    "T>O",
    "S>L",
    "Z>J",
    "O>I"

]                   #"T>L" veut dire que le T doit arriver avant le L

bag = ["O","I","S","Z","L","J","T"]
used = []
soluce = []

for i in range(5040):
    result = True
    random_bag = bag
    while random_bag in used:
        random.shuffle(random_bag)

    used.append(list(random_bag))
    

    for j in dependencies:
        if random_bag.index(j[0]) < random_bag.index(j[2]):
            result = False
            break
    if result:
        soluce.append(list(random_bag))
    
    """O_index = random_bag.index("O")

    if random_bag.index("T") < O_index and random_bag.index("S") < O_index :
        if random_bag.index("O") < random_bag.index("I") and random_bag.index("Z") < random_bag.index("J") :
            soluce.append(list(random_bag))"""

print("----------------------")
for i in soluce:
    print("fail : ", end="")
    print(*i)

possibility = len(soluce)
print(f"il y a {possibility} possibilitées d'échecs sur 5040 ce qui fait {(5040 - possibility) / 5040 * 100}% de réussite")