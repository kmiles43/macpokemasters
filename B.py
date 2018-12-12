from Trainers import *
from trainerFight import fight
from resetHealth import resetHealth
from pokedex import getPokeStats
from Moves import AllMoves



def B():
    # trainerName = input("What is your name?")
    # userTrainer = trainer(trainerName)
    # partySize = int(input("What is the size of your party"))
    # print("Start with the first pokemon in your party and continue through your last for the following")
    userTrainer = trainer("Wolf")
    partySize = 3
    for x in range(0, partySize ):
        # partyPokeName = input("What is the pokemon's name?")
        partyPokeName = "Venusaur"
        partyPoke = getPokeStats(partyPokeName)
        partyPokeMovesArray = []
        # partyPokemonLevel = int(input("What is this pokemon's level?"))
        partyPokemonLevel = 100
        partyPoke.addLevel(partyPokemonLevel)
        # partyPokeMove1 = input("What's a move that this pokemon has that does damage?")
        partyPokeMove1 = "absorb"
        partyPokeMovesArray.append(partyPokeMove1)
        # areThereMore = input("Is there another? y/n?")
        areThereMore = "y"
        if areThereMore == "y" or areThereMore == "Y":
            # howMany = int(input("How many?"))
            howMany = 1
            i = 0
            while i < howMany:
                # partyPokeMoves = input("What's another move that this pokemon has that does damage?")
                partyPokeMoves = "acid"
                partyPokeMovesArray.append(partyPokeMoves)
                i = i + 1
                break

        partyPoke.addMoves(partyPokeMovesArray)
        userTrainer.addPokemon(partyPoke)

    gym1 = fight(Brock, userTrainer)
    if gym1 == userTrainer.name:
        resetHealth(userTrainer)
        gym2 = fight(Misty, userTrainer)
        if gym2 == userTrainer:
            resetHealth(userTrainer)
            gym3 = fight(Surge, userTrainer)
            if gym3 == userTrainer:
                resetHealth(userTrainer)
                gym4 = fight(Erika, userTrainer)
                if gym4 == userTrainer:
                    resetHealth(userTrainer)
                    gym5 = fight(Koga, userTrainer)
                    if gym5 == userTrainer:
                        resetHealth(userTrainer)
                        gym6 = fight(Sabrina, userTrainer)
                        if gym6 == userTrainer:
                            resetHealth(userTrainer)
                            gym7 = fight(Blaine, userTrainer)
                            if gym7 == userTrainer:
                                resetHealth(userTrainer)
                                gym8 = fight(Giovanni, userTrainer)
                                if gym8 == userTrainer:
                                    resetHealth(userTrainer)
                                    elitefour1 = fight(Lorelei, userTrainer)
                                    elitefour2 = fight(Bruno, userTrainer)
                                    elitefour3 = fight(Agatha, userTrainer)
                                    elitefour4 = fight(Lance, userTrainer)
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