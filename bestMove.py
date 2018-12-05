from pokemonClass import pokemon
from damageCalculator import *


pokemonC = pokemon("Bulbasaur")
pokemonC.addPokeInfo('grass',45,49,49,65,65,45,16,["cut","vineWhip"])

pokemonD = pokemon("Squirtle")
pokemonD.addPokeInfo('water',44,48,65,50,64,45,12,["water gun"])


def bestMove(poke1,poke2):
    damage = 0
    for move in poke1.moves :
        testing = damageCalulator(poke1,poke2,move)
        if testing > damage:
            damage = testing
            attack = move
    bestMove = {"name": attack,
                "damgae": damage}
    return bestMove
