import random
from listapalavras import lista_de_palavras

def palavra_aleatoria():
    return random.choice(lista_de_palavras)

palavra = palavra_aleatoria()

listaL = []

chances = 7

ganhou = False


while True:
    print('Descubra a palavra:')
    for letra in palavra:
        if letra.lower() in listaL:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print('')
    
    print(f'Você tem {chances} chances')
    
    if chances == 7:
        print()
        print("|----- ")
        print("|    | ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    elif chances == 6:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    elif chances == 5:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|    | ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    elif chances == 4:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|    |\ ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    elif chances == 3:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\ ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    elif chances == 2:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\ ")
        print("|    | ")
        print("|      ")
        print("_      ")
        print()
    elif chances == 1:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\ ")
        print("|    | ")
        print("|     \ ")
        print("_      ")
        print()

    tentativa = input('Escreva a letra: ')
    if tentativa.lower() in listaL:
        print('ESSA LETRA JÁ FOI ESCOLHIDA!')
        tentativa = ''
    else:
        listaL.append(tentativa.lower())

    if tentativa.lower() not in palavra:
        chances -= 1
    tentativa = ''

    ganhou = True
    for letra in palavra:
        if letra.lower() not in listaL:
            ganhou = False

    if chances == 0:
        print('PUXEM A CORDA!!!')
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\ ")
        print("|    | ")
        print("|   / \ ")
        print("_      ")
        print()

    if chances == 0 or ganhou:
        break

if ganhou:
    print("Parabéns, você ganhou!")
    print(f'A palavra era "{palavra}"')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

else:
    print("Puxa, você foi enforcado!")
    print(f'A palavra era "{palavra}"')
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
