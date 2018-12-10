import gymLeader
import damageCalculator
from bestMove import bestMove
from pokemonClass import pokemon
from headTohead import oneVone




def beatGym(Leader,Trainer):
    leaderPokemon=Leader.getPokemon()
    trainerPokemon=Trainer.getPokemon()
    while len(leaderPokemon)>0 and len(trainerPokemon)>0:
        enemy=leaderPokemon[0]
        bestOption={"name": "this is a fake",
                "damgae": -1}
        bestPokemon=""
        for pokemon in trainerPokemon:
            possibleOption=bestMove(pokemon,enemy)
            if possibleOption["damage"]> bestOption["damage"]:
                bestOption=possibleOption
                bestPokemon=pokemon
        chosenPokemon=trainerPokemon[bestPokemon]
        winner=oneVone(pokemon,enemy)
        #needs more work






