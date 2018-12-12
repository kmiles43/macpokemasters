from pokedex import genIPokemon
from bestMove import bestMove
import math
from Trainers import geodudeB


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
    # poke1Damage = damageCalulator(poke1,poke2,move1["name"])
    # poke2Damage = damageCalulator(poke2,poke1,move2["name"])
    poke1Damage = move1["damage"]
    poke2Damage = move2["damage"]
    poke1TurnsAlive = math.ceil(hp1/poke2Damage)
    poke2TurnsAlive = math.ceil(hp2/poke1Damage)

    if poke1TurnsAlive > poke2TurnsAlive:
        if poke1.speed > poke2.speed:
         hp1Left = hp1 - (poke2TurnsAlive-1)*poke2Damage
         poke1.hp = hp1Left
        else:
            hp1Left = hp1 - (poke2TurnsAlive)*poke2Damage
            poke1.hp = hp1Left
    elif poke2TurnsAlive > poke1TurnsAlive:
        if poke2.speed > poke1.speed:
            hp2Left = hp2 - (poke1TurnsAlive-1) * poke1Damage
            poke2.hp = hp2Left
        else:
            hp2Left = hp2 - poke1TurnsAlive*poke1Damage
            poke2.hp = hp2Left
    else:
        hp3Left = 0
        poke2.hp = hp3Left
        poke1.hp = hp3Left


    if poke1TurnsAlive > poke2TurnsAlive:
        return poke1
    elif poke2TurnsAlive > poke1TurnsAlive:
        return poke2
    else:
        if poke1.getLevel() > poke2.getLevel():
            return poke1
        else:
            return poke2


# def hpLeft(pokemon1,pokemon2):
#     poke1 = geodudeB
#     poke2 = geodudeB
#     helper1 = False
#     helper2 = False
#     nameCatcher = pokemon1.getName()
#     nameCatcher2 = pokemon2.getName()
#     for p in genIPokemon:
#         numbre = p.getName()
#         if numbre == nameCatcher:
#             poke1 = p
#             helper1 = True
#
#         elif numbre == nameCatcher2:
#             poke2 = p
#             helper2 = True
#
#         if helper1 == True & helper2 == True:
#             break
#     move1 = bestMove(poke1, poke2)
#     move2 = bestMove(poke2, poke1)
#
#     hp1 = poke1.getHp()
#     hp2 = poke2.getHp()
#     # poke1Damage = damageCalulator(poke1, poke2, move1["name"])
#     # poke2Damage = damageCalulator(poke2, poke1, move2["name"])
#     poke1Damage = move1["damage"]
#     poke2Damage = move2["damage"]
#
#     poke1TurnsAlive = math.ceil(hp1 / poke2Damage)
#     poke2TurnsAlive = math.ceil(hp2 / poke1Damage)
#
#
#
#
#
