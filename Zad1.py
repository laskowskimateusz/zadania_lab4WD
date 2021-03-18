from random import randint


plik = open('zadanie1.txt', 'w')
for x in range(20):
    plik.write(str(randint(0, 30)*2))
    plik.write("\n")
plik.close()
