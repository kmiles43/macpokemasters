from damageCalculator import *
from pokedex import genIPokemon
from bestMove import bestMove
from pokemonClass import pokemon
import math
from beatGym import geodudeB


# def generateStats(Pokemon):
#     ChosenPokemon=[]
#     for pokemon in Pokedex:
#         if Pokemon == pokemon[0]:
#             attack=pokemon[20]
#             defense=pokemon[23]
#             hp=pokemon[24]
#             spAttack=pokemon[26]
#             spDefense=pokemon[27]
#             speed=pokemon[28]
#             typeList=pokemon[29]
#             ChosenPokemon=[attack,defense,hp,spAttack,spDefense,speed,typeList]
#     if len(ChosenPokemon)==0:
#         raise ValueError('This pokemon does not exist in gen1')
#     return ChosenPokemon

# def headTohead(Pokemon1,Pokemon2,move1,move2):
#     PokemonA=generateStats(Pokemon1)
#     PokemonB=generateStats(Pokemon2)
#     attackQueue=Queue()
#     hp1=PokemonA[2]
#     hp2=PokemonB[2]
#     pokeADamage=damageCalulator(PokemonA,PokemonB,move1)
#     pokeBDamage=damageCalulator(PokemonB,PokemonA,move2)
#     PokeATurnsAlive=math.ceil(hp1/pokeBDamage)
#     PokeBTurnsAlive=math.ceil(hp2/pokeADamage)
#     if PokeATurnsAlive>PokeBTurnsAlive:
#         return Pokemon1
#     elif PokeBTurnsAlive>PokeATurnsAlive:
#         return Pokemon2
#     else:
#         if PokemonA[5]>PokemonB[5]:
#             return Pokemon1
#         else:
#             return Pokemon2
# #test
# # print(headTohead("Bulbasaur","Squirtle", "swift","swift"))

def oneVone(pokemon1,pokemon2):

    helper1= False
    helper2 = False
    nameCatcher = pokemon1.getName()
    nameCatcher2 = pokemon2.getName()
    poke1 = geodudeB
    poke2 = geodudeB

    for p in genIPokemon:
        numbre = p.getName()
        if numbre == nameCatcher:
            poke1 = p
            helper1 = True

        elif numbre == nameCatcher2:
            poke2 = p
            helper2 = True




        if helper1 == True and helper2 == True:
            break

    move1 = bestMove(poke1, poke2)
    move2 = bestMove(poke2, poke1)

    hp1 = poke1.getHp()
    hp2 = poke2.getHp()
    poke1Damage = damageCalulator(poke1,poke2,move1["name"])
    poke2Damage = damageCalulator(poke2,poke1,move2["name"])
    poke1TurnsAlive = math.ceil(hp1/poke2Damage)
    poke2TurnsAlive = math.ceil(hp2/poke1Damage)


    if poke1TurnsAlive > poke2TurnsAlive:
        return poke1
    elif poke2TurnsAlive > poke1TurnsAlive:
        return poke2
    else:
        if poke1.getLevel() > poke2.getLevel():
            return poke1
        else:
            return poke2


def hpLeft(pokemon1,pokemon2):
    poke1 = geodudeB
    poke2 = geodudeB
    helper1 = False
    helper2 = False
    nameCatcher = pokemon1.getName()
    nameCatcher2 = pokemon2.getName()
    for p in genIPokemon:
        numbre = p.getName()
        if numbre == nameCatcher:
            poke1 = p
            helper1 = True

        elif numbre == nameCatcher2:
            poke2 = p
            helper2 = True

        if helper1 == True & helper2 == True:
            break
    move1 = bestMove(poke1, poke2)
    move2 = bestMove(poke2, poke1)

    hp1 = poke1.getHp()
    hp2 = poke2.getHp()
    poke1Damage = damageCalulator(poke1, poke2, move1["name"])
    poke2Damage = damageCalulator(poke2, poke1, move2["name"])
    poke1TurnsAlive = math.ceil(hp1 / poke2Damage)
    poke2TurnsAlive = math.ceil(hp2 / poke1Damage)
    hp1Left = hp1 - poke1TurnsAlive * poke2Damage
    hp2Left = hp2 - poke2TurnsAlive * poke1Damage

    if poke1TurnsAlive > poke2TurnsAlive:
        return hp1Left
    elif poke2TurnsAlive > poke1TurnsAlive:
        return hp2Left
    else:
        if poke1.getLevel() > poke2.getLevel():
            return hp1Left
        else:
            return hp2Left



