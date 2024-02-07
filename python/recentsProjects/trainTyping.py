import random, string, time

print(string.printable[:-11] + string.printable[-10:-7])

#paramètres :
nombreDeTest = 25
nombreDeCaratère = 1

startTime = time.time()
inp = ""
caracterList = string.printable[:-11] + string.printable[-10:-7] + "ôîûùêèéàâçÀÈ"

for i in range(nombreDeTest):
    toWrite = "".join([random.choice(caracterList) for i in range(nombreDeCaratère)])
    while inp != toWrite.rstrip(" "):
      inp = input(toWrite + " : ")

print("Score :", int(time.time() - startTime), "seconds")