import random
#Character Dictionaries

#Player Level
playerLevel = 1

#Player class
playerClass = ""
#Class Stats
playerStr = 0 
playerInt = 0
playerVit = 0
playerDex = 0
playerSpd = 0
playerIns = 0
playerDef = 0
playerLuck = 0

#Player Exp
playerExp = 0 
levelUpExp = 10

# Player Inventory
playerInventory = {
    "Weapon": "",
    "Armor": "",
    "Gloves": "",
    "Boots": "",
    "Ring slot 1": "",
    "Ring slot 2": "",
    "Necklace": ""
}

#Tier 1 Mobs
tinyRaptor = {
    "Tier": "1",
    "name": "Tiny Raptor",
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
    "Tier": "1",
    "name": "Cave Spider",
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
    "Tier": "1",
    "name":"Grubling Worm",
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
    "Tier": "1",
    "name": "Whisker Rat",
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
    "Tier": "1",
    "name": "Duskbat Hatchling",
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
    "Tier": "2",
    "name": "Squeak Claw Drake",
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
    "Tier": "2",
    "name": "Frostling Sprite",
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
    "Tier": "2",
    "name": "Twitch Fang Bat",
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
    "Tier": "2",
    "name": "Feral Gnat",
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
    "Tier": "2",
    "name": "Puff Tail Rabbit",
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
    "Tier": "3",
    "name": "Emberjaw Drake",
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
    "Tier": "3",
    "name": "Vile Wing Harpy",
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
    "Tier": "3",
    "name": "Frostclaw Lynx",
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
    "Tier": "3",
    "name": "Fierce Ravanger",
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
    "Tier": "3",
    "name": "Blightroot Treant",
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
    "Tier": "4",
    "name": "Storm Basilisk",
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
    "Tier": "4",
    "name": "Shadow Stalker",
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
    "Tier": "4",
    "name": "ironskin Minotaur",
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
    "Tier": "4",
    "name": "Firefang Hydra",
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
    "Tier": "4",
    "name": "Legendary Manticore",
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
    "name": "Inferno Dragon Sovereign",
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
    "name": "Titan King",
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
    "name": "Plaguebringer Behemoth",
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
    "name": "Terrorfang Chimera",
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
    "name": "Voidrend Lich King",
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
def rollTheDice (tempPlayerLck):

    diceRollResult = 0

    diceRoll = random.randint (2, 12)

    lckRoll = random.randint (1, 100)

    if lckRoll <= tempPlayerLck:    
        
        diceRoll = diceRoll + 2

    print (f'Dice roll: {diceRoll}')

    diceRollResult += diceRoll

    while diceRoll > 12:
        
        diceRoll = random.randint (2, 12)
        
        lckRoll = random.randint (1, 100)
        
        if lckRoll <= tempPlayerLck:
            
            diceRoll = diceRoll + 2
        
        diceRollResult += diceRoll
        
        print (f'Dice roll: {diceRoll}')
        
    print (f'End result: {diceRollResult}')
    
    return diceRollResult
    

#Combat Function
  
<<<<<<< HEAD
def startCombat (playerVitTemp, playerStrTemp, playerDefTemp, playerSpdTemp, enemyVitTemp, enemyStrTemp, enemyDefTemp, enemySpdTemp):
    
    global levelUpExp
    
=======
currentMob = mobEncounter (4)

def startCombat (playerVitTemp, playerStrTemp, playerDefTemp, playerSpdTemp, enemyVitTemp, enemyStrTemp, enemyDefTemp, enemySpdTemp):
    
    
    input ('Combat starts!')
    
    # check if enemy is actually faster and thus goes first
    if enemySpdTemp > playerSpdTemp:            
        
        input ('The enemy starts the round!')
        
        playerDodgeChance = playerSpdTemp / 200
        enemyHitChance = random.random ()

        if playerDodgeChance > enemyHitChance:
            input ('You dodged the attack!')
                    
        elif playerDodgeChance < enemyHitChance:        
            enemyAtk = enemyStrTemp + rollTheDice (50)        
            input (f'The enemy attacks with {enemyAtk} damage!')
            playerDmgProt = playerDefTemp / 100    
            dmgOnPlayer = playerDmgProt * enemyAtk    
            playerVitTemp -= dmgOnPlayer
            input (f'The enemy deals {dmgOnPlayer} damage.')
            input (f'You have {playerVitTemp}Hp remaining.')
                    
                        
        elif playerDodgeChance == enemyHitChance:
                    
                playerTieBreaker = random.random ()
                enemyTieBreaker = random.random ()
                    
                # just in case they actually roll the same number again >.>        
                while enemyTieBreaker == playerTieBreaker:
                            
                    playerTieBreaker = random.random ()
                    enemyTieBreaker = random.random ()
                        
                    # if the enemy wins the tie breaker, they start. otherwise nothing happens and player starts by default
                if enemyTieBreaker > playerTieBreaker:
                        
                    enemyAtk = enemyStrTemp + rollTheDice (50)    
                    input (f'The enemy attacks with {enemyAtk} damage!')
                    playerDmgProt = playerDefTemp / 100    
                    dmgOnPlayer = playerDmgProt * enemyAtk    
                    playerVitTemp -= dmgOnPlayer
                    input (f'The enemy deals {dmgOnPlayer} damage.')
                    input (f'You have {playerVitTemp}Hp remaining.')
        
    # if both are the same speed, they roll a number between 0-1 and the larger number wins    
    elif enemySpdTemp == playerSpdTemp:
        
        playerTieBreaker = random.random ()
        enemyTieBreaker = random.random ()
       
       # just in case they actually roll the same number again >.>
        while enemyTieBreaker == playerTieBreaker:
            
            playerTieBreaker = random.random ()
            enemyTieBreaker = random.random ()
        
        # if the enemy wins the tie breaker, they start. otherwise nothing happens and player starts by default
        if enemyTieBreaker > playerTieBreaker:
            
            playerDodgeChance = playerSpdTemp / 200
            enemyHitChance = random.random ()
            
            if playerDodgeChance > enemyHitChance:
                input ('You dodged the attack!')
                                             
            elif playerDodgeChance == enemyHitChance:
                    
                playerTieBreaker = random.random ()
                enemyTieBreaker = random.random ()
                    
                # just in case they actually roll the same number again >.>        
                while enemyTieBreaker == playerTieBreaker:
                            
                    playerTieBreaker = random.random ()
                    enemyTieBreaker = random.random ()
                        
               
                # if the enemy wins the tie breaker, they start. otherwise nothing happens and player starts by default
                if enemyTieBreaker > playerTieBreaker:
                        
                    enemyAtk = enemyStrTemp + rollTheDice (50)    
                    input (f'The enemy attacks with {enemyAtk} damage!')
                    playerDmgProt = playerDefTemp / 100    
                    dmgOnPlayer = playerDmgProt * enemyAtk    
                    playerVitTemp -= dmgOnPlayer
                    input (f'The enemy deals {dmgOnPlayer} damage.')
                    input (f'You have {playerVitTemp}Hp remaining.')
            
            
            
            
            
        # fighting is a loop that continues on until someone loses all their hp
    while  playerVitTemp or enemyVitTemp > 0:    
            
            playerChoice = input ('Choose your action (attack, defend, item, talk): ')
            
            if playerChoice == 'attack': 
        
                enemyDodgeChance = enemySpdTemp / 200
                playerHitChance = random.random ()

                if enemyDodgeChance > playerHitChance:
                    input ('The enemy dodged the attack!')
                            
                elif enemyDodgeChance < playerHitChance:        
                    playerAtk = playerStrTemp + rollTheDice (50)        
                    input (f'You attack with {playerAtk} damage!')
                    enemyDmgProt = enemyDefTemp / 100    
                    dmgOnEnemy = enemyDmgProt * playerAtk    
                    enemyVitTemp -= dmgOnEnemy
                    input (f'You deal {dmgOnEnemy} damage.')
                    input (f'The enemy has {enemyVitTemp}Hp remaining.')
                    
                    if enemyVitTemp <= 0:
                        input ('Sweet victory at last! All hail the glorious wall kitten!')
                        
                        expGainedAfterCombat(2)

                        while playerExp > levelUpExp:
                            levelUpExp = levelUpExp + levelUpExp
                        
                        break
                        
                        
                        
                        
                        
                            
                                
                elif playerDodgeChance == enemyHitChance:
                            
                        playerTieBreaker = random.random ()
                        enemyTieBreaker = random.random ()
                            
                        # just in case they actually roll the same number again >.>        
                        while enemyTieBreaker == playerTieBreaker:
                                    
                            playerTieBreaker = random.random ()
                            enemyTieBreaker = random.random ()
                                
                            # if the enemy wins the tie breaker, they start. otherwise nothing happens and player starts by default
                        if enemyTieBreaker > playerTieBreaker:
                                
                            playerAtk = playerStrTemp + rollTheDice (50)        
                            input (f'You attack with {playerAtk} damage!')
                            enemyDmgProt = enemyDefTemp / 100    
                            dmgOnEnemy = enemyDmgProt * playerAtk    
                            enemyVitTemp -= dmgOnEnemy
                            input (f'You deal {dmgOnEnemy} damage.')
                            input (f'The enemy has {enemyVitTemp}Hp remaining.')
                            
                            if enemyVitTemp <= 0:
                                input ('Sweet victory at last! All hail the glorious wall kitten!')   
                                
                                expGainedAfterCombat(2)

                                while playerExp > levelUpExp:
                                    levelUpExp = levelUpExp + levelUpExp
                        
                                break
                
                                
                playerDodgeChance = playerSpdTemp / 200
                enemyHitChance = random.random ()

                if playerDodgeChance > enemyHitChance:
                    input ('You dodged the attack!')
                    
                elif playerDodgeChance < enemyHitChance:
                    
                    enemyAtk = enemyStrTemp + rollTheDice (50)        
                    input (f'The enemy attacks with {enemyAtk} damage!')
                    playerDmgProt = playerDefTemp / 100    
                    dmgOnPlayer = playerDmgProt * enemyAtk    
                    playerVitTemp -= dmgOnPlayer
                    input (f'The enemy deals {dmgOnPlayer} damage.')
                    input (f'You have {playerVitTemp}Hp remaining.')
                    
                    if playerVitTemp <= 0:
                        input ('You died, the wall kitten is mildy displeased.')
                        break
                    
                        
                elif playerDodgeChance == enemyHitChance:
                    
                    playerTieBreaker = random.random ()
                    enemyTieBreaker = random.random ()
                    
                    # just in case they actually roll the same number again >.>        
                    while enemyTieBreaker == playerTieBreaker:
                            
                            playerTieBreaker = random.random ()
                            enemyTieBreaker = random.random ()
                        
                        # if the enemy wins the tie breaker, they start. otherwise nothing happens and player starts by default
                    if enemyTieBreaker > playerTieBreaker:
                        
                        enemyAtk = enemyStrTemp + rollTheDice (50)    
                        input (f'The enemy attacks with {enemyAtk} damage!')
                        playerDmgProt = playerDefTemp / 100    
                        dmgOnPlayer = playerDmgProt * enemyAtk    
                        playerVitTemp -= dmgOnPlayer
                        input (f'The enemy deals {dmgOnPlayer} damage.')
                        input (f'You have {playerVitTemp}Hp remaining.')
                        
                        if playerVitTemp <= 0:
                            input ('You died, the wall kitten is mildy displeased.')
                            break
                        

            elif playerChoice == 'defend':
                                
                playerDodgeChance = playerSpdTemp / 200
                enemyHitChance = random.random ()

                if playerDodgeChance > enemyHitChance:
                    input ('You dodged the attack!')
                    
                elif playerDodgeChance < enemyHitChance:
                    
                    enemyAtk = enemyStrTemp + rollTheDice (50)
                    input (f'The enemy attacks with {enemyAtk} damage!')
                    playerDmgProt = playerDefTemp / 100 
                    playerDmgProt = playerDmgProt * 2   
                    dmgOnPlayer = playerDmgProt * enemyAtk    
                    playerVitTemp -= dmgOnPlayer
                    input (f'The enemy deals {dmgOnPlayer} damage.')
                    input (f'You have {playerVitTemp}Hp remaining.')
                    
                    if playerVitTemp <= 0:
                        input ('You died, the wall kitten is mildy displeased.')
                        break
                    
                        
                elif playerDodgeChance == enemyHitChance:
                    
                    playerTieBreaker = random.random ()
                    enemyTieBreaker = random.random ()
                    
                    # just in case they actually roll the same number again >.>        
                    while enemyTieBreaker == playerTieBreaker:
                            
                            playerTieBreaker = random.random ()
                            enemyTieBreaker = random.random ()
                        
                        # if the enemy wins the tie breaker, they start. otherwise nothing happens and player starts by default
                    if enemyTieBreaker > playerTieBreaker:
                        
                        enemyAtk = enemyStrTemp + rollTheDice (50)
                        input (f'The enemy attacks with {enemyAtk} damage!')
                        playerDmgProt = playerDefTemp / 100 
                        playerDmgProt = playerDmgProt * 2   
                        dmgOnPlayer = playerDmgProt * enemyAtk    
                        playerVitTemp -= dmgOnPlayer
                        input (f'The enemy deals {dmgOnPlayer} damage.')
                        input (f'You have {playerVitTemp}Hp remaining.')
                        
                        if playerVitTemp <= 0:
                            input ('You died, the wall kitten is mildy displeased.')
                            break
            
            elif playerChoice == 'item':
                
                ###########
                ###########
                ###########
                ###########
                ###########
                
                playerDodgeChance = playerSpdTemp / 200
                enemyHitChance = random.random ()

                if playerDodgeChance > enemyHitChance:
                    input ('You dodged the attack!')
                    
                elif playerDodgeChance < enemyHitChance:
                    
                    enemyAtk = enemyStrTemp + rollTheDice (50)        
                    input (f'The enemy attacks with {enemyAtk} damage!')
                    playerDmgProt = playerDefTemp / 100    
                    dmgOnPlayer = playerDmgProt * enemyAtk    
                    playerVitTemp -= dmgOnPlayer
                    input (f'The enemy deals {dmgOnPlayer} damage.')
                    input (f'You have {playerVitTemp}Hp remaining.')
                    
                    if playerVitTemp <= 0:
                        input ('You died, the wall kitten is mildy displeased.')
                        break
                    
                        
                elif playerDodgeChance == enemyHitChance:
                    
                    playerTieBreaker = random.random ()
                    enemyTieBreaker = random.random ()
                    
                    # just in case they actually roll the same number again >.>        
                    while enemyTieBreaker == playerTieBreaker:
                            
                            playerTieBreaker = random.random ()
                            enemyTieBreaker = random.random ()
                        
                        # if the enemy wins the tie breaker, they start. otherwise nothing happens and player starts by default
                    if enemyTieBreaker > playerTieBreaker:
                        
                        enemyAtk = enemyStrTemp + rollTheDice (50)    
                        input (f'The enemy attacks with {enemyAtk} damage!')
                        playerDmgProt = playerDefTemp / 100    
                        dmgOnPlayer = playerDmgProt * enemyAtk    
                        playerVitTemp -= dmgOnPlayer                          
                        input (f'The enemy deals {dmgOnPlayer} damage.')
                        input (f'You have {playerVitTemp}Hp remaining.')    
                        
                        if playerVitTemp <= 0:
                            input ('You died, the wall kitten is mildy displeased.')
                            break
                
            elif playerChoice == 'talk':
                
                ##########
                ##########
                ##########
                ##########
                ##########    
                playerDodgeChance = playerSpdTemp / 200
                enemyHitChance = random.random ()

                if playerDodgeChance > enemyHitChance:
                    input ('You dodged the attack!')
                    
                elif playerDodgeChance < enemyHitChance:
                    
                    enemyAtk = enemyStrTemp + rollTheDice (50)        
                    input (f'The enemy attacks with {enemyAtk} damage!')
                    playerDmgProt = playerDefTemp / 100    
                    dmgOnPlayer = playerDmgProt * enemyAtk    
                    playerVitTemp -= dmgOnPlayer
                    input (f'The enemy deals {dmgOnPlayer} damage.')
                    input (f'You have {playerVitTemp}Hp remaining.')
                    
                    if playerVitTemp <= 0:
                        input ('You died, the wall kitten is mildy displeased.')
                        break
                    
                        
                elif playerDodgeChance == enemyHitChance:
                    
                    playerTieBreaker = random.random ()
                    enemyTieBreaker = random.random ()
                    
                    # just in case they actually roll the same number again >.>        
                    while enemyTieBreaker == playerTieBreaker:
                            
                            playerTieBreaker = random.random ()
                            enemyTieBreaker = random.random ()
                        
                        # if the enemy wins the tie breaker, they start. otherwise nothing happens and player starts by default
                    if enemyTieBreaker > playerTieBreaker:
                        
                        enemyAtk = enemyStrTemp + rollTheDice (50)    
                        input (f'The enemy attacks with {enemyAtk} damage!')
                        playerDmgProt = playerDefTemp / 100    
                        dmgOnPlayer = playerDmgProt * enemyAtk    
                        playerVitTemp -= dmgOnPlayer
                        input (f'The enemy deals {dmgOnPlayer} damage.')                            
                        input (f'You have {playerVitTemp}Hp remaining.')
                        
                        if playerVitTemp <= 0:
                            input ('You died, the wall kitten is mildy displeased.')
                            break
                

startCombat (playerVit, playerDef, playerStr, playerSpd, int (currentMob ['vit']), int (currentMob ['str']), int (currentMob ['def']), int (currentMob ['spd']))
                


# Class choice function
def chooseClass():
    global playerStr
    global playerInt
    global playerVit
    global playerDex
    global playerSpd
    global playerLuck
    global playerIns
    global playerDef
    global playerClass
    chooseClass = 0
    while chooseClass not in [1, 2, 3]:
        chooseClass = int(input("There are 3 classes. Archer, Warrior and Mage. Which one would you like to start your journey with? Type 1 for Archer, 2 for Warrior or 3 for Mage: "))
        if chooseClass == 1:
            playerStr = 5
            playerInt = 5
            playerVit = 10
            playerDex = 15
            playerSpd = 15
            playerLuck = 15
            playerIns = 5
            playerDef = 10
            playerClass = "Archer"
            print("You are an Archer!")
            break
        elif chooseClass == 2:
            playerStr = 15
            playerInt = 5
            playerVit = 15
            playerDex = 10
            playerSpd = 10
            playerLuck = 5
            playerIns = 5
            playerDef = 15
            playerClass = "Warrior"
            print("Your are a Warrior!")
            break
        else:
            playerStr = 5
            playerInt = 15
            playerVit = 10
            playerDex = 10
            playerSpd = 5
            playerLuck = 15
            playerIns = 15
            playerDef = 5
            playerClass = "Mage"
            print("You are a Mage!")
            break
            
    return playerStr, playerInt, playerVit, playerDex, playerSpd, playerLuck, playerIns, playerDef, playerClass


# Random mob encounter
def mobEncounter(tierChoice): # Insert a tier in the range of 1-4 as an argument
    mobID = 0
    mobID = random.randint(1, 5)
    if tierChoice == 1:
        if mobID == 1:
            mobID = tinyRaptor
        elif mobID == 2:
            mobID = caveSpider
        elif mobID == 3:
            mobID = grublingWorm
        elif mobID == 4:
            mobID = whiskerRat
        else:
            mobID = duskbatHatchling
    elif tierChoice == 2:
        if mobID == 1:
            mobID = squeakclawDrake
        elif mobID == 2:
            mobID = frostlingSprite 
        elif mobID == 3:
            mobID = twitchfangBat
        elif mobID == 4:
            mobID = feralGnat
        else:
            mobID = pufftailRabbit
    elif tierChoice == 3:
        if mobID == 1:
            mobID = emberjawDrake
        elif mobID == 2:
            mobID = vilewingHarpy
        elif mobID == 3:
            mobID = frostclawLynx
        elif mobID == 4:
            mobID = fierceRavanger
        else:
            mobID = blightrootTreant
    elif tierChoice == 4:
        if mobID == 1:
            mobID = stormBasilisk
        elif mobID == 2:
            mobID = shadowStalker
        elif mobID == 3:
            mobID== ironskinMinotaur
        elif mobID == 4:
            mobID = firefangHydra
        else:
            mobID = legendaryManticore

    return mobID


# Level up function
def levelUp(tempPlayerClass): # Insert "playerClass" variable as argument
    global playerLevel
    global playerStr
    global playerInt 
    global playerVit 
    global playerDex 
    global playerSpd 
    global playerIns 
    global playerDef 
    global playerLuck

    playerLevel += 1

    if tempPlayerClass == "Archer":
        playerStr += 1
        playerInt += 1
        playerVit += 1
        playerIns += 1
        playerDef += 1

        playerDex += 3
        playerSpd += 3
        playerLuck += 3


    elif tempPlayerClass == "Warrior":
        playerDex += 1
        playerInt += 1
        playerSpd += 1
        playerIns += 1
        playerLuck += 1

        playerStr += 3
        playerVit += 3
        playerDef += 3

    elif tempPlayerClass == "Mage":
        playerDex += 1
        playerSpd += 1
        playerStr += 1
        playerVit += 1
        playerDef += 1

        playerInt += 3
        playerIns += 3
        playerLuck += 3

    

    print(f"You leveled up! You are now level {playerLevel}")


    return playerLevel, playerStr, playerInt, playerVit, playerIns, playerDef, playerDex, playerSpd, playerLuck

def expGainedAfterCombat(tempMonsterTier): # Random Number of EXP based on monster tier
    global playerExp
    if tempMonsterTier == 1:
        playerExp += random.randint(5, 10)
    elif tempMonsterTier == 2:
        playerExp += random.randint(15, 25)
    elif tempMonsterTier ==  3:
        playerExp += random.randint(40, 50)
    elif tempMonsterTier == 4:
        playerExp += random.randint(70, 85)
    
    return playerExp      

# Chapter 1 function
def startChapter1():
    userChoice = 0

    print("NPC/Narator Text")

    chooseClass()

    print("NPC/Narator Text")

    print("1. Random battle encounter")
    print("2. Dialog option (Continue)")
    print("3. Dialog option (Continue)")
    print("4. Check your Level, Class and Stats")

    userChoice = int(input("Press 1 2 3 or 4 to Continue "))
    while userChoice == 1:
        startCombat()
        userChoice = int(input("Press 1 2 3 or 4 to Continue "))

        if userChoice == 2 or userChoice == 3:
            break

    while userChoice == 4:
        print(f"Your Level: {playerLevel}")
        print(f"Class: {playerClass}")
        print(f"Str: {playerStr}, Spd: {playerSpd}, Def: {playerDef}, Int: {playerInt}, Dex: {playerDex}, Ins: {playerIns}, Luck: {playerLuck}, Vit: {playerVit}")
      

        userChoice = int(input("Press 1 2 3 or 4 to Continue "))
        if userChoice == 2 or userChoice == 3:
            break

        




#Test Area

"""chooseClass()
print(playerClass)
levelUp(playerClass)
print(f"Str: {playerStr}, Spd: {playerSpd}, Def: {playerDef}, Int: {playerInt}, Dex: {playerDex}, Ins: {playerIns}, Luck: {playerLuck}, Vit: {playerVit}")
levelUp(playerClass)
print(f"Str: {playerStr}, Spd: {playerSpd}, Def: {playerDef}, Int: {playerInt}, Dex: {playerDex}, Ins: {playerIns}, Luck: {playerLuck}, Vit: {playerVit}")
levelUp(playerClass)
print(f"Str: {playerStr}, Spd: {playerSpd}, Def: {playerDef}, Int: {playerInt}, Dex: {playerDex}, Ins: {playerIns}, Luck: {playerLuck}, Vit: {playerVit}")"""

#to do´s
<<<<<<< HEAD
#Function to track exp = > pass to combat function = > 
=======
#Function to track exp = > pass to combat function = > 



startChapter1()

>>>>>>> fbe56cfb05587547422aa7b7efb12496486aecae
