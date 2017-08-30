import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 205)

display_width = 1100
display_height = 600

lottery_width = 250
lottery_height = 200
lottery_price = 20

# buttons
okay_button = pygame.image.load('image/okay_button.png')
start_button = pygame.image.load('image/start_button.png')
about_button = pygame.image.load('image/about_button.png')
about_description = pygame.image.load('image/about_description.png')
title_image = pygame.image.load('image/title.png')
accept_button = pygame.image.load('image/accept.png')
credit_button = pygame.image.load('image/credit.png')

buy_button = pygame.image.load('image/buy_button.png')
sell_button = pygame.image.load('image/sell_button.png')
next_button = pygame.image.load('image/next_button.png')
lottery_button = pygame.image.load('image/lottery.png')
lottery_popUp = pygame.image.load('image/lottery_popUp.png')

# shrimp image
crs_shrimp = pygame.image.load('image/crystalRedShrimp.png')
cbs_shrimp = pygame.image.load('image/crystalBlackShrimp.png')
bkk_shrimp = pygame.image.load('image/blackKingKong.png')
rw_shrimp = pygame.image.load('image/redWine.png')
blueBolt_shrimp = pygame.image.load('image/blueBolt.png')
tiger_shrimp = pygame.image.load('image/tiger.png')
shadowPanda_shrimp = pygame.image.load('image/shadowPanda.png')
oebt_shrimp = pygame.image.load('image/oebt.png')
redPinto_shrimp = pygame.image.load('image/redPinto.png')
hidden_shrimp = pygame.image.load('image/hiddenShrimp.png')

#nitialize game display
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Shrimp Simulator')
font = pygame.font.SysFont(None, 25)
clock = pygame.time.Clock()

FPS = 30
maxPopulation = 150

pregnancyWaitPeriod = 3
crs_price = 5
cbs_price = 4
rw_price = 15
bkk_price = 11

# Reading text file
numLines = sum(1 for line in open('trivia.txt'))
f=open('trivia.txt')
lines=f.readlines()

# super class
class Shrimp:
    __Shrimp = []
    __isMale = False
    __age = 0
    __isPregnant = False
    __isAlive = True
    __pregnancyPeriod = 0

    def __init__(self, isMale, age):
        self.__isMale = isMale
        self.__age = age

    def increasePregnancyPeriod(self):
        self.__pregnancyPeriod += 1

    def setPregnancyPeriod(self, num):
        self.__pregnancyPeriod = 0

    def getPregnancyPeriod(self):
        return self.__pregnancyPeriod

    def increaseAge(self):
        self.__age += 1

    def getAge(self):
        return self.__age

    def isMale(self):
        return self.__isMale

    def isPregnant(self):
        if self.__isPregnant == True:
            return True
        else:
            return False

    def setPregnant(self, truth):
        self.__isPregnant = truth

    def getBaby(self):
        return self.__Shrimp

    def addBaby(self, shrimp):
        self.__Shrimp.append(shrimp)

    def clearBaby(self):
        del self.__Shrimp[:]

### subclasses
class CrystalRedShrimp(Shrimp):
    __fitness = 0
    colorGene1 = "R"
    colorGene2 = "R"
    tbGene1 = "N"
    tbGene2 = "N"

    def __init__(self, isMale, age):
        self.__fitness = 30
        super(CrystalRedShrimp, self).__init__(isMale, age)

    def getFitness(self):
        return self.__fitness

    def decreaseFitness(self):
        self.__fitness -= random.randint(7, 10)

class CrystalBlackShrimp(Shrimp):
    __fitness = 0
    colorGene1 = "B"
    colorGene2 = "B"
    tbGene1 = "N"
    tbGene2 = "N"

    def __init__(self, isMale, age):
        self.__fitness = 40
        super(CrystalBlackShrimp, self).__init__(isMale, age)

    def getFitness(self):
        return self.__fitness

    def decreaseFitness(self):
        random.randint(6, 8)
        self.__fitness -= random.randint(6, 10)

