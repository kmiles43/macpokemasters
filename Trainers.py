from pokemonClass import pokemon
from pokedex import getPokeStats



class trainer:
    name = ""
    listOfPokemon = []

    def addtrainerInfo(self, pokemon):
        self.listOfPokemon = pokemon

    def __init__(self, name):
        self.name = name

    def getPokemon(self):
        return self.listOfPokemon
    def addPokemon(self,pokemon):
        trainer.listOfPokemon.append(pokemon)
#TEST
Kiante = trainer("Kiante")
bulbasaur = getPokeStats('Bulbasaur')
bulbasaurb = getPokeStats('Bulbasaur')
bulbasaur.addMoves(["absorb","cut"])
bulbasaurb.addMoves(["absorb","cut"])
bulbasaur.addLevel(12)
bulbasaurb.addLevel(17)
Kiante.addtrainerInfo([bulbasaurb, bulbasaur])

Josh = trainer("Josh")
s = getPokeStats("Squirtle")
ss = getPokeStats("Wartortle")
s.addMoves(["bubble","bubble beam"])
ss.addMoves(["bubble","bubble"])
s.addLevel(1)
ss.addLevel(2)
Josh.addtrainerInfo([s, ss])
# Brock's Pokemon

geodudeB = getPokeStats("Geodude")
geodudeB.addLevel(12)
geodudeB.addMoves(["tackle"])

onixB = getPokeStats("Onix")
onixB.addMoves(["tackle"])
onixB.addLevel(14)

Brock = trainer("Brock")
Brock.addtrainerInfo([geodudeB, onixB])

# Misty

staryuM = pokemon("Staryu")
staryuM.addPokeInfo("water",43,45,55,70,55,85,18,["tackle","water gun"])

starmieM = pokemon("Starmie")
starmieM.addPokeInfo("water",83,75,85,100,85,115,21,["water gun","bubble beam"])

Misty = trainer("Misty")
Misty.addtrainerInfo([staryuM,starmieM])

# Lt Surge

voltorbS = pokemon("Voltorb")
voltorbS.addPokeInfo("electric",58,30,50,55,55,100,21,["tackle","sonicBoom"])

pikachuS = pokemon('Pikachu')
pikachuS.addPokeInfo("electric",48,55,40,50,50,90,18,["thunderShock","quick attack"])

raichuS = pokemon("Raichu")
raichuS.addPokeInfo("electric",88,90,55,90,80,110,24,["thunderbolt","thunderShock"])

Surge = trainer("Lt Surge")
Surge.addtrainerInfo([voltorbS,pikachuS,raichuS])

# Erika

victreebel = pokemon("Victreebel")
victreebel.addPokeInfo("grass poison",126,105,65,100,70,70,29,["razor leaf","wrap"])

tangela = pokemon("Tangela")
tangela.addPokeInfo("grass",95,55,115,100,40,60,24,["bind","constrict"])

vileplume = pokemon("Vileplume")
vileplume.addPokeInfo("grass poison",119,80,85,110,90,50,29,["petal dance","mega drain","poison powder"])

Erika = trainer("Erika")
Erika.addtrainerInfo([victreebel,tangela,vileplume])

# Koga

koffing = pokemon("Koffing")
koffing.addPokeInfo("poison",73,65,95,60,45,35,37,["tackle","smog","sludge"])

muk = pokemon('Muk')
muk.addPokeInfo("poison",177,105,75,65,100,50,39,["poison gas","sludge"])

Koga = trainer("Koga")
Koga.addtrainerInfo([koffing,muk])

# Sabrina

kadabra = pokemon("Kadabra")
kadabra.addPokeInfo("psychic",74,35,30,120,70,105,38,["psybeam","psychic"])

mrMime = pokemon("Mr. Mime")
mrMime.addPokeInfo("psychic",73,45,65,100,120,90,37,["confusion"])

venomoth = pokemon("Venomoth")
venomoth.addPokeInfo("poison bug",121,65,60,90,75,90,38,["leech life","psybeam"])

alakazam = pokemon("Alakazam")
alakazam.addPokeInfo("psychic",99,50,45,135,95,120,43,["psybeam"])

Sabrina = trainer("Sabrina")
Sabrina.addtrainerInfo([kadabra,mrMime,venomoth,alakazam])

# Blaine

growlithe = pokemon("Growlithe")
growlithe.addPokeInfo("fire",99,70,45,70,50,60,42,["ember","take down"])

ponyta = pokemon("Ponyta")
ponyta.addPokeInfo("fire",91,85,55,65,65,90,40,["stomp","fire spin"])

rapidash = pokemon("Rapidash")
rapidash.addPokeInfo("fire",115,100,70,80,80,105,42,["stomp","fire spin"])

