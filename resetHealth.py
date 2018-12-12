from pokedex import genIPokemon
from pokedex import getPokeStats
from pokemonClass import pokemon
from Trainers import Josh


def resetHealth(trainersPokemon):
    pokeList = trainersPokemon.listOfPokemon
    storage = []
    for pokee in pokeList:
        p=pokee.getName()
        poke = getPokeStats(p)
        storage.append(poke)
    trainersPokemon.newPokemon(storage)

