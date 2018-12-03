import random
class pokemon:
    type = ""
    hp =0
    attack =0
    defense = 0
    specialAttack = 0
    specialDefense = 0
    speed = 0
    moves = []
    level = 0

    def addPokeInfo(self,type,hp,attack,defense,specAttack,specDefense,speed,level,moves):
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.specialAttack = specAttack
        self.specialDefense = specDefense
        self.speed = speed
        self.moves = moves
        self.level = level
    def __init__(self,name):
        self.name = name
    def getType(self):
        return self.type
    def gethp(self):
        return self.hp
    def getAttack(self):
        return self.attack
    def getDefense(self):
        return self.defense
    def getSPA(self):
        return self.specialAttack
    def getSPDEF(self):
        return self.specialDefense
    def getSpeed(self):
        return self.speed
    def getMoves(self):
        return self.moves
    def getName(self):
        return self.name
    def getLevel(self):
        return self.level

absorb = {"name":"absorb",
          "type": "grass",
          "category": "special",
          "power": 20}
acid = {"name":"acid",
        "type":"poison",
        "category":"special",
        "power":40}
auroraBeam = {"name": "aurora beam",
              "type":"ice",
              "category":"special",
              "power":65}
blizzard = {"name": "blizzard",
              "type":"ice",
              "category":"special",
              "power":100}
bodySlam = {"name": "body slam",
              "type":"normal",
              "category":"physical",
              "power":85}
boneClub = {"name": "bone club",
              "type":"ground",
              "category":"physical",
              "power":65}
bonemerang = {"name": "bonemerang",
              "type":"ground",
              "category":"physcial",
              "power":50}
bubble = {"name": "bubble",
              "type":"water",
              "category":"special",
              "power":40}
bubbleBeam = {"name": "bubble beam",
              "type":"water",
              "category":"special",
              "power":65}
confusion = {"name": "confusion",
              "type":"psychic",
              "category":"special",
              "power":50}
crabhammer = {"name": "crabhammer",
              "type":"water",
              "category":"physical",
              "power":100}
cut = {"name": "cut",
              "type":"normal",
              "category":"physical",
              "power":50}
dig = {"name": "dig",
              "type":"ground",
              "category":"physical",
              "power":80}
dizzyPunch = {"name": "dizzy punch",
              "type":"fight",
              "category":"physical",
              "power":70}
doubleKick = {"name": "double kick",
              "type":"fight",
              "category":"physical",
              "power":60}
doubleEdge = {"name": "double-edge",
              "type":"normal",
              "category":"physcal",
              "power":120}
drillPeck = {"name": "drill peck",
              "type":"flying",
              "category":"physical",
              "power":80}
earthquake = {"name": "earthquake",
              "type":"ground",
              "category":"physical",
              "power":100}
eggbomb = {"name": "egg bomb",
              "type":"normal",
              "category":"physical",
              "power":100}
ember = {"name": "ember",
              "type":"fire",
              "category":"special",
              "power":40}
explosion = {"name": "explosion",
              "type":"normal",
              "category":"special",
              "power":250}
fireBlast = {"name": "fire blast",
              "type":"fire",
              "category":"specail",
              "power":110}
firePunch = {"name": "fire punch",
              "type":"fire",
              "category":"physical",
              "power":75}
fireSpin = {"name": "fire spin",
              "type":"fire",
              "category":"special",
              "power":55}
flamethrower = {"name": "flamethrower",
              "type":"fire",
              "category":"special",
              "power":90}

fly = {"name": "fly",
              "type":"flying",
              "category":"physical",
              "power":90}
gust = {"name": "gust",
              "type":"flying",
              "category":"special",
              "power":40}
headbutt = {"name": "headbutt",
              "type":"normal",
              "category":"physical",
              "power":70}
highJumpKick = {"name": "high jump kick",
              "type":"fight",
              "category":"physical",
              "power":120}
hornAttack = {"name": "horn attack",
              "type":"normal",
              "category":"physical",
              "power":65}
hydroPump = {"name": "hydro pump",
              "type":"water",
              "category":"special",
              "power":110}
hyperBeam = {"name": "hyper beam",
             "type": "nomral",
             "category": "special",
             "power":150}
hyperFang ={"name": "hyper fang",
             "type": "normal",
             "category": "physical",
             "power":80}
iceBeam = {"name": "ice beam",
             "type": "ice",
             "category": "special",
             "power":90}
icePunch = {"name": "ice punch",
             "type": "ice",
             "category": "physical",
             "power":75}
jumpKick = {"name": "jump kick",
             "type": "fight",
             "category": "physical",
             "power":100}
karateChop = {"name": "karate chop",
             "type": "fight",
             "category": "physical",
             "power":50}
leechLife = {"name": "leech life",
             "type": "bug",
             "category": "special",
             "power":80}
