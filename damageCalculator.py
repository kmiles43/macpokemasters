import random
from pokemonClass import pokemon
from Moves import *
from Effectiveness import *

pokemonC = pokemon('Bulbasaur')
pokemonC.addPokeInfo('grass',45,49,49,65,65,45,16,["cut","vineWhip"])

pokemonD = pokemon('Squirtle')
pokemonD.addPokeInfo('water',44,48,65,50,64,45,12,["water gun"])






def damageCalulator( pokemonA, pokemonB,move):

    for movem in moves:
        if move == movem["name"]:
            chosenMove = movem
            moveType = chosenMove["type"]
            power = chosenMove["power"]
            movChar = chosenMove["category"]
            break


    # moveType = input("What is the type of the move:")
    # power = int(input("what is the power of the move: "))
    # movChar = input("is the move physical or special:")
    # for testing
    # moveType = "grass"
    # power = 45
    # movChar = "physical"
    target = 1

# Weather factor
#     weather = input("Is the weather rainy, harsh sunlight, or normal: ")
    weatherbooster = 0
    weather = "normal"
    if weather =="rainy":
        if pokemonA.getType == "water":
            weatherbooster = 1.5
        elif pokemonA.getType == "fire":
            weatherbooster = .5
        else:
            weatherbooster = 1
    elif weather == "harsh sunlight":
        if pokemonA.getType == "fire":
            weatherbooster = 1.5
        else:
            weatherbooster = 1
    else:
        weatherbooster = 1
    if pokemonA.getType == moveType :
        stab = 1.5
    else:
        stab = 1

    typeA = moveType
    typeB = pokemonB.getType()

    effectiveVariable = 0

    if typeA == "normal":
        if typeB in normalTypeNotEffective:
            effectiveVariable = .5
        elif typeB in normalTypeNoEffect:
            effectiveVariable = 0

        else:
            effectiveVariable = 1
    elif typeA =="fight":
        if typeB in fightTypeNoEffect:
            effectiveVariable = 0
        elif typeB in fightTypeSuperEffective:
            effectiveVariable = 2
        elif typeB in fightTypeNotEffective:
            effectiveVariable = .5
        else:
            effectiveVariable = 1
    elif typeA =="flying":
        if typeB in flyingTypeNotEffective:
            effectiveVariable = .5
        elif typeB in flyingTypeSuperEffective:
            effectiveVariable = 2
        else:
            effectiveVariable = 1
    elif typeA == "poison":
        if typeB in poisonTypeNotEffective:
            effectiveVariable = .5
        elif typeB in poisonTypeSuperEffective:
            effectiveVariable = 2
        else:
            effectiveVariable = 1
    elif typeA == "ground":
        if typeB in groundTypeSuperEffective:
            effectiveVariable = 2
        elif typeB in groundTypeNotEffective:
            effectiveVariable = .5
        elif typeB in groundTypeNoEffect:
            effectiveVariable =0
        else:
            effectiveVariable = 1
    elif typeA == "rock":
        if typeB in rockTypeNotEffective:
            effectiveVariable = .5
        elif typeB in rockTypeSuperEffective:
            effectiveVariable = 2
        else:
            effectiveVariable = 1
    elif typeA == "bug":
        if typeB in bugTypeNotEffective:
            effectiveVariable = .5
        elif typeB in bugTypeSuperEffective:
            effectiveVariable =2
        else:
            effectiveVariable = 1
    elif typeA =="ghost":
        if typeB in ghostTypeNoEffect:
            effectiveVariable = 0
        elif typeB in ghostTypeSuper:
            effectiveVariable = 2
        else:
            effectiveVariable = 1
    elif typeA == "fire":
        if typeB in fireTypeSuper:
            effectiveVariable = 2
        elif typeB in fireTypeNotEffective:
            effectiveVariable = .5
        else:
            effectiveVariable = 1
    elif typeA == "water":
        if typeB in waterTypeSuper:
            effectiveVariable = 2
        elif typeB in waterTypeNot:
            effectiveVariable = .5
        else:
            effectiveVariable = 1
    elif typeA == "grass":
        if typeB in grassTypeSuper:
            effectiveVariable = 2
        elif typeB in grassTypeNotEffective:
            effectiveVariable = .5
        else:
            effectiveVariable = 1
    elif typeA == "electric":
        if typeB in electricNoEffect:
            effectiveVariable =0
        elif typeB in electricTypeNotEffective:
            effectiveVariable =.5
        elif typeB in electricTypeSuper:
            effectiveVariable = 2
        else:
            effectiveVariable = 1
    elif typeA =="psychic":
        if typeB in psychicTypeNotEffective:
            effectiveVariable =.5
        elif typeB in psychicTypeSuper:
            effectiveVariable = 2
        else:
            effectiveVariable = 1
    elif typeA == "ice":
        if typeB in iceTypeNotEffective:
            effectiveVariable = .5
        elif typeB in iceTypeSuper:
            effectiveVariable = 2
        else:
            effectiveVariable = 1
    elif typeA == "dragon":
        if typeB in dragonTypeSuper:
            effectiveVariable = 2
        else:
            effectiveVariable = 1
    else:
        print("You imputed an invalid type")




    attackA = pokemonA.getAttack()
    defenseB = pokemonB.getDefense()
    specialAttackA = pokemonA.getSPA()
    specialDefenseB = pokemonB.getSPDEF()
    level = pokemonA.getLevel()
    if movChar == "special":
        attackingPower = specialAttackA
        defensePower = specialDefenseB
    else:
        attackingPower = attackA
        defensePower = defenseB

    one =(2*level)
    two = one/5
    three = two + 2
    four = three * power
    five = attackingPower/defensePower
    six = four * five
    seven = six /50
    eight = seven+2
    modifier = weatherbooster * stab * effectiveVariable
    totalDamage = eight * modifier

    return totalDamage