class BlackKingKongShrimp(Shrimp):
    __fitness = 50
    colorGene1 = "B"
    colorGene2 = "B"
    tbGene1 = "Y"
    tbGene2 = "Y"

    def __init__(self, isMale, age):
        self.__fitness = 30
        super(BlackKingKongShrimp, self).__init__(isMale, age)

    def getFitness(self):
        return self.__fitness

    def decreaseFitness(self):
        self.__fitness -= random.randint(7, 15)

class RedWineShrimp(Shrimp):
    __fitness = 50
    colorGene1 = "R"
    colorGene2 = "R"
    tbGene1 = "Y"
    tbGene2 = "Y"

    def __init__(self, isMale, age):
        self.__fitness = 40
        super(RedWineShrimp, self).__init__(isMale, age)

    def getFitness(self):
        return self.__fitness

    def decreaseFitness(self):
        self.__fitness -= random.randint(6, 11)

def message_to_screen(msg, color, x_coord, y_coord, fontSize):
    font = pygame.font.SysFont("comicsansms", fontSize)
    screen_text = font.render(msg, True, color)
    text_rect_coord = screen_text.get_rect(center=(x_coord, y_coord))
    gameDisplay.blit(screen_text, text_rect_coord)

def sexDeterminator():
    value = random.randint(0, 1)
    if value == 0:
        return True
    else:
        return False

def try_buy(totalMoney, price):
    temp_money = totalMoney
    if temp_money >= price:
        totalMoney -= price
        return True
    else:
        return False

def try_sell(list):
    temp_list = list
    list_length = len(temp_list)
    if (list_length <= 0):
        failList = []
        return failList

    # if a shrimp is berried(pregnant), it will not be sold unless there is nothing else to sell
    # or else whichever (male/female) has more number is sold first
    # for each sex, the one with oldest is sold
    maleCounter = 0
    maleMaxAge = 0
    femaleCounter = 0
    femaleMaxAge = 0
    pregnantCounter = 0
    pregnantMaxAge = 0

    for x in temp_list:
        if x.isPregnant() == True:
            pregnantCounter += 1
            if x.getAge() > pregnantMaxAge:
                pregnantMaxAge = x.getAge()
        elif x.isMale():
            maleCounter += 1
            if x.getAge() > maleMaxAge:
                maleMaxAge = x.getAge()
        else:
            femaleCounter += 1
            if x.getAge() > femaleMaxAge:
                femaleMaxAge = x.getAge()

    usage = 0  # 1 --> sell Pregant   2 -->sell male  3-->sell female
    # if only pregnant one is available to sell
    if maleCounter == 0 and femaleCounter == 0 and pregnantCounter > 0:
        usage = 1
    elif maleCounter > femaleCounter:
        usage = 2
    else:
        usage = 3
    for x in temp_list:
        if usage == 1:
            if x.isPregnant() == True and x.getAge() == pregnantMaxAge:
                temp_list.remove(x)
                return temp_list
        if usage == 2:
            if x.isMale() == True and x.getAge() == maleMaxAge:
                temp_list.remove(x)
                return temp_list
        if usage == 3:
            if x.isMale() != True and x.getAge() == femaleMaxAge and x.isPregnant() == False:
                temp_list.remove(x)
                return temp_list
    return temp_list

def startScreen():
    intro = True
    while intro is True:
        gameDisplay.fill(white)
        message_to_screen("Shrimp Simulator", red, display_width / 2, display_height / 10, 25)
        start_button_display = gameDisplay.blit(start_button, (300, 420))
        about_button_display = gameDisplay.blit(about_button, (500, 420))
        title_image_display = gameDisplay.blit(title_image, (100,20))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                intro = False
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_display.collidepoint(pygame.mouse.get_pos()):
                    intro = False
                if about_button_display.collidepoint(pygame.mouse.get_pos()):
                    aboutScreen()

        pygame.display.update()

