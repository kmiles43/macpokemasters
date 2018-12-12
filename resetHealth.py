from pokedex import genIPokemon
from pokedex import getPokeStats

def resetHealth(trainersPokemon):
    list = trainersPokemon.getPokemon()
    holder = []
    for pokemon in list:
        name =pokemon.getName()
        poke = getPokeStats(name)
        holder.append(poke)
    trainersPokemon.addPokemon(holder)


