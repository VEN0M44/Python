import functools, math


infos = [       #chaque élément correspond à une gdc
    "l-7"       #un string commencant par "l" pour lose ou "w" pour win
]               #un numero correspondant au nombre de base attaquée
                #"l-7" pour mettre le compteur à zero


objective = 6438

infoString = functools.reduce(lambda x, y: x + y, infos ,"")

exp = sum([int(i[1:]) * 5 + {'l': 35, 'w': 85}[i[0]] for i in infos])

if exp > objective:
    objective = 1000 * (exp // 1000 + 1)

rest = objective - exp

win, lose, total = infoString.count('w'), infoString.count('l'), len(infos)

toPrint = [
f"Wins     : {win}",
f"Lost     : {lose}",
f"Total    : {total}",
f"Rate     : {int(win / total * 100)}%",
f"Exp      : {exp}/{objective}",
f"War Left : {math.ceil(rest / 335)} ~ {math.ceil(rest / 285)}"
]

print(*toPrint, sep="\n")