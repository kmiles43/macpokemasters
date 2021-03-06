from pokemonClass import pokemon


#name,abilities,against_bug,against_dark,against_dragon,against_electric,against_fairy,against_fight,against_fire,against_flying,against_ghost,against_grass,against_ground,against_ice,against_normal,against_poison,against_psychic,against_rock,against_steel,against_water,attack,base_total,capture_rate,defense,hp,pokedex_number,sp_attack,sp_defense,speed,type1,type2,generation,is_legendary
#name=Pokemon[0]
#attack=Pokemon[20]
#captureRate=Pokemon[22]
#defense=Pokemon[23]
#hp=Pokemon[24]
#spAttack=Pokemon[26]
#spDefense=Pokemon[27]
#speed=Pokemon[28]
#typeList=Pokemon[29]
Pokedex=[
["Bulbasaur","['Overgrow', 'Chlorophyll']",1,1,1,0.5,0.5,0.5,2,2,1,0.25,1,2,1,1,2,1,1,0.5,49,318,45,49,45,1,65,65,45,["grass","poison"],1,0],
["Ivysaur","['Overgrow', 'Chlorophyll']",1,1,1,0.5,0.5,0.5,2,2,1,0.25,1,2,1,1,2,1,1,0.5,62,405,45,63,60,2,80,80,60,["grass","poison"],1,0],
["Venusaur","['Overgrow', 'Chlorophyll']",1,1,1,0.5,0.5,0.5,2,2,1,0.25,1,2,1,1,2,1,1,0.5,100,625,45,123,80,3,122,120,80,["grass","poison"],1,0],
["Charmander","['Blaze', 'Solar Power']",0.5,1,1,1,0.5,1,0.5,1,1,0.5,2,0.5,1,1,1,2,0.5,2,52,309,45,43,39,4,60,50,65,["fire"],1,0],
["Charmeleon","['Blaze', 'Solar Power']",0.5,1,1,1,0.5,1,0.5,1,1,0.5,2,0.5,1,1,1,2,0.5,2,64,405,45,58,58,5,80,65,80,["fire"],1,0],
["Charizard","['Blaze', 'Solar Power']",0.25,1,1,2,0.5,0.5,0.5,1,1,0.25,0,1,1,1,1,4,0.5,2,104,634,45,78,78,6,159,115,100,["fire","flying"],1,0],
["Squirtle","['Torrent', 'Rain Dish']",1,1,1,2,1,1,0.5,1,1,2,1,0.5,1,1,1,1,0.5,0.5,48,314,45,65,44,7,50,64,43,["water"],1,0],
["Wartortle","['Torrent', 'Rain Dish']",1,1,1,2,1,1,0.5,1,1,2,1,0.5,1,1,1,1,0.5,0.5,63,405,45,80,59,8,65,80,58,["water"],1,0],
["Blastoise","['Torrent', 'Rain Dish']",1,1,1,2,1,1,0.5,1,1,2,1,0.5,1,1,1,1,0.5,0.5,103,630,45,120,79,9,135,115,78,["water"],1,0],
["Caterpie","['Shield Dust', 'Run Away']",1,1,1,1,1,0.5,2,2,1,0.5,0.5,1,1,1,1,2,1,1,30,195,255,35,45,10,20,20,45,["bug"],1,0],
["Metapod",['Shed Skin'],1,1,1,1,1,0.5,2,2,1,0.5,0.5,1,1,1,1,2,1,1,20,205,120,55,50,11,25,25,30,["bug"],1,0],
["Butterfree","['Compoundeyes', 'Tinted Lens']",0.5,1,1,2,1,0.25,2,2,1,0.25,0,2,1,1,1,4,1,1,45,395,45,50,60,12,90,80,70,["bug","flying"],1,0],
["Weedle","['Shield Dust', 'Run Away']",0.5,1,1,1,0.5,0.25,2,2,1,0.25,1,1,1,0.5,2,2,1,1,35,195,255,30,40,13,20,20,50,["bug","poison"],1,0],
["Kakuna",['Shed Skin'],0.5,1,1,1,0.5,0.25,2,2,1,0.25,1,1,1,0.5,2,2,1,1,25,205,120,50,45,14,25,25,35,["bug","poison"],1,0],
["Beedrill","['Swarm', 'Sniper']",0.5,1,1,1,0.5,0.25,2,2,1,0.25,1,1,1,0.5,2,2,1,1,150,495,45,40,65,15,15,80,145,["bug","poison"],1,0],
["Pidgey","['Keen Eye', 'Tangled Feet', 'Big Pecks']",0.5,1,1,2,1,1,1,1,0,0.5,0,2,1,1,1,2,1,1,45,251,255,40,40,16,35,35,56,["normal","flying"],1,0],
["Pidgeotto","['Keen Eye', 'Tangled Feet', 'Big Pecks']",0.5,1,1,2,1,1,1,1,0,0.5,0,2,1,1,1,2,1,1,60,349,120,55,63,17,50,50,71,["normal","flying"],1,0],
["Pidgeot","['Keen Eye', 'Tangled Feet', 'Big Pecks']",0.5,1,1,2,1,1,1,1,0,0.5,0,2,1,1,1,2,1,1,80,579,45,80,83,18,135,80,121,["normal","flying"],1,0],
["Rattata","['Run Away', 'Guts', 'Hustle', 'Gluttony', 'Hustle', 'Thick Fat']",1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,1,56,253,255,35,30,19,25,35,72,["normal","dark"],1,0],
["Raticate","['Run Away', 'Guts', 'Hustle', 'Gluttony', 'Hustle', 'Thick Fat']",1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,1,71,413,127,70,75,20,40,80,77,["normal","dark"],1,0],
["Spearow","['Keen Eye', 'Sniper']",0.5,1,1,2,1,1,1,1,0,0.5,0,2,1,1,1,2,1,1,60,262,255,30,40,21,31,31,70,["normal","flying"],1,0],
["Fearow","['Keen Eye', 'Sniper']",0.5,1,1,2,1,1,1,1,0,0.5,0,2,1,1,1,2,1,1,90,442,90,65,65,22,61,61,100,["normal","flying"],1,0],
["Ekans","['Intimidate', 'Shed Skin', 'Unnerve']",0.5,1,1,1,0.5,0.5,1,1,1,0.5,2,1,1,0.5,2,1,1,1,60,288,255,44,35,23,40,54,55,["poison"],1,0],
["Arbok","['Intimidate', 'Shed Skin', 'Unnerve']",0.5,1,1,1,0.5,0.5,1,1,1,0.5,2,1,1,0.5,2,1,1,1,95,448,90,69,60,24,65,79,80,["poison"],1,0],
["Pikachu","['Static', 'Lightningrod']",1,1,1,0.5,1,1,1,0.5,1,1,2,1,1,1,1,1,0.5,1,55,320,190,40,35,25,50,50,90,["electric"],1,0],
["Raichu","['Static', 'Lightningrod', 'Surge Surfer']",1,1,1,0.5,1,1,1,0.5,1,1,2,1,1,1,1,1,0.5,1,85,485,75,50,60,26,95,85,110,["electric"],1,0],
["Sandshrew","['Sand Veil', 'Sand Rush', 'Snow Cloak', 'Slush Rush']",1,1,1,0,1,1,1,1,1,2,1,2,1,0.5,1,0.5,1,2,75,300,255,90,50,27,10,35,40,["ground","ice"],1,0],
["Sandslash","['Sand Veil', 'Sand Rush', 'Snow Cloak', 'Slush Rush']",1,1,1,0,1,1,1,1,1,2,1,2,1,0.5,1,0.5,1,2,100,450,90,120,75,28,25,65,65,["ground","ice"],1,0],
["NidoranFemale","['Poison Point', 'Rivalry', 'Hustle']",0.5,1,1,1,0.5,0.5,1,1,1,0.5,2,1,1,0.5,2,1,1,1,47,275,235,52,55,29,40,40,41,["poison"],1,0],
["Nidorina","['Poison Point', 'Rivalry', 'Hustle']",0.5,1,1,1,0.5,0.5,1,1,1,0.5,2,1,1,0.5,2,1,1,1,62,365,120,67,70,30,55,55,56,["poison"],1,0],
["Nidoqueen","['Poison Point', 'Rivalry', 'Sheer Force']",0.5,1,1,0,0.5,0.5,1,1,1,1,2,2,1,0.25,2,0.5,1,2,92,505,45,87,90,31,75,85,76,["poison","ground"],1,0],
["NidoranMale","['Poison Point', 'Rivalry', 'Hustle']",0.5,1,1,1,0.5,0.5,1,1,1,0.5,2,1,1,0.5,2,1,1,1,57,273,235,40,46,32,40,40,50,["poison"],1,0],
["Nidorino","['Poison Point', 'Rivalry', 'Hustle']",0.5,1,1,1,0.5,0.5,1,1,1,0.5,2,1,1,0.5,2,1,1,1,72,365,120,57,61,33,55,55,65,["poison"],1,0],
["Nidoking","['Poison Point', 'Rivalry', 'Sheer Force']",0.5,1,1,0,0.5,0.5,1,1,1,1,2,2,1,0.25,2,0.5,1,2,102,505,45,77,81,34,85,75,85,["poison","ground"],1,0],
["Clefairy","['Cute Charm', 'Magic Guard', 'Friend Guard']",0.5,0.5,0,1,1,0.5,1,1,1,1,1,1,1,2,1,1,2,1,45,323,150,48,70,35,60,65,35,["fairy"],1,0],
["Clefable","['Cute Charm', 'Magic Guard', 'Unaware']",0.5,0.5,0,1,1,0.5,1,1,1,1,1,1,1,2,1,1,2,1,70,483,25,73,95,36,95,90,60,["fairy"],1,0],
["Vulpix","['Flash Fire', 'Drought', 'Snow Cloak', 'Snow Warning']",0.5,1,1,1,0.5,1,0.5,1,1,0.5,2,0.5,1,1,1,2,0.5,2,41,299,190,40,38,37,50,65,65,["fire","ice"],1,0],
["Ninetales","['Flash Fire', 'Drought', 'Snow Cloak', 'Snow Warning']",0.5,1,1,1,0.5,1,0.5,1,1,0.5,2,0.5,1,1,1,2,0.5,2,67,505,75,75,73,38,81,100,109,["fire","ice"],1,0],
["Jigglypuff","['Cute Charm', 'Competitive', 'Friend Guard']",0.5,0.5,0,1,1,1,1,1,0,1,1,1,1,2,1,1,2,1,45,270,170,20,115,39,45,25,20,["normal","fairy"],1,0],
["Wigglytuff","['Cute Charm', 'Competitive', 'Frisk']",0.5,0.5,0,1,1,1,1,1,0,1,1,1,1,2,1,1,2,1,70,435,50,45,140,40,85,50,45,["normal","fairy"],1,0],
["Zubat","['Inner Focus', 'Infiltrator']",0.25,1,1,2,0.5,0.25,1,1,1,0.25,0,2,1,0.5,2,2,1,1,45,245,255,35,40,41,30,40,55,["poison","flying"],1,0],
["Golbat","['Inner Focus', 'Infiltrator']",0.25,1,1,2,0.5,0.25,1,1,1,0.25,0,2,1,0.5,2,2,1,1,80,455,90,70,75,42,65,75,90,["poison","flying"],1,0],
["Oddish","['Chlorophyll', 'Run Away']",1,1,1,0.5,0.5,0.5,2,2,1,0.25,1,2,1,1,2,1,1,0.5,50,320,255,55,45,43,75,65,30,["grass","poison"],1,0],
["Gloom","['Chlorophyll', 'Stench']",1,1,1,0.5,0.5,0.5,2,2,1,0.25,1,2,1,1,2,1,1,0.5,65,395,120,70,60,44,85,75,40,["grass","poison"],1,0],
["Vileplume","['Chlorophyll', 'Effect Spore']",1,1,1,0.5,0.5,0.5,2,2,1,0.25,1,2,1,1,2,1,1,0.5,80,490,45,85,75,45,110,90,50,["grass","poison"],1,0],
["Paras","['Effect Spore', 'Dry Skin', 'Damp']",2,1,1,0.5,1,0.5,4,4,1,0.25,0.25,2,1,2,1,2,1,0.5,70,285,190,55,35,46,45,55,25,["bug","grass"],1,0],
["Parasect","['Effect Spore', 'Dry Skin', 'Damp']",2,1,1,0.5,1,0.5,4,4,1,0.25,0.25,2,1,2,1,2,1,0.5,95,405,75,80,60,47,60,80,30,["bug","grass"],1,0],
["Venonat","['Compoundeyes', 'Tinted Lens', 'Run Away']",0.5,1,1,1,0.5,0.25,2,2,1,0.25,1,1,1,0.5,2,2,1,1,55,305,190,50,60,48,40,55,45,["bug","poison"],1,0],
["Venomoth","['Shield Dust', 'Tinted Lens', 'Wonder Skin ']",0.5,1,1,1,0.5,0.25,2,2,1,0.25,1,1,1,0.5,2,2,1,1,65,450,75,60,70,49,90,75,90,["bug","poison"],1,0],
["Diglett","['Sand Veil', 'Arena Trap', 'Sand Force', 'Sand Veil', 'Tangling Hair', 'Sand Force']",1,1,1,0,1,1,1,1,1,2,1,2,1,0.5,1,0.5,1,2,55,265,255,30,10,50,35,45,90,["ground"],1,0],
["Dugtrio","['Sand Veil', 'Arena Trap', 'Sand Force', 'Sand Veil', 'Tangling Hair', 'Sand Force']",1,1,1,0,1,1,1,1,1,2,1,2,1,0.5,1,0.5,1,2,100,425,50,60,35,51,50,70,110,["ground"],1,0],
["Meowth","['Pickup', 'Technician', 'Unnerve', 'Pickup', 'Technician', 'Rattled']",1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,1,35,290,255,35,40,52,50,40,90,["normal","dark"],1,0],
["Persian","['Limber', 'Technician', 'Unnerve', 'Fur Coat', 'Technician', 'Rattled']",1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,1,60,440,90,60,65,53,75,65,115,["normal","dark"],1,0],
["Psyduck","['Damp', 'Cloud Nine', 'Swift Swim']",1,1,1,2,1,1,0.5,1,1,2,1,0.5,1,1,1,1,0.5,0.5,52,320,190,48,50,54,65,50,55,["water"],1,0],
["Golduck","['Damp', 'Cloud Nine', 'Swift Swim']",1,1,1,2,1,1,0.5,1,1,2,1,0.5,1,1,1,1,0.5,0.5,82,500,75,78,80,55,95,80,85,["water"],1,0],
["Mankey","['Vital Spirit', 'Anger Point', 'Defiant']",0.5,0.5,1,1,2,1,1,2,1,1,1,1,1,1,2,0.5,1,1,80,305,190,35,40,56,35,45,70,["fighting"],1,0],
["Primeape","['Vital Spirit', 'Anger Point', 'Defiant']",0.5,0.5,1,1,2,1,1,2,1,1,1,1,1,1,2,0.5,1,1,105,455,75,60,65,57,60,70,95,["fighting"],1,0],
["Growlithe","['Intimidate', 'Flash Fire', 'Justified']",0.5,1,1,1,0.5,1,0.5,1,1,0.5,2,0.5,1,1,1,2,0.5,2,70,350,190,45,55,58,70,50,60,["fire"],1,0],
["Arcanine","['Intimidate', 'Flash Fire', 'Justified']",0.5,1,1,1,0.5,1,0.5,1,1,0.5,2,0.5,1,1,1,2,0.5,2,110,555,75,80,90,59,100,80,95,["fire"],1,0],
["Poliwag","['Water Absorb', 'Damp', 'Swift Swim']",1,1,1,2,1,1,0.5,1,1,2,1,0.5,1,1,1,1,0.5,0.5,50,300,255,40,40,60,40,40,90,["water"],1,0],
["Poliwhirl","['Water Absorb', 'Damp', 'Swift Swim']",1,1,1,2,1,1,0.5,1,1,2,1,0.5,1,1,1,1,0.5,0.5,65,385,120,65,65,61,50,50,90,["water"],1,0],
["Poliwrath","['Water Absorb', 'Damp', 'Swift Swim']",0.5,0.5,1,2,2,1,0.5,2,1,2,1,0.5,1,1,2,0.5,0.5,0.5,95,510,45,95,90,62,70,90,70,["water","fighting"],1,0],
["Abra","['Synchronize', 'Inner Focus', 'Magic Guard']",2,2,1,1,1,0.5,1,1,2,1,1,1,1,1,0.5,1,1,1,20,310,200,15,25,63,105,55,90,["psychic"],1,0],
["Kadabra","['Synchronize', 'Inner Focus', 'Magic Guard']",2,2,1,1,1,0.5,1,1,2,1,1,1,1,1,0.5,1,1,1,35,400,100,30,40,64,120,70,105,["psychic"],1,0],
["Alakazam","['Synchronize', 'Inner Focus', 'Magic Guard']",2,2,1,1,1,0.5,1,1,2,1,1,1,1,1,0.5,1,1,1,50,600,50,65,55,65,175,105,150,["psychic"],1,0],
["Machop","['Guts', 'No Guard', 'Steadfast']",0.5,0.5,1,1,2,1,1,2,1,1,1,1,1,1,2,0.5,1,1,80,305,180,50,70,66,35,35,35,["fighting"],1,0],
["Machoke","['Guts', 'No Guard', 'Steadfast']",0.5,0.5,1,1,2,1,1,2,1,1,1,1,1,1,2,0.5,1,1,100,405,90,70,80,67,50,60,45,["fighting"],1,0],
["Machamp","['Guts', 'No Guard', 'Steadfast']",0.5,0.5,1,1,2,1,1,2,1,1,1,1,1,1,2,0.5,1,1,130,505,45,80,90,68,65,85,55,["fighting"],1,0],
["Bellsprout","['Chlorophyll', 'Gluttony']",1,1,1,0.5,0.5,0.5,2,2,1,0.25,1,2,1,1,2,1,1,0.5,75,300,255,35,50,69,70,30,40,["grass","poison"],1,0],
["Weepinbell","['Chlorophyll', 'Gluttony']",1,1,1,0.5,0.5,0.5,2,2,1,0.25,1,2,1,1,2,1,1,0.5,90,390,120,50,65,70,85,45,55,["grass","poison"],1,0],
["Victreebel","['Chlorophyll', 'Gluttony']",1,1,1,0.5,0.5,0.5,2,2,1,0.25,1,2,1,1,2,1,1,0.5,105,490,45,65,80,71,100,70,70,["grass","poison"],1,0],
["Tentacool","['Clear Body', 'Liquid Ooze', 'Rain Dish']",0.5,1,1,2,0.5,0.5,0.5,1,1,1,2,0.5,1,0.5,2,1,0.5,0.5,40,335,190,35,40,72,50,100,70,["water","poison"],1,0],
["Tentacruel","['Clear Body', 'Liquid Ooze', 'Rain Dish']",0.5,1,1,2,0.5,0.5,0.5,1,1,1,2,0.5,1,0.5,2,1,0.5,0.5,70,515,60,65,80,73,80,120,100,["water","poison"],1,0],
["Geodude","['Rock Head', 'Sturdy', 'Sand Veil', 'Magnet Pull', 'Sturdy', 'Galvanize']",1,1,1,0,1,2,0.5,0.5,1,4,2,2,0.5,0.25,1,0.5,2,4,80,300,255,100,40,74,30,30,20,["rock","ground"],1,0],
["Graveler","['Rock Head', 'Sturdy', 'Sand Veil', 'Magnet Pull', 'Sturdy', 'Galvanize']",1,1,1,0,1,2,0.5,0.5,1,4,2,2,0.5,0.25,1,0.5,2,4,95,390,120,115,55,75,45,45,35,["rock","ground"],1,0],
["Golem","['Rock Head', 'Sturdy', 'Sand Veil', 'Magnet Pull', 'Sturdy', 'Galvanize']",1,1,1,0,1,2,0.5,0.5,1,4,2,2,0.5,0.25,1,0.5,2,4,120,495,45,130,80,76,55,65,45,["rock","ground"],1,0],
["Ponyta","['Run Away', 'Flash Fire', 'Flame Body']",0.5,1,1,1,0.5,1,0.5,1,1,0.5,2,0.5,1,1,1,2,0.5,2,85,410,190,55,50,77,65,65,90,["fire"],1,0],
["Rapidash","['Run Away', 'Flash Fire', 'Flame Body']",0.5,1,1,1,0.5,1,0.5,1,1,0.5,2,0.5,1,1,1,2,0.5,2,100,500,60,70,65,78,80,80,105,["fire"],1,0],
["Slowpoke","['Oblivious', 'Own Tempo', 'Regenerator']",2,2,1,2,1,0.5,0.5,1,2,2,1,0.5,1,1,0.5,1,0.5,0.5,65,315,190,65,90,79,40,40,15,["water","psychic"],1,0],
["Slowbro","['Oblivious', 'Own Tempo', 'Regenerator']",2,2,1,2,1,0.5,0.5,1,2,2,1,0.5,1,1,0.5,1,0.5,0.5,75,590,75,180,95,80,130,80,30,["water","psychic"],1,0],
["Magnemite","['Magnet Pull', 'Sturdy', 'Analytic']",0.5,1,0.5,0.5,0.5,2,2,0.25,1,0.5,4,0.5,0.5,0,0.5,0.5,0.25,1,35,325,190,70,25,81,95,55,45,["electric","steel"],1,0],
["Magneton","['Magnet Pull', 'Sturdy', 'Analytic']",0.5,1,0.5,0.5,0.5,2,2,0.25,1,0.5,4,0.5,0.5,0,0.5,0.5,0.25,1,60,465,60,95,50,82,120,70,70,["electric","steel"],1,0],
["Farfetch'd","['Keen Eye', 'Inner Focus', 'Defiant']",0.5,1,1,2,1,1,1,1,0,0.5,0,2,1,1,1,2,1,1,90,377,45,55,52,83,58,62,60,["normal","flying"],1,0],
["Doduo","['Run Away', 'Early Bird', 'Tangled Feet']",0.5,1,1,2,1,1,1,1,0,0.5,0,2,1,1,1,2,1,1,85,310,190,45,35,84,35,35,75,["normal","flying"],1,0],
["Dodrio","['Run Away', 'Early Bird', 'Tangled Feet']",0.5,1,1,2,1,1,1,1,0,0.5,0,2,1,1,1,2,1,1,110,470,45,70,60,85,60,60,110,["normal","flying"],1,0],
["Seel","['Thick Fat', 'Hydration', 'Ice Body']",1,1,1,2,1,1,0.5,1,1,2,1,0.5,1,1,1,1,0.5,0.5,45,325,190,55,65,86,45,70,45,["water"],1,0],
["Dewgong","['Thick Fat', 'Hydration', 'Ice Body']",1,1,1,2,1,2,1,1,1,2,1,0.25,1,1,1,2,1,0.5,70,475,75,80,90,87,70,95,70,["water,ice"],1,0],
["Grimer","['Stench', 'Sticky Hold', 'Poison Touch', 'Poison Touch', 'Gluttony', 'Power of Alchemy']",0.5,1,1,1,0.5,0.5,1,1,1,0.5,2,1,1,0.5,2,1,1,1,80,325,190,50,80,88,40,50,25,["poison"],1,0],
["Muk","['Stench', 'Sticky Hold', 'Poison Touch', 'Poison Touch', 'Gluttony', 'Power of Alchemy']",0.5,1,1,1,0.5,0.5,1,1,1,0.5,2,1,1,0.5,2,1,1,1,105,500,75,75,105,89,65,100,50,["poison"],1,0],
["Shellder","['Shell Armor', 'Skill Link', 'Overcoat']",1,1,1,2,1,1,0.5,1,1,2,1,0.5,1,1,1,1,0.5,0.5,65,305,190,100,30,90,45,25,40,["water"],1,0],
["Cloyster","['Shell Armor', 'Skill Link', 'Overcoat']",1,1,1,2,1,2,1,1,1,2,1,0.25,1,1,1,2,1,0.5,95,525,60,180,50,91,85,45,70,["water","ice"],1,0],
["Gastly",['Levitate'],0.25,2,1,1,0.5,0,1,1,2,0.5,2,1,0,0.25,2,1,1,1,35,310,190,30,30,92,100,35,80,["ghost","poison"],1,0],
["Haunter",['Levitate'],0.25,2,1,1,0.5,0,1,1,2,0.5,2,1,0,0.25,2,1,1,1,50,405,90,45,45,93,115,55,95,["ghost","poison"],1,0],
["Gengar",['Cursed Body'],0.25,2,1,1,0.5,0,1,1,2,0.5,2,1,0,0.25,2,1,1,1,65,600,45,80,60,94,170,95,130,["ghost","poison"],1,0],
["Onix","['Rock Head', 'Sturdy', 'Weak Armor']",1,1,1,0,1,2,0.5,0.5,1,4,2,2,0.5,0.25,1,0.5,2,4,45,385,45,160,35,95,30,45,70,["rock","ground"],1,0],
["Drowzee","['Insomnia', 'Forewarn', 'Inner Focus']",2,2,1,1,1,0.5,1,1,2,1,1,1,1,1,0.5,1,1,1,48,328,190,45,60,96,43,90,42,["psychic"],1,0],
["Hypno","['Insomnia', 'Forewarn', 'Inner Focus']",2,2,1,1,1,0.5,1,1,2,1,1,1,1,1,0.5,1,1,1,73,483,75,70,85,97,73,115,67,["psychic"],1,0],
["Krabby","['Hyper Cutter', 'Shell Armor', 'Sheer Force']",1,1,1,2,1,1,0.5,1,1,2,1,0.5,1,1,1,1,0.5,0.5,105,325,225,90,30,98,25,25,50,["water"],1,0],
["Kingler","['Hyper Cutter', 'Shell Armor', 'Sheer Force']",1,1,1,2,1,1,0.5,1,1,2,1,0.5,1,1,1,1,0.5,0.5,130,475,60,115,55,99,50,50,75,["water"],1,0],
["Voltorb","['Soundproof', 'Static', 'Aftermath']",1,1,1,0.5,1,1,1,0.5,1,1,2,1,1,1,1,1,0.5,1,30,330,190,50,40,100,55,55,100,["electric"],1,0],
["Electrode","['Soundproof', 'Static', 'Aftermath']",1,1,1,0.5,1,1,1,0.5,1,1,2,1,1,1,1,1,0.5,1,50,490,60,70,60,101,80,80,150,["electric"],1,0],
["Exeggcute","['Chlorophyll', 'Harvest']",4,2,1,0.5,1,0.5,2,2,2,0.5,0.5,2,1,2,0.5,1,1,0.5,40,325,90,80,60,102,60,45,40,["grass","psychic"],1,0],
["Exeggutor","['Chlorophyll', 'Harvest', 'Frisk', 'Harvest']",4,2,1,0.5,1,0.5,2,2,2,0.5,0.5,2,1,2,0.5,1,1,0.5,105,530,45,85,95,103,125,75,45,["grass","psychic"],1,0],
["Cubone","['Rock Head', 'Lightningrod', 'Battle Armor']",1,1,1,0,1,1,1,1,1,2,1,2,1,0.5,1,0.5,1,2,50,320,190,95,50,104,40,50,35,["ground"],1,0],
["Marowak","['Rock Head', 'Lightningrod', 'Battle Armor', 'Cursed Body', 'Lightningrod', 'Rock Head']",1,1,1,0,1,1,1,1,1,2,1,2,1,0.5,1,0.5,1,2,80,425,75,110,60,105,50,80,45,["ground","fire"],1,0],
["Hitmonlee","['Limber', 'Reckless', 'Unburden']",0.5,0.5,1,1,2,1,1,2,1,1,1,1,1,1,2,0.5,1,1,120,455,45,53,50,106,35,110,87,["fighting"],1,0],
["Hitmonchan","['Keen Eye', 'Iron Fist', 'Inner Focus']",0.5,0.5,1,1,2,1,1,2,1,1,1,1,1,1,2,0.5,1,1,105,455,45,79,50,107,35,110,76,["fighting"],1,0],
["Lickitung","['Own Tempo', 'Oblivious', 'Cloud Nine']",1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,1,55,385,45,75,90,108,60,75,30,["normal"],1,0],
["Koffing",['Levitate'],0.5,1,1,1,0.5,0.5,1,1,1,0.5,2,1,1,0.5,2,1,1,1,65,340,190,95,40,109,60,45,35,["poison"],1,0],
["Weezing",['Levitate'],0.5,1,1,1,0.5,0.5,1,1,1,0.5,2,1,1,0.5,2,1,1,1,90,490,60,120,65,110,85,70,60,["poison"],1,0],
["Rhyhorn","['Lightningrod', 'Rock Head', 'Reckless']",1,1,1,0,1,2,0.5,0.5,1,4,2,2,0.5,0.25,1,0.5,2,4,85,345,120,95,80,111,30,30,25,["ground","rock"],1,0],
["Rhydon","['Lightningrod', 'Rock Head', 'Reckless']",1,1,1,0,1,2,0.5,0.5,1,4,2,2,0.5,0.25,1,0.5,2,4,130,485,60,120,105,112,45,45,40,["ground","rock"],1,0],
["Chansey","['Natural Cure', 'Serene Grace', 'Healer']",1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,1,5,450,30,5,250,113,35,105,50,["normal"],1,0],
["Tangela","['Chlorophyll', 'Leaf Guard', 'Regenerator']",2,1,1,0.5,1,1,2,2,1,0.5,0.5,2,1,2,1,1,1,0.5,55,435,45,115,65,114,100,40,60,["grass"],1,0],
["Kangaskhan","['Early Bird', 'Scrappy', 'Inner Focus']",1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,1,125,590,45,100,105,115,60,100,100,["normal"],1,0],
["Horsea","['Swift Swim', 'Sniper', 'Damp']",1,1,1,2,1,1,0.5,1,1,2,1,0.5,1,1,1,1,0.5,0.5,40,295,225,70,30,116,70,25,60,["water"],1,0],
["Seadra","['Poison Point', 'Sniper', 'Damp']",1,1,1,2,1,1,0.5,1,1,2,1,0.5,1,1,1,1,0.5,0.5,65,440,75,95,55,117,95,45,85,["water"],1,0],
["Goldeen","['Swift Swim', 'Water Veil', 'Lightningrod']",1,1,1,2,1,1,0.5,1,1,2,1,0.5,1,1,1,1,0.5,0.5,67,320,225,60,45,118,35,50,63,["water"],1,0],
["Seaking","['Swift Swim', 'Water Veil', 'Lightningrod']",1,1,1,2,1,1,0.5,1,1,2,1,0.5,1,1,1,1,0.5,0.5,92,450,60,65,80,119,65,80,68,["water"],1,0],
["Staryu","['Illuminate', 'Natural Cure', 'Analytic']",1,1,1,2,1,1,0.5,1,1,2,1,0.5,1,1,1,1,0.5,0.5,45,340,225,55,30,120,70,55,85,["water"],1,0],
["Starmie","['Illuminate', 'Natural Cure', 'Analytic']",2,2,1,2,1,0.5,0.5,1,2,2,1,0.5,1,1,0.5,1,0.5,0.5,75,520,60,85,60,121,100,85,115,["water","psychic"],1,0],
["Mr. Mime","['Soundproof', 'Filter', 'Technician']",1,1,0,1,1,0.25,1,1,2,1,1,1,1,2,0.5,1,2,1,45,460,45,65,40,122,100,120,90,["psychic","fairy"],1,0],
["Scyther","['Swarm', 'Technician', 'Steadfast']",0.5,1,1,2,1,0.25,2,2,1,0.25,0,2,1,1,1,4,1,1,110,500,45,80,70,123,55,80,105,["bug","flying"],1,0],
["Jynx","['Oblivious', 'Forewarn', 'Dry Skin']",2,2,1,1,1,1,2,1,2,1,1,0.5,1,1,0.5,2,2,1,50,455,45,35,65,124,115,95,95,["ice","psychic"],1,0],
["Electabuzz","['Static', 'Vital Spirit']",1,1,1,0.5,1,1,1,0.5,1,1,2,1,1,1,1,1,0.5,1,83,490,45,57,65,125,95,85,105,["electric"],1,0],
["Magmar","['Flame Body', 'Vital Spirit']",0.5,1,1,1,0.5,1,0.5,1,1,0.5,2,0.5,1,1,1,2,0.5,2,95,495,45,57,65,126,100,85,93,["fire"],1,0],
["Pinsir","['Hyper Cutter', 'Mold Breaker', 'Moxie']",1,1,1,1,1,0.5,2,2,1,0.5,0.5,1,1,1,1,2,1,1,155,600,45,120,65,127,65,90,105,["bug"],1,0],
["Tauros","['Intimidate', 'Anger Point', 'Sheer Force']",1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,1,100,490,45,95,75,128,40,70,110,["normal"],1,0],
["Magikarp","['Swift Swim', 'Rattled']",1,1,1,2,1,1,0.5,1,1,2,1,0.5,1,1,1,1,0.5,0.5,10,200,255,55,20,129,15,20,80,["water"],1,0],
["Gyarados","['Intimidate', 'Moxie']",0.5,1,1,4,1,0.5,0.5,1,1,1,0,1,1,1,1,2,0.5,0.5,155,640,45,109,95,130,70,130,81,["water","flying"],1,0],
["Lapras","['Water Absorb', 'Shell Armor', 'Hydration']",1,1,1,2,1,2,1,1,1,2,1,0.25,1,1,1,2,1,0.5,85,535,45,80,130,131,85,95,60,["water","ice"],1,0],
["Ditto","['Limber', 'Imposter']",1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,1,48,288,35,48,48,132,48,48,48,["normal"],1,0],
["Eevee","['Run Away', 'Adaptability', 'Anticipation']",1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,1,55,325,45,50,55,133,45,65,55,["normal"],1,0],
["Vaporeon","['Water Absorb', 'Hydration']",1,1,1,2,1,1,0.5,1,1,2,1,0.5,1,1,1,1,0.5,0.5,65,525,45,60,130,134,110,95,65,["water"],1,0],
["Jolteon","['Volt Absorb', 'Quick Feet']",1,1,1,0.5,1,1,1,0.5,1,1,2,1,1,1,1,1,0.5,1,65,525,45,60,65,135,110,95,130,["electric"],1,0],
["Flareon","['Flash Fire', 'Guts']",0.5,1,1,1,0.5,1,0.5,1,1,0.5,2,0.5,1,1,1,2,0.5,2,130,525,45,60,65,136,95,110,65,["fire"],1,0],
["Porygon","['Trace', 'Download', 'Analytic']",1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,1,60,395,45,70,65,137,85,75,40,["normal"],1,0],
["Omanyte","['Swift Swim', 'Shell Armor', 'Weak Armor']",1,1,1,2,1,2,0.25,0.5,1,4,2,0.5,0.5,0.5,1,1,1,1,40,355,45,100,35,138,90,55,35,["rock","water"],1,0],
["Omastar","['Swift Swim', 'Shell Armor', 'Weak Armor']",1,1,1,2,1,2,0.25,0.5,1,4,2,0.5,0.5,0.5,1,1,1,1,60,495,45,125,70,139,115,70,55,["rock","water"],1,0],
["Kabuto","['Swift Swim', 'Battle Armor', 'Weak Armor']",1,1,1,2,1,2,0.25,0.5,1,4,2,0.5,0.5,0.5,1,1,1,1,80,355,45,90,30,140,55,45,55,["rock","water"],1,0],
["Kabutops","['Swift Swim', 'Battle Armor', 'Weak Armor']",1,1,1,2,1,2,0.25,0.5,1,4,2,0.5,0.5,0.5,1,1,1,1,115,495,45,105,60,141,65,70,80,["rock","water"],1,0],
["Aerodactyl","['Rock Head', 'Pressure', 'Unnerve']",0.5,1,1,2,1,1,0.5,0.5,1,1,0,2,0.5,0.5,1,2,2,2,135,615,45,85,80,142,70,95,150,["rock","flying"],1,0],
["Snorlax","['Immunity', 'Thick Fat', 'Gluttony']",1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,1,110,540,25,65,160,143,65,110,30,["normal"],1,0],
["Articuno","['Pressure', 'Snow Cloak']",0.5,1,1,2,1,1,2,1,1,0.5,0,1,1,1,1,4,2,1,85,580,3,100,90,144,95,125,85,["ice","flying"],1,1],
["Zapdos","['Pressure', 'Static']",0.5,1,1,1,1,0.5,1,0.5,1,0.5,0,2,1,1,1,2,0.5,1,90,580,3,85,90,145,125,90,100,["electric","flying"],1,1],
["Moltres","['Pressure', 'Flame Body']",0.25,1,1,2,0.5,0.5,0.5,1,1,0.25,0,1,1,1,1,4,0.5,2,100,580,3,90,90,146,125,85,90,["fire","flying"],1,1],
["Dratini","['Shed Skin', 'Marvel Scale']",1,1,2,0.5,2,1,0.5,1,1,0.5,1,2,1,1,1,1,1,0.5,64,300,45,45,41,147,50,50,50,["dragon"],1,0],
["Dragonair","['Shed Skin', 'Marvel Scale']",1,1,2,0.5,2,1,0.5,1,1,0.5,1,2,1,1,1,1,1,0.5,84,420,45,65,61,148,70,70,70,["dragon"],1,0],
["Dragonite","['Inner Focus', 'Multiscale']",0.5,1,2,1,2,0.5,0.5,1,1,0.25,0,4,1,1,1,2,1,0.5,134,600,45,95,91,149,100,100,80,["dragon","flying"],1,0],
["Mewtwo","['Pressure', 'Unnerve']",2,2,1,1,1,0.5,1,1,2,1,1,1,1,1,0.5,1,1,1,150,780,3,70,106,150,194,120,140,["psychic"],1,1],
["Mew",['Synchronize'],2,2,1,1,1,0.5,1,1,2,1,1,1,1,1,0.5,1,1,1,100,600,45,100,100,151,100,100,100,["psychic"],1,1]
]

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

genIPokemon = []
for poke in Pokedex:
    name = poke[0]
    attack = poke[20]
    defense = poke[23]
    hp = poke[24]
    spAttack = poke[26]
    spDefense = poke[27]
    speed = poke[28]
    typeList = poke[29]
    stockPokemon = pokemon(name)
    stockPokemon.addName(name)
    stockPokemon.addPokeInfo(typeList,hp,attack,defense,spAttack,spDefense,speed,50,[""])
    genIPokemon.append(stockPokemon)
pokeNames = []
for poke in Pokedex:
    name = poke[0]
    pokeNames.append(name)

def getPokeStats(poke1):
    for poke in genIPokemon:
        pokemonIndex = poke.getName()
        if poke1 == pokemonIndex:
            poke2 = poke
            return poke2


# for pokemon in genIPokemon:
#     print(pokemon.getName())
