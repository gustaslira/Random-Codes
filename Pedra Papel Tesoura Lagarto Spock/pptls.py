def bazinga():
    print('Bazinga!')

def trap():
    print('Raj trapaceou!')

def again():
    print('De novo!')

choice = input().upper().strip()
split = choice.split()

try:
    if split[0] == 'PEDRA':
        if split[1] == 'PEDRA':
            again()
        if split[1] == 'PAPEL':
            trap()
        if split[1] == 'TESOURA':
            bazinga()
        if split[1] == 'LAGARTO':
            bazinga()
        if split[1] == 'SPOCK':
            trap()

    if split[0] == 'PAPEL':
        if split[1] == 'PEDRA':
            bazinga()
        if split[1] == 'PAPEL':
            again()
        if split[1] == 'TESOURA':
            trap()
        if split[1] == 'LAGARTO':
            trap()
        if split[1] == 'SPOCK':
            bazinga()

    if split[0] == 'TESOURA':
        if split[1] == 'PEDRA':
            trap()
        if split[1] == 'PAPEL':
            bazinga()
        if split[1] == 'TESOURA':
            again()
        if split[1] == 'LAGARTO':
            bazinga()
        if split[1] == 'SPOCK':
            trap()

    if split[0] == 'LAGARTO':
        if split[1] == 'PEDRA':
            trap()
        if split[1] == 'PAPEL':
            bazinga()
        if split[1] == 'TESOURA':
            trap()
        if split[1] == 'LAGARTO':
            again()
        if split[1] == 'SPOCK':
            bazinga()

    if split[0] == 'SPOCK':
        if split[1] == 'PEDRA':
            bazinga()
        if split[1] == 'PAPEL':
            trap()
        if split[1] == 'TESOURA':
            bazinga()
        if split[1] == 'LAGARTO':
            trap()
        if split[1] == 'SPOCK':
            again()
except:
    print('Erro')