lick = {"name": "lick",
             "type": "ghost",
             "category": "physical",
             "power":30}
megaDrain = {"name": "mega drain",
             "type": "grass",
             "category": "special",
             "power":40}
megaKick = {"name": "mega kick",
             "type": "normal",
             "category": "physical",
             "power":120}
megaPunch =  {"name": "mega punch",
             "type": "fight",
             "category": "physical",
             "power":80}
payDay =  {"name": "pay day",
             "type": "normal",
             "category": "physical",
             "power":40}
peck =  {"name": "peck",
             "type": "flying",
             "category": "physical",
             "power":35}
petalDance =  {"name": "petal dance",
             "type": "grass",
             "category": "special",
             "power":120}
pinMissile =  {"name":"pin missile",
             "type": "bug",
             "category": "physical",
             "power":25}
poisonSting =  {"name": "poison sting",
             "type": "poison",
             "category": "physical",
             "power":15}
pound =  {"name": "pound",
             "type": "normal",
             "category": "physical",
             "power":40}
psybeam =  {"name": "psybeam",
             "type": "psychic",
             "category": "special",
             "power":65}
psychic =  {"name": "psychic",
             "type": "psychic",
             "category": "special",
             "power":90}
quickAttack =  {"name":"quick attack",
             "type": "normal",
             "category": "physical",
             "power":40}
rage =  {"name": "rage",
             "type": "normal",
             "category": "physical",
             "power":20}
razorLeaf =  {"name": "razor leaf",
             "type": "grass",
             "category": "physcial",
             "power":55}
razorWind =  {"name": "razor wind",
             "type": "flying",
             "category": "special",
             "power":80}
rockSlide =  {"name": "rock slide",
             "type": "rock",
             "category": "physical",
             "power":75}
rockThrow =  {"name": "rock throw",
             "type": "rock",
             "category": "physical",
             "power":50}
rollingKick =  {"name":"rolling kick",
             "type": "fight",
             "category": "physical",
             "power":60}
scratch =  {"name": "scratch",
             "type": "normal",
             "category": "physical",
             "power":40}
selfDestruct=  {"name": "self destruct",
             "type": "normal",
             "category": "physical",
             "power":200}
skullBash =  {"name": "skull bash",
             "type": "normal",
             "category": "physical",
             "power":130}
skyAttack =  {"name": "sky attack",
             "type": "flying",
             "category": "physical",
             "power":140}
slam =  {"name": "slam",
             "type": "normal",
             "category": "physical",
             "power":80}
slash =  {"name": "slash",
             "type": "normal",
             "category": "physical",
             "power":70}
sludge =  {"name": "sludge",
             "type": "poison",
             "category": "special",
             "power":65}
smog =  {"name": "smog",
             "type": "poison",
             "category": "special",
             "power":30}
solarBeam =  {"name": "solar beam",
             "type": "grass",
             "category": "special",
             "power":120}
spikeCannon =  {"name": "spike cannon",
             "type": "normal",
             "category": "physical",
             "power":20}
stomp =  {"name": "stomp",
             "type": "normal",
             "category": "physical",
             "power":65}
strength =  {"name": "strength",
             "type": "normal",
             "category": "physical",
             "power":80}
struggle = {"name": "struggle",
             "type": "normal",
             "category": "physical",
             "power":50}
submission =  {"name":"submission",
             "type": "fight",
             "category": "physical",
             "power":80}
surf =  {"name": "surf",
             "type": "water",
             "category": "special",
             "power":90}
swift =  {"name": "swift",
             "type": "normal",
             "category": "special",
             "power":60}
tackle =  {"name": "tackle",
             "type": "normal",
             "category": "physical",
             "power":60}
takeDown =  {"name": "take down",
             "type": "normal",
             "category": "physical",
             "power":90}
thrash =  {"name": "thrash",
             "type": "normal",
             "category": "physical",
             "power":120}
thunder =  {"name": "thunder",
             "type": "electric",
             "category": "special",
             "power":110}
thunderPunch =  {"name":"thunder punch",
             "type": "electric",
             "category": "special",
             "power":75}
thunderShock =  {"name":"thunder shock",
             "type": "electric",
             "category": "special",
             "power":40}
thunderbolt =  {"name": "thunderbolt",
             "type": "electric",
             "category": "special",
             "power":90}
triAttack =  {"name": "tri attack",
             "type": "normal",
             "category": "special",
             "power":80}
twineedle =  {"name": "twineedle",
             "type": "bug",
             "category": "special",
             "power":25}
viceGrip = {"name": "vice grip",
             "type": "normal",
             "category": "physical",
             "power":55}
vineWhip =  {"name": "vine whip",
             "type": "grass",
             "category": "physical",
             "power":45}
