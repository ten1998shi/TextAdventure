import random

#Character Dictionaries

#Class Stats
playerStr = 0
playerInt = 0
playerVit = 0
playerDex = 0
playerSpd = 0
playerIns = 0
playerDef = 0
playerLuck = 0

#Tier 1 Mobs
tinyRaptor = {
    "str": "5",
    "int": "1",
    "vit": "3",
    "dex": "7",
    "spd": "7",
    "ins": "1",
    "def": "3",
    "luck": "1"
}

caveSpider = {
    "str": "3",
    "int": "1",
    "vit": "2",
    "dex": "6",
    "spd": "5",
    "ins": "1",
    "def": "2",
    "luck": "1"
}

grublingWorm = {
    "str": "1",
    "int": "1",
    "vit": "10",
    "dex": "1",
    "spd": "1",
    "ins": "1",
    "def": "10",
    "luck": "1"
}

whiskerRat = {
    "str": "3",
    "int": "1",
    "vit": "2",
    "dex": "1",
    "spd": "10",
    "ins": "1",
    "def": "4",
    "luck": "1"
}

duskbatHatchling = {
    "str": "1",
    "int": "1",
    "vit": "10",
    "dex": "1",
    "spd": "1",
    "ins": "1",
    "def": "10",
    "luck": "1"
}

#Tier 2 Mobs

squeakclawDrake = {
    "str": "15",
    "int": "5",
    "vit": "10",
    "dex": "5",
    "spd": "10",
    "ins": "5",
    "def": "10",
    "luck": "10"
}

frostlingSprite = {
    "str": "5",
    "int": "25",
    "vit": "5",
    "dex": "5",
    "spd": "10",
    "ins": "10",
    "def": "5",
    "luck": "10"
}

twitchfangBat = {
    "str": "5",
    "int": "5",
    "vit": "5",
    "dex": "5",
    "spd": "40",
    "ins": "5",
    "def": "5",
    "luck": "5"
}

feralGnat = {
    "str": "20",
    "int": "2",
    "vit": "10",
    "dex": "5",
    "spd": "10",
    "ins": "1",
    "def": "10",
    "luck": "1"
}

pufftailRabbit = {
    "str": "10",
    "int": "3",
    "vit": "10",
    "dex": "5",
    "spd": "25",
    "ins": "5",
    "def": "10",
    "luck": "20"
}

#Tier 3 Mobs

emberjawDrake = {
    "str": "35",
    "int": "20",
    "vit": "20",
    "dex": "5",
    "spd": "25",
    "ins": "15",
    "def": "25",
    "luck": "10"
}

vilewingHarpy = {
    "str": "15",
    "int": "20",
    "vit": "10",
    "dex": "30",
    "spd": "40",
    "ins": "10",
    "def": "10",
    "luck": "10"
}

frostclawLynx = {
    "str": "20",
    "int": "10",
    "vit": "20",
    "dex": "5",
    "spd": "30",
    "ins": "5",
    "def": "20",
    "luck": "20"
}

fierceRavanger = {
    "str": "40",
    "int": "5",
    "vit": "20",
    "dex": "5",
    "spd": "35",
    "ins": "5",
    "def": "10",
    "luck": "10"
}

blightrootTreant = {
    "str": "15",
    "int": "10",
    "vit": "40",
    "dex": "5",
    "spd": "5",
    "ins": "5",
    "def": "50",
    "luck": "10"
}

#Tier 4 Mobs

stormBasilisk = {
    "str": "40",
    "int": "25",
    "vit": "40",
    "dex": "20",
    "spd": "20",
    "ins": "20",
    "def": "45",
    "luck": "20"
}

shadowStalker = {
    "str": "20",
    "int": "25",
    "vit": "20",
    "dex": "20",
    "spd": "60",
    "ins": "20",
    "def": "20",
    "luck": "15"
}

ironskinMinotaur = {
    "str": "40",
    "int": "5",
    "vit": "60",
    "dex": "5",
    "spd": "10",
    "ins": "5",
    "def": "60",
    "luck": "5"
}

firefangHydra = {
    "str": "60",
    "int": "10",
    "vit": "40",
    "dex": "5",
    "spd": "20",
    "ins": "1",
    "def": "45",
    "luck": "20"
}

legendaryManticore = {
    "str": "45",
    "int": "45",
    "vit": "45",
    "dex": "45",
    "spd": "45",
    "ins": "45",
    "def": "45",
    "luck": "45"
}

#Boss Monster

infernoDragonSovereign = {
    "str": "65",
    "int": "50",
    "vit": "55",
    "dex": "20",
    "spd": "40",
    "ins": "55",
    "def": "60",
    "luck": "30"
}

titanKing = {
    "str": "25",
    "int": "25",
    "vit": "80",
    "dex": "10",
    "spd": "25",
    "ins": "25",
    "def": "80",
    "luck": "20"
}

plaguebringerBehemoth = {
    "str": "20",
    "int": "70",
    "vit": "40",
    "dex": "20",
    "spd": "40",
    "ins": "40",
    "def": "45",
    "luck": "40"
}

terrorfangChimera = {
    "str": "70",
    "int": "15",
    "vit": "60",
    "dex": "30",
    "spd": "60",
    "ins": "15",
    "def": "45",
    "luck": "30"
}

voidrendLichKing = {
    "str": "30",
    "int": "95",
    "vit": "30",
    "dex": "15",
    "spd": "50",
    "ins": "70",
    "def": "25",
    "luck": "45"
}




#Roll Dice Function
def rollTheDice ():

    diceRollResult = 0

    diceRoll = random.randint (2, 12)

    lckRoll = random.randint (1, 100)

    if lckRoll <= playerLck:    
        
        diceRoll = diceRoll + 2

    print (f'Your roll: {diceRoll}')

    diceRollResult += diceRoll

    while diceRoll > 12:
        
        diceRoll = random.randint (2, 12)
        
        lckRoll = random.randint (1, 100)
        
        if lckRoll <= playerLck:
            
            diceRoll = diceRoll + 2
        
        diceRollResult += diceRoll
        
        print (f'Your roll: {diceRoll}')
        
    print (f'Your result: {diceRollResult}')


def chooseClass():
    chooseClass = 0
    while chooseClass not in range[1, 2, 3]:
        chooseClass = int(input("There are 3 classes. Archer, Warrior and Mage. Which one would you like to start your journey with? Type 1 for Archer, 2 for Warrior or 3 for Mage"))
        if chooseClass == 1:
            playerStr == 5
            playerInt == 5
            playerVit == 10
            playerDex == 15
            playerSpd == 15
            playerLuck == 15
            playerIns == 5
            playerDef == 10
            break
        elif chooseClass == 2:
            playerStr == 15
            playerInt == 5
            playerVit == 15
            playerDex == 10
            playerSpd == 10
            playerLuck == 5
            playerIns == 5
            playerDef == 15
            break
        else:
            playerStr == 5
            playerInt == 15
            playerVit == 10
            playerDex == 10
            playerSpd == 5
            playerLuck == 15
            playerIns == 15
            playerDef == 5
            break
            
    return playerStr, playerInt, playerVit, playerDex, playerSpd, playerLuck, playerIns, playerDef



