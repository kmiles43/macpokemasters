from pokedex import genIPokemon
from pokedex import getPokeStats
from OnevOne import oneVone

def C():
    poke1 = input("Input first Pokemon.")
    if poke1 in genIPokemon:

        numMoves = int(input("How many damage moves does this pokemon have?"))
        moveArray = []
        count = 0
        while count < numMoves:
            pokeMove1 = input("What is the move?")
            if pokeMove1 in genIPokemon:
                moveArray.append(pokeMove1)
            else:
                print("that move isn't in Gen I")
            count = count + 1
        level1 = int(input("What is the pokemon's level?"))
        pokepoke = getPokeStats(poke1)
        pokepoke.addMoves(moveArray)
        pokepoke.addLevel(level1)
    else:
        print("Sorry that move isn't in Gen I")
    poke2 = input("Input Second Pokemon.")
    if poke2 in genIPokemon:

        numMoves2 = int(input("How many damage moves does this pokemon have?"))
        moveArray2 = []
        count2 = 0
        while count2 < numMoves2:
            pokeMove2 = input("What is the move?")
            if pokeMove2 in genIPokemon:
                moveArray2.append(pokeMove2)
            else:
                print("that move isn't in Gen I")
            count2 = count2 + 1
        level2 = int(input("What is the pokemon's level?"))
        pokepoke2 = getPokeStats(poke2)
        pokepoke2.addMoves(moveArray2)
        pokepoke2.addLevel(level2)
    else:
        print("Sorry that move isn't in Gen I")
    print(oneVone(pokepoke, pokepoke2), "Will win the battle")