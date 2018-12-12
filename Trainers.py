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

geodudeB = getPokeStats("Bulbasaur")
geodudeB.addLevel(12)
geodudeB.addMoves(["absorb"])

onixB = getPokeStats("Bulbasaur")
onixB.addMoves(["absorb"])
onixB.addLevel(14)

Brock = trainer("Brock")
Brock.addtrainerInfo([geodudeB, onixB])

# Misty

staryuM = getPokeStats("Staryu")
staryuM.addLevel(18)
staryuM.addMoves(["tackle","water gun"])

starmieM = getPokeStats("Starmie")
starmieM.addLevel(21)
starmieM.addMoves(["water gun","bubble beam"])

Misty = trainer("Misty")
Misty.addtrainerInfo([staryuM,starmieM])

# Lt Surge

voltorbS = getPokeStats("Voltorb")
voltorbS.addLevel(21)
voltorbS.addMoves(["tackle","sonicBoom"])

pikachuS = getPokeStats('Pikachu')
pikachuS.addLevel(18)
pikachuS.addMoves(["thunderShock","quick attack"])

raichuS = getPokeStats("Raichu")
raichuS.addMoves(["thunderbolt","thunderShock"])
raichuS.addLevel(24)

Surge = trainer("Lt Surge")
Surge.addtrainerInfo([voltorbS,pikachuS,raichuS])

# Erika

victreebel = getPokeStats("Victreebel")
victreebel.addMoves(["razor leaf","wrap"])
victreebel.addLevel(29)

tangela = getPokeStats("Tangela")
tangela.addLevel(24)
tangela.addMoves(["bind","constrict"])

vileplume = getPokeStats("Vileplume")
vileplume.addMoves(["petal dance","mega drain","poison powder"])
vileplume.addLevel(29)

Erika = trainer("Erika")
Erika.addtrainerInfo([victreebel,tangela,vileplume])

# Koga

koffing = getPokeStats("Koffing")
koffing.addLevel(37)
koffing.addMoves(["tackle","smog","sludge"])

muk = getPokeStats('Muk')
muk.addMoves(["poison gas","sludge"])
muk.addLevel(39)


Koga = trainer("Koga")
Koga.addtrainerInfo([koffing,muk])

# Sabrina

kadabra = getPokeStats("Kadabra")
kadabra.addLevel(38)
kadabra.addMoves(["psybeam","psychic"])

mrMime = getPokeStats("Mr. Mime")
mrMime.addLevel(37)
mrMime.addMoves(["confusion"])

venomoth = getPokeStats("Venomoth")
venomoth.addLevel(38)
venomoth.addMoves(["leech life","psybeam"])

alakazam = getPokeStats("Alakazam")
alakazam.addLevel(43)
alakazam.addMoves(["psybeam"])

Sabrina = trainer("Sabrina")
Sabrina.addtrainerInfo([kadabra,mrMime,venomoth,alakazam])

# Blaine

growlithe = getPokeStats("Growlithe")
growlithe.addLevel(43)
growlithe.addMoves(["ember","take down"])

ponyta = getPokeStats("Ponyta")
ponyta.addLevel(42)
ponyta.addMoves(["stomp","fire spin"])

rapidash = getPokeStats("Rapidash")
rapidash.addLevel(42)
rapidash.addMoves(["stomp","fire spin"])

arcanine = getPokeStats("Arcanine")
arcanine.addLevel(47)
arcanine.addMoves(["ember","fire blast","take down"])

Blaine = trainer("Blaine")
Blaine.addtrainerInfo([growlithe,ponyta,rapidash,arcanine])

# Giovanni

rhyhorn = getPokeStats("Rhyhorn")
rhyhorn.addLevel(45)
rhyhorn.addMoves(["stomp,""fury attack","horn drill"])

rhydon = getPokeStats("Rhydon")
rhydon.addLevel(50)
rhydon.addMoves(["stomp","horn drill","fissure"])

nidoking = getPokeStats("Nidoking")
nidoking.addLevel(45)
nidoking.addMoves(["tackle","horn attack","poison sting","thrash"])

dugtrio = getPokeStats("Dugtrio")
dugtrio.addLevel(42)
dugtrio.addMoves(["dig","slash"])

nidoqueen = getPokeStats("Nidoqueen")
nidoqueen.addLevel(44)
nidoqueen.addMoves(["scratch","body slam","poison sting"])

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