def aboutScreen():

    aboutScreen = True

    while aboutScreen is True:
        gameDisplay.fill(white)
        message_to_screen("About", black, display_width / 2, display_height / 10, 25)
        gameDisplay.blit(about_description, (200, 100))
        ok_button_display = gameDisplay.blit(okay_button, (400, 460))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                intro = False
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ok_button_display.collidepoint(pygame.mouse.get_pos()):
                    aboutScreen = False

        pygame.display.update()

def updateShrimp(crs, cbs, bkk, rw, bb):
    tempPopulationSize = 0
    maleList = []
    maleListLength = 0
    allShrimp = []
    allShrimp.append(crs)
    allShrimp.append(cbs)
    allShrimp.append(bkk)
    allShrimp.append(rw)
    allShrimp.append(bb)

    for x in range(0, len(allShrimp)):
        for y in allShrimp[x]:
            tempPopulationSize += 1
    # initial loop to:
    # 1. increase age, decrease fitness
    # 2. death from fitness
    # 3. if pregnant, increase pregnancy, if ready, give birth
    # 4. if male, should put it into mating pool
    for x in range(0, len(allShrimp)):
        for y in allShrimp[x]:
            # print("getting baby"+ str(y.getBaby()))
            y.increaseAge()
            y.decreaseFitness()
            if y.getFitness() < 0:  # shrimp deaths
                allShrimp[x].remove(y)

            if y.isMale() == False:
                if y.isPregnant():
                    y.increasePregnancyPeriod()
                    if y.getPregnancyPeriod() > 3:
                        for z in y.getBaby():
                            babyClassName = z.__class__.__name__
                            if tempPopulationSize < maxPopulation:
                                if babyClassName == "CrystalRedShrimp":
                                    allShrimp[0].append(z)
                                    tempPopulationSize += 1
                                elif babyClassName == "CrystalBlackShrimp":
                                    allShrimp[1].append(z)
                                    tempPopulationSize += 1
                                elif babyClassName == "BlackKingKongShrimp":
                                    allShrimp[2].append(z)
                                    tempPopulationSize += 1
                                elif babyClassName == "RedWineShrimp":
                                    allShrimp[3].append(z)
                                    tempPopulationSize += 1
                        y.clearBaby()
                        y.setPregnant(False)
                        y.setPregnancyPeriod(0)

            elif y.isMale() == True:
                maleList.append(y)

    # search for female, then do the mating
    '''
    genetic assumptions:
       - diploid model
       - black is dominant, red is recessive
       - taiwan bee gene(red wine, panda, etc) is recessive, Crystal gene is dominant
       - sexual reproduction: receives 1 copy of gene from a single parents at random 
    '''
    # filtered list of allShrimp of deaths, births
    maleListLength = len(maleList);
    luckyMaleNumber = 0
    if maleListLength != 0:
        luckyMaleNumber = random.randint(0, maleListLength - 1)

    for x in range(0, len(allShrimp)):
        for y in allShrimp[x]:
            if y.isMale() == False:
                if y.isPregnant() == False and maleListLength > 0:

                    firstMomColor = y.colorGene1
                    secondMomColor = y.colorGene2
                    firstMomTb = y.tbGene1
                    secondMomTb = y.tbGene2

                    luckyMale = maleList[luckyMaleNumber]
                    firstDadColor = luckyMale.colorGene1
                    secondDadColor = luckyMale.colorGene2
                    firstDadTb = luckyMale.tbGene1
                    secondDadTb = luckyMale.tbGene2

                    numBabies = random.randint(3, 6)
                    for eachBaby in range(0, numBabies):
                        firstBabyColor = 'N'
                        secondBabyColor = 'N'
                        firstBabyTb = 'N'
                        secondBabyTb = 'N'

                        # 0 is mom , 1 is dad
                        colorGene1RNG = random.randint(0, 1)
                        colorGene2RNG = random.randint(0, 1)
                        tbGene1RNG = random.randint(0, 1)
                        tbGene2RNG = random.randint(0, 1)

                        if colorGene1RNG == 0:
                            firstBabyColor = firstMomColor
                        else:
                            firstBabyColor = firstDadColor
                        if colorGene2RNG == 0:
                            secondBabyColor = secondMomColor
                        else:
                            secondBabyColor = secondDadColor
                        if tbGene1RNG == 0:
                            firstBabyTb = firstMomTb
                        else:
                            firstBabyTb = firstDadTb
                        if tbGene2RNG == 0:
                            secondBabyTb = secondMomTb
                        else:
                            secondBabyTb = secondDadTb

                        # now determine what kind of shrimp this is
                        isCrystal = False
                        isRed = False

                        if firstBabyColor == 'R' and secondBabyColor == 'R':
                            isRed = True
                        else:
                            isRed = False

                        if firstBabyTb == 'Y' and secondBabyTb == 'Y':
                            isCrystal = False
                        else:
                            isCrystal = True

                        newShrimp = None
                        if isCrystal == True and isRed == True:
                            if colorGene1RNG == 0:
                                newShrimp = CrystalRedShrimp(True, 0)
                            else:
                                newShrimp = CrystalRedShrimp(False, 0)

                        if isCrystal == True and isRed == False:
                            if colorGene1RNG == 0:
                                newShrimp = CrystalBlackShrimp(True, 0)
                            else:
                                newShrimp = CrystalBlackShrimp(False, 0)

                        if isCrystal == False and isRed == True:
                            if colorGene1RNG == 0:
                                newShrimp = RedWineShrimp(True, 0)
                            else:
                                newShrimp = RedWineShrimp(False, 0)

                        if isCrystal == False and isRed == False:
                            if colorGene1RNG == 0:
                                newShrimp = BlackKingKongShrimp(True, 0)
                            else:
                                newShrimp = BlackKingKongShrimp(False, 0)

                        newShrimp.colorGene1 = firstBabyColor
                        newShrimp.colorGene2 = secondBabyColor
                        newShrimp.tbGene1 = firstBabyTb
                        newShrimp.tbGene2 = secondBabyTb
                        y.setPregnant(True)
                        y.addBaby(newShrimp)

