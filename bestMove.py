from pokemonClass import pokemon
from damageCalculator import *



def bestMove(mon1,mon2):
    damage = 0
    for move in mon1.moves :
        testing = damageCalulator(mon1,mon2,move)
        if testing > damage:
            damage = testing
            attack = move
    bestMove = {"name": attack,
                "damage": damage}
    return bestMove

