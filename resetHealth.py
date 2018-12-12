from pokedex import genIPokemon
from pokedex import getPokeStats
from pokemonClass import pokemon

def resetHealth(trainersPokemon):
    pokeList = trainersPokemon.listOfPokemon
    storage = []
    for pokemon in pokeList:
        poke = getPokeStats(pokemon.name)
        storage.append(poke)
    trainersPokemon.addPokemon(storage)