waterGun =  {"name": "water gun",
             "type": "water",
             "category": "special",
             "power":40}
waterfall =  {"name": "waterfall",
             "type": "water",
             "category": "physical",
             "power":80}
wingAttack =  {"name":"wing attack",
             "type": "flying",
             "category": "physical",
             "power":60}
wrap =  {"name": "wrap",
             "type": "normal",
             "category": "physical",
             "power":15}




moves = [absorb,acid,auroraBeam,blizzard,bodySlam,boneClub,bodySlam,bonemerang,bubble,
         bubbleBeam,confusion,crabhammer,cut,dig,dizzyPunch,doubleKick,doubleEdge,drillPeck,earthquake,eggbomb,ember,explosion,fireBlast,firePunch,fireSpin,flamethrower,fly,gust,
         headbutt,highJumpKick,hornAttack,hydroPump,hyperBeam,hyperFang,iceBeam,icePunch,jumpKick,karateChop,leechLife,lick,megaDrain,megaKick,megaPunch,payDay,peck,
         petalDance,pinMissile,poisonSting,pound,psybeam,psychic,rage,razorLeaf,razorWind,rockSlide,rockThrow,rollingKick,scratch,selfDestruct,skullBash,skyAttack,slam,slash,
         sludge,smog,solarBeam,spikeCannon,stomp,strength,struggle,submission,surf,swift,tackle,takeDown,thrash,thunder,thunderbolt,thunderPunch,thunderShock,triAttack,twineedle,
         waterfall,waterGun,wingAttack,wrap,vineWhip,viceGrip,]



typeList = ["normal","fight","flying","poison","ground","rock","bug","bug","ghost","fire","water","grass","electric","psychic","ice","dragon"]
pokemonC = pokemon('Bulbasaur')
pokemonC.addPokeInfo('grass',45,49,49,65,65,45,16,["tackle","vineWhipe"])

pokemonD = pokemon('Squirtle')
pokemonD.addPokeInfo('water',44,48,65,50,64,45,12,["water gun"])






def damageCalulator( pokemonA, pokemonB,move):

    for movem in moves:
        if move == movem["name"]:
            chosenMove = movem
            moveType = chosenMove["type"]
            power = chosenMove["power"]
            movChar = chosenMove["category"]


    # moveType = input("What is the type of the move:")
    # power = int(input("what is the power of the move: "))
    # movChar = input("is the move physical or special:")
    # for testing
    # moveType = "grass"
    # power = 45
    # movChar = "physical"
    target = 1

# Weather factor
    weather = input("Is the weather rainy, harsh sunlight, or normal: ")
    weatherbooster = 0
    # weather = "normal"
    if weather =="rainy":
        if pokemonA.getType == "water":
            weatherbooster = 1.5
        elif pokemonA.getType == "fire":
            weatherbooster = .5
        else:
            weatherbooster = 1
    elif weather == "harsh sunlight":
        if pokemonA.getType == "fire":
            weatherbooster = 1.5
        else:
            weatherbooster = 1
    else:
        weatherbooster = 1
    if pokemonA[6][0]==moveType :     #only takes first type into account
        stab = 1.5
    else:
        stab = 1
