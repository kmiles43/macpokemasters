from pokedex import getPokeStats
from pokedex import genIPokemon
from bestMove import bestMove
from pokedex import pokeNames
from Moves import moveNames


def D():

    response2 = input("What is the pokemon that you have an inquiry about?")
    respone3 = input("What pokemon are you facing?")
    responseLevel = int(input("Wbat level is your pokemon?"))
    responseMoves = []
    num = int(input("How many damage moves does this pokemon have?"))
    for j in range(0,num):
        newMove = input("What is the move?")
        responseMoves.append(newMove)

    responseArray = []
    for move in responseMoves:
        responseArray.append(move)
    if response2 in pokeNames:
        responsePoke = getPokeStats(response2)
        responsePoke.addLevel(responseLevel)
        responsePoke.addMoves(responseArray)
        if respone3 in pokeNames:
            responsePoke2 = getPokeStats(respone3)
            bestie = bestMove(responsePoke, responsePoke2)
            print("You should use", bestie["name"])
        else:
            print("ERROR 31")
            print("Try again")
            D()
    else:
        print("ERROR 35")