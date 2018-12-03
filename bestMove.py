from pokemonClass import pokemon
from damageCalculator import *



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

