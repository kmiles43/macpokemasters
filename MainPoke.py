from trainerFight import fight
from Trainers import *
from pokemonCaptureAlgorithm import *
from pokedex import genIPokemon
from pokedex import getPokeStats
from Moves import AllMoves

def mainPoke():
    ans1 = input("What would you like to do:"
                 "A.Find out if you could catch a pokemon"
                 "B.See how many badges you could obtain with your current party"
                 "C.Simulate a one vs one battle"
                 "D. What Move should you use")
    if ans1 == "A" or ans1 == "a":
        health = int(input("What is the full health of the pokemon?"))
        pokeCaptureGenI(health)
    elif ans1 == "B" or ans1 == "b":
        trainerName = input("What is your name?")
        userTrainer = trainer(trainerName)
        partySixe = int(input("What is the size of your party"))
        print("Start with the first pokemon in your party and continue through your last for the following")
        for x in range(0,partySixe):
            partyPokeName = input("What is the pokemon's name?")
            if partyPokeName in genIPokemon:
                partyPoke = getPokeStats(partyPokeName)
                partyPokeMovesArray = []
                partyPokemonLevel = int(input("What is this pokemon's level?"))
                partyPoke.addLevel(partyPokemonLevel)
                partyPokeMove1 = input("What's a move that this pokemon has that does damage?")
                if partyPokeMove1 in AllMoves:
                    partyPokeMovesArray.append(partyPokeMove1)
                    areThereMore = input("Is there another? y/n?")
                    if areThereMore == "y" or areThereMore == "Y":
                        howMany = int(input("How many?"))
                        i = 0
                        while i < howMany:
                         partyPokeMoves = input("What's another move that this pokemon has that does damage?")
                         if partyPokeMoves in AllMoves:
                             partyPokeMovesArray.append(partyPokeMoves)
                         else:
                             print("You've entered a wrong Move")
                         i = i +1
                partyPoke.addMoves(partyPokeMovesArray)
                userTrainer.addPokemon(partyPoke)
            else:
                print("The pokemon you've entered isn't in Gen I.")
        gym1 = fight(Brock,userTrainer)
        if gym1 == userTrainer:
            gym2 = fight(Misty,userTrainer)
            if gym2 == userTrainer:
                gym3 = fight(Surge,userTrainer)
                if gym3 == userTrainer:
                    gym4 = fight(Erika,userTrainer)
                    if gym4 == userTrainer:
                        gym5 = fight(Koga,userTrainer)
                        if gym5 == userTrainer:
                            gym6 = fight(Sabrina,userTrainer)
                            if gym6 == userTrainer:
                                gym7 = fight(Blaine,userTrainer)
                                if gym7 == userTrainer:
                                    gym8 = fight(Giovanni,userTrainer)
                                    if gym8 == userTrainer:
                                        elitefour1 = fight(Lorelei,userTrainer)
                                        elitefour2 = fight(Bruno,userTrainer)
                                        elitefour3 = fight(Agatha,userTrainer)
                                        elitefour4 = fight(Lance,userTrainer)
                                        if elitefour1 and elitefour2 and elitefour3 and elitefour4 == userTrainer:
                                            print("Congrats you're a pokemon Master and can beat anyone!")
                                        else:
                                            print("You can obtain all 8 gym badges!")
                                    else:
                                        print("You can beat the first 7 gyms!")
                                else:
                                    print("You can beat the first 6 gyms!")
                            else:
                                print("You can beat the first 5 gyms!")
                        else:
                            print("You can beat the first 4 gyms!")
                    else:
                        print("You can beat the first 3 gyms!")
                else:
                    print("You can beat the first 2 gyms!")
            else:
                print("You can beat the first gym!")
        else:
            print("You're not ready for a gym yet. Keep working hard Trainer!!")

