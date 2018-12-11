import random

pokemonNames = {
    "bulbasaur":45,
    "ivysaur": 45,
    "venusaur":45,
    "squirtle":45,
    "wartortle":45,
    "blastoise":45,
    "charmander":45,
    "charmeleon":45,
    "caterpie":255,
    "metapod":120,
    "butterfree":45,
    "weedle":255,
    "kakuna":120,
    "beedrill":45,
    "pidgey":255,
    "pidgeotto":127,
    "pidgeot": 45,
    "rattatta":255,
    "raticate":90,
    "soearow": 255,
    "fearow":90,
    "ekans":255,
    "arbok":90,
    "pikachu":190,
    "raichu":75,
    "sandshrew":255,
    "sandslash":90,
    "nidoran":235,
    "nidorina":120,
    "nidoqueen":45,
    "nidorino":120,
    "nidoking":45,
    "clefairy":150,
    "clefable":25,
    "vulpix": 190,
    "ninetales":75,
    "jigglypuff":170,
    "wigglypuff":50,
    "zubat":255,
    "goldbat":90,
    "oddish":255,
    "gloom":120,
    "vileplume":45,
    "paras":190,
    "parasect":75,
    "venonat":190,
    "venomoth":75,
    "diglett":255,
    "dugtrio":50,
    "meowth":255,
    "persian":90,
    "psyduck":190,
    "golduck":75,
    "mankey":190,
    "primeape":75,
    "growlithe":190,
    "arcanine":75,
    "poliwag":255,
    "poliwhirl":120,
    "poliwrath":45,
    "abra":200,
    "kadabra":100,
    "alakazam":50,
    "machop":180,
    "machoke":90,
    "machamp":45,
    "bellsprout":255,
    "weepinbell":120,
    "victreebel":45,
    "tentacool":190,
    "tentacruel":60,
    "geodude":255,
    "graveler":120,
    "golem":45,
    "ponyta":190,
    "rapidash":60,
    "slowpoke":190,
    "slowbro":75,
    "magnemite":190,
    "magneton":60,
    "farfetch'd":45,
    "doduo":190,
    "dodrio":45,
    "seel":190,
    "dewgong":75,
    "grimer":190,
    "muk":75,
    "sheldder":190,
    "cloyster":60,
    "gastly":190,
    "haunter":90,
    "gengar":45,
    "onix":45,
    "drowzee":190,
    "hypno":75,
    "krabby":255,
    "kingler":60,
    "voltorb":190,
    "electrode":60,
    "exeggcute":90,
    "exeggutor":45,
    "cubone":190,
    "marowak":75,
    "hitmonlee":45,
    "hitmonchan":45,
    "lickitung":45,
    "koffing":190,
    "weezing":60,
    "rhyhorn":120,
    "rhydon":60,
    "chansey":30,
    "tangela":45,
    "kangaskhan":45,
    "horsea":225,
    "seadra":75,
    "goldeen":255,
    "seaking":60,
    "staryu":225,
    "starmie":60,
    "mr.mime":45,
    "scyther":45,
    "jynx":45,
    "electabuzz":45,
    "magmar":45,
    "pinsir":45,
    "tauros":45,
    "magikarp":255,
    "gyarados":45,
    "lapras":45,
    "ditto":35,
    "eevee":45,
    "vaporeon":45,
    "jolteon":45,
    "flareon":45,
    "porygon":45,
    "omanyte":45,
    "omastar":45,
    "kabuto":45,
    "kabutops":45,
    "aerodactyl":45,
    "snorlax":25,
    "articuno":3,
    "zapdos":3,
    "moltres":3,
    "dratini":45,
    "drangonair": 45,
    "dragonite":45,
    "mewtwo":3,
    "mew":45,
}
def pokeCaptureGenI(maxHp,name):
    capture = False
    if name in pokemonNames:
        captureRate = pokemonNames[name]
        status = input('What is the status of the pokemon: ')
        ballType = input("What ball are you using?")
        Hp = int( input("How much health does it have left?"))

        status = status.lower()
        ballType = ballType.lower()
        if ballType == "MasterBall":
            capture = True
            return  capture

        if ballType =="Poke Ball":
             R1 = random.randint(0,255)
        elif ballType == "Great Ball":
            R1 = random.randint(0,200)
        else:
            R1 = random.randint(0,150)

        if status in ["frozen", "asleep"]:
            s = 25
        elif status in ["burned", "paralyzed", "poisoned"]:
            s = 12
        else:
            s = 0
        num = R1 - s

        if num < 0:
            capture = True
            return capture
        F = maxHp * 255
        if ballType =="great ball":
            F = F/8
        else:
            F = F/12
        Hp = Hp/4
        if Hp > 0:
            F = F/Hp
        if F > 255:
            F = 255
        if captureRate < num:
            capture = False
            return  capture
        R2 = random.randrange(0,255)
        if R2 <= F:
            capture = True

            return capture, "You will catch it"
        else:
            return capture, "The pokemon will break free"
    else:
        print("name input error")
