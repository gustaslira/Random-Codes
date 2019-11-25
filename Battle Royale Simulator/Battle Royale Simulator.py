import random
import time
lista = []

def welcomeCompetitors():
    while True:
        player = input('Nome: ').title()
        if player == '':
            break
        lista.append(player)

def battleRoyaleBegin():
    while len(lista) > 1:
        x = random.randrange(len(lista))
        y = random.randrange(len(lista))
        if x == y:
            print(f'{lista[y]} cometeu suicídio')
            del lista[y]
            time.sleep(1)
            continue
        print(f'{lista[x]} matou {lista[y]}')
        del lista[y]
        time.sleep(1)

welcomeCompetitors()
print('Competidores:', len(lista))
battleRoyaleBegin()
print(lista[0], 'é o vencedor!')


