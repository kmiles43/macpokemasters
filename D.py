from pokedex import getPokeStats
from pokedex import genIPokemon
from bestMove import bestMove


def D():

    response2 = input("What is the pokemon that you have an inquiry about?")
    respone3 = input("What pokemon are you facing?")
    responseLevel = int(input("Wbat level is your pokemon?"))
    responeMoves = input("What are your pokemon's damage moves?")
    responseArray = []
    for move in responeMoves:
        responseArray.append(move)
    if response2 in genIPokemon:
        responsePoke = getPokeStats(response2)
        responsePoke.addLevel(responseLevel)
        responsePoke.addMoves(responseArray)
        if respone3 in genIPokemon:
            responsePoke2 = getPokeStats(respone3)
            print(bestMove(responsePoke, responsePoke2))
        else:
            print("ERROR 23")
    else:
        print("ERROR 25")