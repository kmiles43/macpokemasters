from damageCalculator import *
from pokedex import *

def generateStats(Pokemon):
    ChosenPokemon=[]
    for pokemon in Pokedex:
        if Pokemon == pokemon[0]:
            attack=pokemon[20]
            defense=pokemon[23]
            hp=pokemon[24]
            spAttack=pokemon[26]
            spDefense=pokemon[27]
            speed=pokemon[28]
            typeList=pokemon[29]
            ChosenPokemon=[attack,defense,hp,spAttack,spDefense,speed,typeList]
    if len(ChosenPokemon)==0:
        raise ValueError('This pokemon does not exist in gen1')
    return ChosenPokemon

def headTohead(Pokemon1,Pokemon2,move1,move2):
    PokemonA=generateStats(Pokemon1)
    PokemonB=generateStats(Pokemon2)
    attackQueue=Queue()
    hp1=PokemonA[2]
    hp2=PokemonB[2]
    if PokemonA[5]>PokemonB[5]:
        attackQueue.enqueue(PokemonA)
        attackQueue.enqueue(PokemonB)
    else:
        attackQueue.enqueue(PokemonB)
        attackQueue.enqueue(PokemonA)
    damageCalulator(PokemonA,PokemonB,move1)

headTohead("Bulbasaur","Squirtle", "swift",0)



