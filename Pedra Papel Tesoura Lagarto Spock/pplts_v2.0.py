sheldon, raj = input().split()

pedra, papel, tesoura, lagarto, Spock = 'pedra','papel','tesoura','lagarto','Spock'

if sheldon == raj:
    print('De novo!')

elif (
    (sheldon == pedra and (raj == lagarto or raj == tesoura)) or
    (sheldon == papel and (raj == pedra or raj == Spock)) or
    (sheldon == tesoura and (raj == papel or raj == lagarto)) or
    (sheldon == lagarto and (raj == Spock or raj == papel)) or
    (sheldon == Spock and (raj == tesoura or raj == pedra))
    ):
    print('Bazinga!')

else:
    print('Raj trapaceou!')