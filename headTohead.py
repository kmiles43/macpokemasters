from damageCalculator import *
from pokedex import *
from bestMove import *
from pokemonClass import pokemon
import math

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
    test1Level = 12
    test2Level = 14
    test1Moves = ["absorb","cut"]
    test2Moves = ["bubble","bubble beam"]
    helper1= False
    helper2 = False
    for p in genIPokemon:
        numbre = p.getName()
        if numbre == pokemon1:
            poke1 = p
            helper1 = True
            poke1.addMoves(test1Moves)
            poke1.addLevel(test1Level)
        elif numbre == pokemon2:
            poke2 = p
            helper2 = True
            poke2.addMoves(test2Moves)
            poke2.addLevel(test2Level)
        if helper1 == True & helper2 == True:
            break
    move1 = bestMove(poke1,poke2)
    move2 = bestMove(poke2,poke1)

    hp1 = poke1.getHp()
    hp2 = poke2.getHp()
    poke1Damage = damageCalulator(poke1,poke2,move1)
    poke2Damage = damageCalulator(poke2,poke1,move2)
    poke1TurnsAlive = math.ceil(hp1/poke2Damage)
    poke2TurnsAlive = math.ceil(hp2/poke1Damage)
    if poke1TurnsAlive > poke2TurnsAlive:
        return poke1.getName()
    elif poke2TurnsAlive > poke1TurnsAlive:
        return poke2.getName()
    else:
        if poke1.getLevel() > poke2.getLevel():
            return poke1.getName()
        else:
            return poke2.getName()
print(oneVone(pokemonC.getName(),pokemonD.getName()))






