slowa = ['przykład1', 'przykład2', 'przykład3']
with open('tekst.txt', 'w', encoding='UTF-8') as plik:
    for x in range(len(slowa)):
        plik.write(slowa[x])
        plik.write('\n')
with open('tekst.txt', 'r', encoding='UTF-8') as plik:
    print(plik.read())
