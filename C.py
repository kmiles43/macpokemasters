from pokedex import genIPokemon
from pokedex import getPokeStats
from OnevOne import oneVone
from pokedex import pokeNames
from Moves import moveNames

def C():
    poke1 = input("Input first Pokemon.")
    # poke1 = "Squirtle"
    if poke1 in pokeNames:

        numMoves = int(input("How many damage moves does this pokemon have?"))
        moveArray = []
        count = 0
        while count < numMoves:
            pokeMove1 = input("What is the move?")
            if pokeMove1 in moveNames:
                moveArray.append(pokeMove1)
            else:
                print("that move isn't in Gen I")
            count = count + 1
        level1 = int(input("What is the pokemon's level?"))
        pokepoke = getPokeStats(poke1)
        pokepoke.addMoves(moveArray)
        pokepoke.addLevel(level1)
    else:
        print("Sorry that pokemon isn't in Gen I")
    poke2 = input("Input Second Pokemon.")
    if poke2 in pokeNames:

        numMoves2 = int(input("How many damage moves does this pokemon have?"))
        moveArray2 = []
        count2 = 0
        while count2 < numMoves2:
            pokeMove2 = input("What is the move?")
            if pokeMove2 in moveNames:
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
    winningPokemon = oneVone(pokepoke, pokepoke2)
    print(winningPokemon.name, "will win this fight.")