#Effectiveness factor

    normalTypeNotEffective = ["rock"]
    normalTypeNoEffect = ["ghost"]

    fightTypeNotEffective = ["flying","poison","bug","psychic"]
    fightTypeSuperEffective = ["normal","rock","ice"]
    fightTypeNoEffect = ["ghost"]


    flyingTypeSuperEffective = ["fight","bug","grass"]
    flyingTypeNotEffective = ["rock","electric"]

    poisonTypeNotEffective = ["poison","ground","rock","ghost"]
    poisonTypeSuperEffective = ["bug","grass",""]


    groundTypeNoEffect = ["flying"]
    groundTypeNotEffective = ["bug","grass"]
    groundTypeSuperEffective = ["poison","rock","fire","electric"]


    rockTypeNotEffective = ["fight","ground"]
    rockTypeSuperEffective = ["flying","bug","fire","ice"]

    bugTypeSuperEffective = ["poison","grass","psychic"]
    bugTypeNotEffective = ["fight","flying","ghost","fire"]


    ghostTypeSuper = ["ghost"]
    ghostTypeNoEffect = ["normal","psychic"]

    fireTypeSuper = ["grass","bug","ice"]
    fireTypeNotEffective = ["rock","fire","water","dragon"]

    waterTypeSuper = ["ground","rock","fire",]
    waterTypeNot = ["water","grass","dragon"]

    grassTypeNotEffective = ["flying","poison","bug","fire","grass","dragon"]
    grassTypeSuper = ["ground","rock","water"]

    electricTypeSuper = ["flying","water"]
    electricTypeNotEffective = ["grass","electric","dragon"]
    electricNoEffect = ["ground"]

    psychicTypeSuper = ["fight","poison"]
    psychicTypeNotEffective = ["electric"]

    iceTypeSuper = ["flying","grround","grass","dragon"]
    iceTypeNotEffective = ["water","ice"]

    dragonTypeSuper = ["dragon"]

    typeA = moveType
    typeB = pokemonB[6][0] #this only takes in first one not both

    effectiveVariable = 0

    if typeA == "normal":
        if typeB in normalTypeNotEffective:
            effectiveVariable = .5
        elif typeB in normalTypeNoEffect:
            effectiveVariable = 0

        else:
            effectiveVariable = 1
    elif typeA =="fight":
        if typeB in fightTypeNoEffect:
            effectiveVariable = 0
        elif typeB in fightTypeSuperEffective:
            effectiveVariable = 2
        elif typeB in fightTypeNotEffective:
            effectiveVariable = .5
        else:
            effectiveVariable = 1
    elif typeA =="flying":
        if typeB in flyingTypeNotEffective:
            effectiveVariable = .5
        elif typeB in flyingTypeSuperEffective:
            effectiveVariable = 2
        else:
            effectiveVariable = 1
    elif typeA == "poison":
        if typeB in poisonTypeNotEffective:
            effectiveVariable = .5
        elif typeB in poisonTypeSuperEffective:
            effectiveVariable = 2
        else:
            effectiveVariable = 1
    elif typeA == "ground":
        if typeB in groundTypeSuperEffective:
            effectiveVariable = 2
        elif typeB in groundTypeNotEffective:
            effectiveVariable = .5
        elif typeB in groundTypeNoEffect:
            effectiveVariable =0
        else:
            effectiveVariable = 1
    elif typeA == "rock":
        if typeB in rockTypeNotEffective:
            effectiveVariable = .5
        elif typeB in rockTypeSuperEffective:
            effectiveVariable = 2
        else:
            effectiveVariable = 1
    elif typeA == "bug":
        if typeB in bugTypeNotEffective:
            effectiveVariable = .5
        elif typeB in bugTypeSuperEffective:
            effectiveVariable =2
        else:
            effectiveVariable = 1
    elif typeA =="ghost":
        if typeB in ghostTypeNoEffect:
            effectiveVariable = 0
        elif typeB in ghostTypeSuper:
            effectiveVariable = 2
        else:
            effectiveVariable = 1
    elif typeA == "fire":
        if typeB in fireTypeSuper:
            effectiveVariable = 2
        elif typeB in fireTypeNotEffective:
            effectiveVariable = .5
        else:
            effectiveVariable = 1
    elif typeA == "water":
        if typeB in waterTypeSuper:
            effectiveVariable = 2
        elif typeB in waterTypeNot:
            effectiveVariable = .5
        else:
            effectiveVariable = 1
    elif typeA == "grass":
        if typeB in grassTypeSuper:
            effectiveVariable = 2
        elif typeB in grassTypeNotEffective:
            effectiveVariable = .5
        else:
            effectiveVariable = 1
    elif typeA == "electric":
        if typeB in electricNoEffect:
            effectiveVariable =0
        elif typeB in electricTypeNotEffective:
            effectiveVariable =.5
        elif typeB in electricTypeSuper:
            effectiveVariable = 2
        else:
            effectiveVariable = 1
    elif typeA =="psychic":
        if typeB in psychicTypeNotEffective:
            effectiveVariable =.5
        elif typeB in psychicTypeSuper:
            effectiveVariable = 2
        else:
            effectiveVariable = 1
    elif typeA == "ice":
        if typeB in iceTypeNotEffective:
            effectiveVariable = .5
        elif typeB in iceTypeSuper:
            effectiveVariable = 2
        else:
            effectiveVariable = 1
    elif typeA == "dragon":
        if typeB in dragonTypeSuper:
            effectiveVariable = 2
        else:
            effectiveVariable = 1
    else:
        print("You imputed an invalid type")




    attackA = pokemonA[0]
    defenseB = pokemonB[1]
    specialAttackA = pokemonA[3]
    specialDefenseB = pokemonB[4]
    level = 1                   #hard code level
    if movChar == "special":
        attackingPower = float(specialAttackA)
        defensePower = float(specialDefenseB)
    else:
        attackingPower = float(attackA)
        defensePower = float(defenseB)

    one =(2*level)
    two = one/5
    three = two + 2
    four = three * power
    five = attackingPower/defensePower
    six = four * five
    seven = six /50
    eight = seven+2
    modifier = weatherbooster * stab * effectiveVariable
    totalDamage = eight * modifier
    totalDamage=int(totalDamage)

    print(pokemonC.getName(),  "will do",totalDamage,"damage to ",pokemonD.getName(),"using move",move)
    return totalDamage

