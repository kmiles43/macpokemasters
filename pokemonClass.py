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
    def addName(self,name):
        self.name = name
    def addLevel(self,level):
        self.level = level
    def addMoves(self,moves):
        self.moves = moves
    def editMoves(self,move):
        self.moves.append(move)
    def addHp(self,Hp):
        self.hp = Hp
    def getType(self):
        return self.type
    def getHp(self):
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