arcanine = pokemon("Arcanine")
arcanine.addPokeInfo("fire",154,110,80,100,80,95,47,["ember","fire blast","take down"])

Blaine = trainer("Blaine")
Blaine.addtrainerInfo([growlithe,ponyta,rapidash,arcanine])

# Giovanni

rhyhorn = pokemon("Rhyhorn")
rhyhorn.addPokeInfo("ground rock",138,85,95,30,30,25,45,["stomp,""fury attack","horn drill"])

rhydon = pokemon("Rhydon")
rhydon.addPokeInfo("ground rock",178,130,120,45,45,40,50,["stomp","horn drill","fissure"])

nidoking = pokemon("Nidoking")
nidoking.addPokeInfo("poison ground",140,102,77,85,75,85,45,["tackle","horn attack","poison sting","thrash"])

dugtrio = pokemon("Dugtrio")
dugtrio.addPokeInfo("ground",67,100,50,50,70,120,42,["dig","slash"])

nidoqueen = pokemon("Nidoqueen")
nidoqueen.addPokeInfo("poison ground",154,92,87,75,85,76,44,["scratch","body slam","poison sting"])

Giovanni = trainer("Giovanni")
Giovanni.addtrainerInfo([rhydon,rhydon,nidoking,nidoqueen,dugtrio])

#Lorelei
dewgong = getPokeStats('Dewgong')
dewgong.addMoves(["aurora beam","take down"])

cloyster = getPokeStats("Cloyster")
cloyster.addMoves(["clamp","aurora beam"])

slowbro = getPokeStats("Slowbro")
slowbro.addMoves(["water gun"])

jynx = getPokeStats("Jynx")
jynx.addMoves(["double slap","ice punch","body slam","thrash"])

lapras = getPokeStats("Lapras")
lapras.addMoves(["body slam","hydro pump","blizard"])

Lorelei = trainer("Lorelei")
Lorelei.addtrainerInfo([dewgong,cloyster,slowbro,jynx,lapras])


# Bruno

onixBruno = getPokeStats("Onix")
onixBruno.addMoves(["rock throw","rage","slam"])

hitmonchan = getPokeStats("Hitmonchan")
hitmonchan.addMoves(["ice punch","fire punch","thunderpunch","counter"])

hitmonlee = getPokeStats("Hitmonlee")
hitmonlee.addMoves(["jump kick","hi jump kick","mega kick"])

onixBruno2 = getPokeStats("Onix")
onixBruno2.addMoves(["rock throw","rage","slam"])

machamp = getPokeStats("Machamp")
machamp.addMoves(["Fissure","submission"])

Bruno = trainer("Bruno")
Bruno.addtrainerInfo([onixBruno,hitmonchan,hitmonlee,onixBruno2,machamp])

#Agatha
gengar = getPokeStats("Gengar")
gengar.addMoves("night shade")

golbat = getPokeStats("Golbat")
golbat.addMoves(["wing attack"])

haunter = getPokeStats("Haunter")
haunter.addMoves(["night shade"])

arbok = getPokeStats("Arbok")
arbok.addMoves(["bite","acid"])

gengar2 = getPokeStats("Gengar")
gengar2.addMoves(["night shade","toxic"])

Agatha = trainer("Agatha")
Agatha.addtrainerInfo([gengar,golbat,haunter,arbok,gengar2])

#Lance
gyarados = getPokeStats("Gyarados")
gyarados.addMoves(["hydro pump","hyper beam"])

drangonair = getPokeStats("Dragonair")
drangonair.addMoves(["slam","hyper beam"])

aerodactyl = getPokeStats("Aerodactyl")
aerodactyl.addMoves(["take down","bite","hyper beam"])

dragonite = getPokeStats("Dragonite")
dragonite.addMoves(["slam","hyper beam"])

Lance = trainer("Lance")
Lance.addtrainerInfo([gyarados,drangonair,drangonair,aerodactyl,dragonite])











#
# pokemontrainerName = input("What is your name?")
# trainer1 = trainer(pokemontrainerName)
# numPokemon = int(input("How many pokemon are in your party?"))
#
# for i in range(0,numPokemon):
#     pokename = input("What is the pokemon's name?")
#     pokemon1 = pokemon(pokename)
#     pokemonLevel = int(input("What is the Pokemon's level?"))
#     pokemon1.level = pokemonLevel
#     trainer1.addPokemon(pokemon1)
#     print("pokemon added")
#
#
#
#
# answer1 = input("What gym are you facing off against:")
# if answer1 == "pewter" | answer1 == "Pewter":
#     ans = input("Are you trying to beat Brock?")
#     if ans == "yes" | ans == "Yes":
#         print("Which Pokemon wins goes here.")
