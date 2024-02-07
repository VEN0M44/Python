import random

pi = open(r"C:\Users\NEVEN.RAAPOTO\programmation\python\recentsProjects\piDigits.txt", "r").readlines()

piDigits = "".join(list(map(lambda x:"".join(list(filter(lambda y:y.isdigit(), x))), pi))) #formatage des tableaux imbriqués contenant les décimales en un unique string

while 0: #programme dans lequel nous devons réciter les décimales qui suivent celles données aléatoirement

    randomNum = random.randint(0, 2016)
    digitsToContinue = piDigits[randomNum : randomNum + 10] #10 décimales piochées aléatoirement
    
    print("Pi digits :", digitsToContinue)

    inp = input("Next digits : ")

    answer = piDigits[randomNum + 10 : randomNum + 10 + len(inp)] #vérification si les décimales entrées suivent bien celles données
    
    print("[true]" if answer == inp else "[false]", end="")
    print(f"The answer is {digitsToContinue} {answer} from {randomNum + 1}th pi décimal")


recitedDecimals = "3."


while 1: #programme qui permet de réciter les décimales de pi depuis le début

    counter = len(recitedDecimals)  #nombre de décimales récitées
    lives = 3

    if counter < 8:     #si le compteur est inférieur à 8 on print toutes les décimales récitées
        number = recitedDecimals
    else:               #sinon seulement les 8 derniers
        number = recitedDecimals[-8:counter]
    
    inp = input(number)

    if inp == piDigits[counter - 2 : counter + len(inp) - 2]: #test si les décimales entrées sont correctes
        recitedDecimals += inp
    else:
        lives -= 1
        print("Erreur :", lives, "vies restantes")