def updateTrivia(trivia):
    # read random lines from trivia.txt.
    randomNum = random.randint(0, numLines)
    return lines[randomNum-1]

def gameLoop():
    crs_list = []
    cbs_list = []
    rw_list = []
    bkk_list = []
    bolt_list = [] # not used anymore

    tiger_unlocked = False
    tigerNum = 0
    blueBolt_unlocked = False
    blueBoltNum =0
    shadowPanda_unlocked = False
    shadowPandaNum = 0
    redPinto_unlocked = False
    redPintoNum = 0
    oebt_unlocked = False
    oebtNum=0

    trivia = "New Shrimp Trivia Every Month"

    # crs1 = CrystalRedShrimp(True, 4)
    crs2 = CrystalRedShrimp(False, 5)
    crs2.addBaby(CrystalRedShrimp(False, 0))
    crs2.addBaby(CrystalRedShrimp(True, 0))
    crs2.setPregnant(True)

    crs_list.append(crs2)

    money = 125;
    month = 0;
    gameExit = False
    gameOver = False

    while not gameExit:

        # Event handling of each buttons
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    j = 0
            if event.type == pygame.MOUSEBUTTONDOWN:

                if next_button_display.collidepoint(pygame.mouse.get_pos()):
                    month += 1
                    updateShrimp(crs_list, cbs_list, bkk_list, rw_list, bolt_list)
                    trivia = updateTrivia(trivia)

                if crs_buy_display.collidepoint(pygame.mouse.get_pos()):
                    if try_buy(money, crs_price):
                        crs_list.append(CrystalRedShrimp(sexDeterminator(), 2))
                        money -= crs_price
                if crs_sell_display.collidepoint(pygame.mouse.get_pos()):
                    crsLen = len(crs_list)
                    temp_list = try_sell(crs_list)
                    if len(temp_list) != 0:
                        money += crs_price
                    if crsLen == 1 and len(temp_list) == 0:  # for selling last ne
                        money += crs_price
                if cbs_buy_display.collidepoint(pygame.mouse.get_pos()):
                    if try_buy(money, cbs_price):
                        cbs_list.append(CrystalBlackShrimp(sexDeterminator(), 2))
                        money -= cbs_price
                if cbs_sell_display.collidepoint(pygame.mouse.get_pos()):
                    cbsLen = len(cbs_list)
                    temp_list = try_sell(cbs_list)
                    if (len(temp_list) != 0):
                        money += cbs_price
                    if (cbsLen == 1 and len(temp_list) == 0):  # for selling last ne
                        money += cbs_price
                if bkk_buy_display.collidepoint(pygame.mouse.get_pos()):
                    if try_buy(money, bkk_price):
                        money -= bkk_price
                        bkk_list.append(BlackKingKongShrimp(sexDeterminator(), 2))
                if bkk_sell_display.collidepoint(pygame.mouse.get_pos()):
                    bkkLen = len(bkk_list)
                    temp_list = try_sell(bkk_list)
                    if len(temp_list) != 0:
                        money += bkk_price
                    if bkkLen == 1 and len(temp_list) == 0:  # for selling last ne
                        money += bkk_price
                if rw_buy_display.collidepoint(pygame.mouse.get_pos()):
                    if try_buy(money, rw_price):
                        money -= rw_price
                        rw_list.append(RedWineShrimp(sexDeterminator(), 2))
                if rw_sell_display.collidepoint(pygame.mouse.get_pos()):
                    rwLen = len(rw_list)
                    temp_list = try_sell(rw_list)
                    if len(temp_list) != 0:
                        money += rw_price
                    if rwLen == 1 and len(temp_list) == 0:  # for selling last ne
                        money += rw_price
                if lottery_display.collidepoint(pygame.mouse.get_pos()):
                     if money>=lottery_price:
                        money -= lottery_price
                        enableLotteryScreen = True

                        creditAmount = 0
                        CRS_credit = 5
                        CBS_credit = 4
                        tiger_credit = 10
                        blueBolt_credit = 15
                        shadowPanda_credit = 25
                        oebt_credit = 40
                        redPinto_credit = 50

                        crs_striing = "CRS"
                        cbs_string = "CBS"
                        tiger_string = "tiger"
                        blueBolt_string = "blueBolt"
                        shadowPanda_string = "shadowPanda"
                        oebt_string = "oebt"
                        redPinto_string = "redPinto"

                        numberPick = random.randint(0, 99)
                        print(numberPick)
                        winner = "CRS"

                        if numberPick > 0 and numberPick <= 20:
                            winner = crs_striing
                            creditAmount = CRS_credit
                        if numberPick > 20 and numberPick <= 40:
                            winner = cbs_string
                            creditAmount = CBS_credit
                        if numberPick > 40 and numberPick <= 60:
                            winner = tiger_string
                            creditAmount = tiger_credit
                        if numberPick > 60 and numberPick <= 70:
                            winner = blueBolt_string
                            creditAmount = blueBolt_credit
                        if numberPick > 70 and numberPick <= 80:
                            if blueBolt_unlocked == True:
                                winner = shadowPanda_string
                                creditAmount = shadowPanda_credit
                            else:
                                winner = blueBolt_string
                                creditAmount = blueBolt_credit
                        if numberPick > 80 and numberPick <= 90:
                            if tiger_unlocked == True:
                                winner = oebt_string
                                creditAmount = oebt_credit
                            else:
                                winner = "tiger"
                                creditAmount = tiger_credit
                        if numberPick > 90 and numberPick <= 99:
                            if len(rw_list) > 0 and tiger_unlocked == True:
                                winner = redPinto_string
                                creditAmount = redPinto_credit
                            else:
                                winner = tiger_string
                                creditAmount = tiger_credit

                        while enableLotteryScreen:
                             for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if creditBlit.collidepoint(pygame.mouse.get_pos()):
                                        money += creditAmount
                                        enableLotteryScreen = False
                                    if acceptBlit.collidepoint(pygame.mouse.get_pos()):
                                        if winner == crs_striing:
                                            crs_list.append(CrystalRedShrimp(sexDeterminator(),2))
                                        if winner == cbs_string:
                                            cbs_list.append(CrystalBlackShrimp(sexDeterminator(), 2))
                                        if winner == tiger_string:
                                            tiger_unlocked = True
                                            tigerNum += 1
                                        if winner == blueBolt_string:
                                            blueBolt_unlocked = True

                                            blueBoltNum += 1
                                        if winner == shadowPanda_string:
                                            shadowPanda_unlocked=True
                                            shadowPandaNum += 1
                                        if winner == oebt_string:
                                            oebt_unlocked = True
                                            oebtNum += 1
                                        if winner == redPinto_string:
                                            redPinto_unlocked = True
                                            redPintoNum += 1
                                        enableLotteryScreen= False

                             gameDisplay.blit(lottery_popUp, (lottery_width, lottery_height))

                             message_to_screen("You have won the following shrimp!:  " + winner +" ($ "+ str(creditAmount)+ ")",
                                               black, lottery_width+270, lottery_height+50, 22 )

                             message_to_screen("Hint: unlock(accept) to win new hidden one in the future!",
                                               red,lottery_width+200, lottery_height+75, 12)
                             whichImageToLoad = None

                             if winner == crs_striing:
                                 whichImageToLoad = crs_shrimp
                             if winner == cbs_string:
                                 whichImageToLoad = cbs_shrimp
                             if winner == blueBolt_string:
                                 whichImageToLoad = blueBolt_shrimp
                             if winner == tiger_string:
                                 whichImageToLoad = tiger_shrimp
                             if winner == oebt_string:
                                 whichImageToLoad = oebt_shrimp
                             if winner == shadowPanda_string:
                                 whichImageToLoad = shadowPanda_shrimp
                             if winner == redPinto_string:
                                 whichImageToLoad = redPinto_shrimp

                             shrimpPic = gameDisplay.blit(whichImageToLoad, (lottery_width+200, lottery_height+100))
                             acceptBlit = gameDisplay.blit(accept_button, (lottery_width+150, lottery_height+210))
                             creditBlit = gameDisplay.blit(credit_button, (lottery_width + 300, lottery_height+ 210))
                             pygame.event.pump()
                             pygame.display.update()

        gameDisplay.fill(white)

        message_to_screen("Shop", black, 300, 60, 33)
        next_button_display = gameDisplay.blit(next_button, (400, 15))

        money_string = "$ " + str(money)
        if money > 20:
            message_to_screen(money_string, black, 50, 20, 25)
        else:
            message_to_screen(money_string, red, 50, 20, 25)

        month_string = "Month: " + str(month)
        message_to_screen(month_string, black, 300, 20, 25)

        # Crystal Red Shrimp
        crs_display = gameDisplay.blit(crs_shrimp, (50, 100))
        message_to_screen("Crystal Red Shrimp: $5", black, 150, 160, 15)

        crs_buy = buy_button
        crs_sell = sell_button
        crs_buy_display = gameDisplay.blit(crs_buy, (150, 100))
        crs_sell_display = gameDisplay.blit(crs_sell, (150, 125))

        # Crystal Black Shrimp
        cbs_display = gameDisplay.blit(cbs_shrimp, (50, 200))
        message_to_screen("Crystal Black Shrimp: $4", black, 150, 260, 15)
        cbs_buy = buy_button
        cbs_sell = sell_button
        cbs_buy_display = gameDisplay.blit(cbs_buy, (150, 200))
        cbs_sell_display = gameDisplay.blit(cbs_sell, (150, 225))

        # Red Wine Shrimp
        rw_display = gameDisplay.blit(rw_shrimp, (300, 100))
        message_to_screen("Red Wine Shrimp: $15", black, 390, 160, 15)
        rw_buy = buy_button
        rw_sell = sell_button
        rw_buy_display = gameDisplay.blit(rw_buy, (410, 100))
        rw_sell_display = gameDisplay.blit(rw_sell, (410, 125))

        # Black King Kong Shrimp
        bkk_display = gameDisplay.blit(bkk_shrimp, (300, 200))
        message_to_screen("Black King Kong Shrimp: $11", black, 390, 260, 15)
        bkk_buy = buy_button
        bkk_sell = sell_button
        bkk_buy_display = gameDisplay.blit(cbs_buy, (410, 200))
        bkk_sell_display = gameDisplay.blit(cbs_sell, (410, 225))

        #lottery button
        lottery_display = gameDisplay.blit(lottery_button, (500, 120))
        message_to_screen("Lottery(can unlock rare) $20", black, 600, 250, 15)

        # Trivia Button
        message_to_screen("Did you know...?", black, 900, 50, 21)
        message_to_screen(trivia, blue, 900, 80, 20)

        # inventory
        message_to_screen("Inventory", black, 300, 300, 33)
        gameDisplay.blit(crs_shrimp, (50, 300))
        message_to_screen("Numbers:" + str(len(crs_list)), black, 200, 340, 15)
        gameDisplay.blit(cbs_shrimp, (50, 350))
        message_to_screen("Numbers:" + str(len(cbs_list)), black, 200, 390, 15)
        gameDisplay.blit(rw_shrimp, (50, 400))
        message_to_screen("Numbers:" + str(len(rw_list)), black, 200, 440, 15)
        gameDisplay.blit(bkk_shrimp, (50, 450))
        message_to_screen("Numbers:" + str(len(bkk_list)), black, 200, 490, 15)

        #hidden
        if tiger_unlocked== False:
            gameDisplay.blit(hidden_shrimp, (400, 300))
        else:
            gameDisplay.blit(tiger_shrimp, (400,300))
            message_to_screen("Tiger Shrimp", black, 550, 320, 15)
            message_to_screen("Numbers:" + str(tigerNum), black, 550, 340, 15)

        if blueBolt_unlocked == False:
            gameDisplay.blit(hidden_shrimp, (400, 350))
        else:
            gameDisplay.blit(blueBolt_shrimp, (400,350))
            message_to_screen("Blue Bolt Shrimp", black, 550, 370, 15)
            message_to_screen("Numbers:" + str(blueBoltNum), black, 550, 390, 15)

        if shadowPanda_unlocked ==False:
            gameDisplay.blit(hidden_shrimp, (400, 400))
        else:
            gameDisplay.blit(shadowPanda_shrimp, (400, 400))
            message_to_screen("Shadow Panda Shrimp", black, 550, 420, 15)
            message_to_screen("Numbers:" + str(shadowPandaNum), black, 550, 440, 15)

        if redPinto_unlocked ==False:
            gameDisplay.blit(hidden_shrimp, (400, 450))

        else:
            gameDisplay.blit(redPinto_shrimp, (400, 450))
            message_to_screen("Red Pinto Shrimp", black, 550, 470, 15)
            message_to_screen("Numbers:" + str(redPintoNum), black, 550, 490, 15)

        if oebt_unlocked ==False:
            gameDisplay.blit(hidden_shrimp, (400, 500))
        else:
            gameDisplay.blit(oebt_shrimp, (400, 500))
            message_to_screen("Orange Eye Blue Tiger", black, 550, 520, 15)
            message_to_screen("Numbers:" + str(oebtNum), black, 550, 540, 15)

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()

startScreen()
gameLoop()
