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

