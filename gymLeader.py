from pokemonClass import pokemon

class gymLeader:
    name = ""
    listOfPokemon =[]

    def addGymLeaderInfo(self,pokemon):
        self.listOfPokemon = pokemon

    def __init__(self, name):
        self.name = name

    def getPokemon(self):
        return self.listOfPokemon

class trainer:
    name = ""
    listOfPokemon = []

    def addTrainerInfo(self, pokemon):
        self.listOfPokemon = pokemon

    def __init__(self, name):
        self.name = name

    def getPokemon(self):
        return self.listOfPokemon
    def addPokemon(self,pokemon):
        trainer.listOfPokemon.append(pokemon)

# Brock's Pokemon

geodudeB = pokemon('geodude')
geodudeB.addPokeInfo("rock ground",44,80,100,30,30,20,12,["tackle","defense curl"])

onixB = pokemon("onix")
onixB.addPokeInfo("rock ground",42,45,160,30,45,70,14,["tackle","bind","rock tomb"])

Brock = gymLeader("Brock")
Brock.addGymLeaderInfo([geodudeB,onixB])

# Misty

staryuM = pokemon("staryu")
staryuM.addPokeInfo("water",43,45,55,70,55,85,18,["tackle","water gun"])

starmieM = pokemon("starmie")
starmieM.addPokeInfo("water",83,75,85,100,85,115,21,["water gun","bubble beam"])

Misty = gymLeader("Misty")
Misty.addGymLeaderInfo([staryuM,starmieM])

# Lt Surge

voltorbS = pokemon("voltorb")
voltorbS.addPokeInfo("electric",58,30,50,55,55,100,21,["tackle","sonicBoom"])

pikachuS = pokemon('pikachu')
pikachuS.addPokeInfo("electric",48,55,40,50,50,90,18,["thunderShock","quick attack"])

raichuS = pokemon("raichu")
raichuS.addPokeInfo("electric",88,90,55,90,80,110,24,["thunderbolt","thunderShock"])

Surge = gymLeader("Lt Surge")
Surge.addGymLeaderInfo([voltorbS,pikachuS,raichuS])

# Erika

victreebel = pokemon("victreebel")
victreebel.addPokeInfo("grass poison",126,105,65,100,70,70,29,["razor leaf","wrap"])

tangela = pokemon("tangela")
tangela.addPokeInfo("grass",95,55,115,100,40,60,24,["bind","constrict"])

vileplume = pokemon("vileplume")
vileplume.addPokeInfo("grass poison",119,80,85,110,90,50,29,["petal dance","mega drain","poison powder"])

Erika = gymLeader("Erika")
Erika.addGymLeaderInfo([victreebel,tangela,vileplume])

# Koga

koffing = pokemon("koffing")
koffing.addPokeInfo("poison",73,65,95,60,45,35,37,["tackle","smog","sludge"])

muk = pokemon('muk')
muk.addPokeInfo("poison",177,105,75,65,100,50,39,["poison gas","sludge"])

Koga = gymLeader("Koga")
Koga.addGymLeaderInfo([koffing,muk])

# Sabrina

kadabra = pokemon("kadabra")
kadabra.addPokeInfo("psychic",74,35,30,120,70,105,38,["psybeam","psychic"])

mrMime = pokemon("Mr. Mime")
mrMime.addPokeInfo("psychic",73,45,65,100,120,90,37,["confusion","doubleSlap"])

venomoth = pokemon("venomoth")
venomoth.addPokeInfo("poison bug",121,65,60,90,75,90,38,["poisonPowder","leech ife","psybeam"])

alakazam = pokemon("alakazam")
alakazam.addPokeInfo("psychic",99,50,45,135,95,120,43,["psybeam","psywave"])

sabrina = gymLeader("Sabrina")
sabrina.addGymLeaderInfo([kadabra,mrMime,venomoth,alakazam])

# Blaine

growlithe = pokemon("growlithe")
growlithe.addPokeInfo("fire",99,70,45,70,50,60,42,["ember","take down"])

ponyta = pokemon("ponyta")
ponyta.addPokeInfo("fire",91,85,55,65,65,90,40,["stomp","fire spin"])

rapidash = pokemon("rapidash")
rapidash.addPokeInfo("fire",115,100,70,80,80,105,42,["stomp","fire spin"])

arcanine = pokemon("arcanine")
arcanine.addPokeInfo("fire",154,110,80,100,80,95,47,["ember","fire blast","take down"])

Blaine = gymLeader("Blaine")
Blaine.addGymLeaderInfo([growlithe,ponyta,rapidash,arcanine])

# Giovanni

rhyhorn = pokemon("rhyhorn")
rhyhorn.addPokeInfo("ground rock",138,85,95,30,30,25,45,["stomp,""fury attack","horn drill"])

rhydon = pokemon("rhydon")
rhydon.addPokeInfo("ground rock",178,130,120,45,45,40,50,["stomp","horn drill","fissure"])

nidoking = pokemon("nidoking")
nidoking.addPokeInfo("poison ground",140,102,77,85,75,85,45,["tackle","horn attack","poison sting","thrash"])

dugtrio = pokemon("dugtrio")
dugtrio.addPokeInfo("ground",67,100,50,50,70,120,42,["dig","slash"])

nidoqueen = pokemon("nidoqueen")
nidoqueen.addPokeInfo("poison ground",154,92,87,75,85,76,44,["scratch","body slam","poison sting"])

Giovanni = gymLeader("Giovanni")
Giovanni.addGymLeaderInfo([rhydon,rhydon,nidoking,nidoqueen,dugtrio])

pokemonTrainerName = input("What is your name?")
trainer1 = trainer(pokemonTrainerName)
numPokemon = int(input("How many pokemon are in your party?"))
#
# for i in range(0,numPokemon):
#     pokename = input("What is the pokemon's name?")
#     pokemon1 = pokemon(pokename)
#     pokemonLevel = int(input("What is the Pokemon's level?"))
#     pokemon1.level = pokemonLevel
#     trainer1.addPokemon(pokemon1)
#     print("pokemon added")



#
# answer1 = input("What gym are you facing off against:")
# if answer1 == "pewter" | answer1 == "Pewter":
#     ans = input("Are you trying to beat Brock?")
#     if ans == "yes" | ans == "Yes":
#         print("Which Pokemon wins goes here.")
