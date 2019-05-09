# You are welcome to write and include any other Python files you want or need
# however your game must be started by calling the main function in this file.

###########################################################################################
# Written by Karl Tomecek 9/18/2018                                                       #
# Program Name: adventure_game.py                                                         #
# Week 6 Assignment                                                                       #
# Comments:                                                                               #
#   Image of Mountain from:                                                               #
#   https://pixabay.com/en/mountains-hills-vector-graphics-1524804/                       #
#   Free for commercial use/No attribution required under                                 #
#   Creative Commons CC0                                                                  #
#                                                                                         #
#   Image of Player from:                                                                 #
#   https://openclipart.org/detail/15873/stickman                                         #
#   Per website: All Clipart are Released into the Public Domain.                         #
#                                                                                         #
#   Image of Rock from:                                                                   #
#   https://dayz.gamepedia.com/File:SmallStone.png                                        #
#   Http://creativecommons.org/licenses/by-nc-sa/3.0/                                     #
#                                                                                         #
#   Image of Electricity from:                                                            #
#   creepyhalloweenimages.com/free_halloween_photos/symbols/slides/lightning.htm          #
#                                                                                         #
#   Attribution 3.0 Unported (CC BY 3.0)                                                  #
#                                                                                         #
#   Image of Sawblade from:                                                               #
#   https://pixabay.com/en/saw-blade-old-circular-saw-2799995/                            #
#   CC0 Creative Commons                                                                  #
#                                                                                         #
#   Image of Cave from:                                                                   #
#   https://nl.wikipedia.org/wiki/Smoo_Cave#/media/File:Smoo_Cave_Waterfall,_Scotland.jpg #
#   (CC BY-SA 2.0)                                                                        #
###########################################################################################


import graphics as g
import random
import math
import ctypes
import time
import textwrap


#Classes
class Player:
   #Common base class for a player
   def __init__(self, name, health):
      self.name = name
      self.health = health
      self.superPowers = 0
               
##   def displayPlayerDetails(self):
##     print ('Name : ', self.name)
##     print ('Player Health: %d' % self.health)
##     print ('Player Wealth: %d\n' % self.wealth)


class Enemy:
   #Common base class for an enemy
    def __init__(self, name, health):
        self.name = name
        self.health = health
         
##    def displayEnemyDetails(self):
##        print ('Name : ', self.name)
##        print ('Enemy Health: %d\n' % self.health)
##     #print ('Enemy Special Power: %d' % self.wealth)



def displayDialog(win, text, pressAnyButton):
    if pressAnyButton:
        text += '        Press Any Button to continue --------------->'
    drawDialogBox(win)
    displayText(win,text, 12)
    buttonOptions = ['Any Button', 'Any Button', 'Any Button', 'Any Button', 'Any Button']
    if pressAnyButton:
        buttonClicked = checkForButtonClick(win,drawOptionButtons(win, buttonOptions))
    
def intro(win):
    text = 'Welcome to Karl\'s Adventure Game, or KAG for short!  You are about to embark on an exciting journey into the unknown...'
    displayDialog(win, text, True)
    text = 'You have 10 days to get to the secret cave at the end of the forest.  No one knows what is in that cave, but you are an amazing adventurer.'
    displayDialog(win, text, True)
    text = 'As you can tell by now, you have jumped out of a plane that flew you deep into an unknown valley.  So far everything is quiet...So far.'
    displayDialog(win, text, True)
    text = 'As you proceed through your adventure, make sure you collect things that will give you SUPER POWERS.  You never know what you might need as you venture deeper and deeper into the unknown!'
    displayDialog(win,text, True)
    text = 'Make sure you look at the stats bar on the bottom of the screen.  You don\'t want to get too low in health.'
    displayDialog(win,text, True)
    text = 'By the way, I forgot to ask you your name?  Type it in below, then press Any Button.  In the future, you will need to use the buttons, so by now you should be a pro.  Sorry...I got side tracked.  What is your name?'
    displayDialog(win,text, False)
    inputBox = g.Entry(g.Point(200,630),25)
    inputBox.draw(win)
    buttonClicked = checkForButtonClick(win,drawOptionButtons(win, ['Any Button', 'Any Button', 'Any Button', 'Any Button', 'Any Button']))
    playerName = inputBox.getText().strip() #trim leading and trailing spaces
    # if player leaves blank, give them a name
    if (not playerName):
        playerName = 'Player1'
    inputBox.undraw()
    return playerName

def displayText(win,text, fontSize): #	Split a text into a list of sentences.
    textList = textwrap.wrap(text,48) #got this info from https://docs.python.org/2/library/textwrap.html
    i = 0
    for line in textList:
        lineText = g.Text( g.Point( 190,515 + i ), line)
        lineText.setTextColor('white')
        lineText.setSize(fontSize)
        lineText.draw( win )
        i += 20
    
def clearScreen():
    for i in range(15): #clear the screen
        print('\n')

def drawDialogBox(win): #, buttons)
    dialog = g.Rectangle(g.Point(1,500), g.Point(498,678))
    dialog.setFill('black')
    dialog.setOutline('yellow')
    dialog.draw(win)

def clearDialog(win):
    for i in range(0,150):
        eraseLine = g.Line(g.Point(3,505 + i),g.Point(375, 505 + i))
        eraseLine.setWidth(1)
        eraseLine.setFill('black')
        eraseLine.draw(win)
        
def drawOptionButtons(win, buttonOptions):
    buttonCoordinates = []
    for i in range(0,5):
        spacer = i * 30
        coordinates = [380, 510 + spacer, 495, 530 + spacer]
        buttonCoordinates.append(coordinates) 
        button = g.Rectangle(g.Point(coordinates[0],coordinates[1]), g.Point(coordinates[2], coordinates[3]))
        button.setFill('white')
        button.setOutline('blue')
        button.setWidth(3)
        button.draw(win)
        # now place text in button
        label = g.Text(g.Point(435,520 + spacer), buttonOptions[i])
        label.setTextColor('black')
        label.setSize(8) # has range of 5 - 36
        label.setFace('courier') # can be "helvetica", "courier", "times roman",  "arial"
        label.setStyle('bold')
        label.draw(win)
    return buttonCoordinates

def simulateButtonClick(win, buttonIndex):
    spacer = buttonIndex * 30
    coordinates = [380, 510 + spacer, 495, 530 + spacer]
    button = g.Rectangle(g.Point(380,510 + spacer), g.Point(495, 530 + spacer))
    button.setFill('gray')
    button.setOutline('white')
    button.setWidth(3)
    button.draw(win)
    time.sleep(.05)
    button.undraw()
    
def displayStats(win, player, monster, dayNumb, monsterIndex):
    #Clear the stat Bar
    for i in range(0,19):
        eraseLine = g.Line(g.Point(2,657 + i),g.Point(497, 657 + i))
        eraseLine.setWidth(1)
        eraseLine.setFill('black')
        eraseLine.draw(win)
    playerStatsBar = g.Text(g.Point(win.getWidth()/2,660), 'Player: {0}  Health: {1}  Super Powers: {2}%  Day: {3}'.format(player.name, player.health, player.superPowers, dayNumb))
    playerStatsBar.setTextColor('white')
    playerStatsBar.setSize(8) # has range of 5 - 36
    playerStatsBar.setFace('courier') # can be "helvetica", "courier", "times roman",  "arial"
    playerStatsBar.setStyle('bold')
    playerStatsBar.draw(win)
    if (monsterIndex > -1):
        for i in range(0,73): # Clear the text for new text
            eraseLine = g.Line(g.Point(100,425 + i),g.Point(497, 425 + i))
            eraseLine.setWidth(1)
            eraseLine.setFill('orange')
            eraseLine.draw(win)
        if (monster.health <= 0):
            enemyStatsBar = g.Text(g.Point(win.getWidth()/2 + 30,465), 'You killed {0}!!!'.format(monster.name))
        else:
            enemyStatsBar = g.Text(g.Point(win.getWidth()/2 + 30,465), 'Monster: {0}  Health: {1}'.format(monster.name, monster.health, dayNumb))
        enemyStatsBar.setTextColor('red')
        enemyStatsBar.setSize(14) # has range of 5 - 36
        enemyStatsBar.setFace('courier') # can be "helvetica", "courier", "times roman",  "arial"
        enemyStatsBar.setStyle('bold')
        enemyStatsBar.draw(win)
    
def checkForButtonClick(win, buttonCoordinates):
    clicked = False
    while not clicked:
        coordinate = win.checkMouse()
        if coordinate:
            mouseX = int(coordinate.getX())
            mouseY = int(coordinate.getY())
            for buttonIndex, items in enumerate(buttonCoordinates): #learned about enumerate here:  http://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
                if (mouseX >= items[0] and mouseX <= items[2] and mouseY >= items[1] and mouseY <= items[3]):
                    #print ('Button {} Clicked!'.format(buttonIndex))
                    simulateButtonClick(win,buttonIndex)
                    clicked = True
                    break
    return buttonIndex                        

def nextScreen(win, backImage, playerImage):
    for i in range(350): #used to be 400
        backImage.move(-1,0)
        if (i % 2 == 0):
            playerImage.move(0,-4)
        else:
            playerImage.move(0,4)
        time.sleep(.005)
    for i in range(0,73): # Clear the monster status
        eraseLine = g.Line(g.Point(100,425 + i),g.Point(497, 425 + i))
        eraseLine.setWidth(1)
        eraseLine.setFill('white')
        eraseLine.draw(win)
    if win.checkMouse(): # this is used to eliminate extra unwanted clicks while screen updates
        clearMouseBuffer = win.checkMouse()
    
def showScreen(win):
    mountainImage = g.Image(g.Point(650,-30),'longmountains.gif')
    mountainImage.draw(win)
    return mountainImage
    
def setToneForDay():
    #pick a random theme
    theme = random.randint(0,3)
    if theme == 0:
        text = 'It\'s a sunny day.  The air is fresh and you feel energetic!!!'
        energy = 100
        visibility = 100
    elif theme == 1:
        text = 'Today is raining.  You feel gloomy.  Is that foretelling?'
        energy = 75
        visibility = 50
    elif theme == 2:
        text = 'There is a gentle snow falling.  You feel cold and sluggish.'
        energy = 25
        visibility = 75
    else:
        text = 'It\'s foggy out today.  You hope you can see where you are going!'
        energy = 75
        visibility = 25
    return [text, energy, visibility]

def checkForPowerup():
    #pick a random power up
    pUp = random.randint(0,4)
    if pUp == 0:
        text = '  You look around on the floor, but you don\'t see anything very interesting.'
        powerUp = 0
    elif pUp == 1:
        text = '  Wow, you found an energy drink!  You drink it and feel ready to go!!!'
        powerUp = 100
    elif pUp == 2:
        text = '  That\'s so weird, you find a Happy Meal...it gives you a little boost.'
        powerUp = 25
    elif pUp == 3:
        text = '  There are Bubba Berries here.  You eat a few and get diarrhea.  Yuck!'
        powerUp = -10
    else:
        text = '  You spot some mushrooms and eat them.  You sl acerrc erclelrcerce. Ekfldsds.'
        powerUp = -30
    return [text, powerUp]

def checkForEnemy(monsters):
    #pick a random enemy, or if you are lucky, none
    pickEnemy = random.randint(0,10) # by select 10 chances, you have a chance of having an enemy free day...so you hope
    if pickEnemy == 0 and monsters[0].health > 0:
        text = '  Rockzilla is here and he wants to crush you!!!'
        enemyNum = 0
    elif pickEnemy == 1 and monsters[1].health > 0:
        text = '  Zaptron is here and she wants to electrocute you!!!'
        enemyNum = 1
    elif pickEnemy == 2 and monsters[2].health > 0:
        text = '  Cutter is here and wants to slice you like a pizza!!!'
        enemyNum = 2
    elif pickEnemy == 3:
        text = '  There are lot\'s of Butterflies here.'
        enemyNum = -1
    elif pickEnemy == 4:
        text = '  Life just can\'t get any better.'
        enemyNum = -1
    elif pickEnemy == 5:
        text = '  I wonder what I will have for dinner tomorrow?'
        enemyNum = -1
    elif pickEnemy == 6:
        text = '  I feel lonely.'
        enemyNum = -1
    elif pickEnemy == 7:
        text = '  It is awefully quiet here...'
        enemyNum = -1
    elif pickEnemy == 8:
        text = '  Hope I am going in the right direction!'
        enemyNum = -1
    elif pickEnemy == 9:
        text = '  Looks like the coast is clear!'
        enemyNum = -1
    else:
        text = '  Hmmmmm.'
        enemyNum = -1
    return [text, enemyNum]
    
def main():
    clearScreen()
    win = g.GraphWin('Karl\'s Adventure Game', 500,680) # create a screen to draw on
    win.setBackground('white')
    playerImage = g.Image(g.Point(50,460),'player.gif')
    playerImage.draw(win)
    backImage = showScreen(win)
    #define Objects
    monsters = [Enemy('Rockzilla', 100), Enemy('Zaptron', 100), Enemy('Cutter',100)]
    player1 = Player(intro(win), 100)
    dayNumber = 10 #Start the game
    dead = False
    while (dayNumber > 0):
        clearDialog(win)

        #Set the tone for the day #######
        daySetting = setToneForDay()
        text = daySetting[0]
        energy = daySetting[1]
        visibility = daySetting[2]
        #################################
        
        #See if you find anything you can use, but it can impact your health as well ###
        powerSetting = checkForPowerup()
        text += powerSetting[0]
        powers = powerSetting[1]
        totalHealth = player1.health
        totalPowers = powers + player1.superPowers
        if (powers < 0):
            totalHealth = totalHealth + powers # it makes you lose health
        if (totalPowers) > 100:
            totalPowers = 100
        elif (totalPowers < 0):
            totalPowers = 0
        player1.superPowers = totalPowers
        if (totalHealth < 0):
            dead = True
            totalHealth = 0
        elif (totalHealth > 100):
            totalHealth = 100
        player1.health = totalHealth
        
        ################################################################################
        #decide if monster
        enemyChosen = checkForEnemy(monsters)
        text += enemyChosen[0]
        monsterIndex = enemyChosen[1]
        monsterHitPoint = random.randint(0,3)
        ################################################################################
               
        if (not dead):
            displayText(win,text, 12)
            buttonOptions = ['go forward', 'do not press', 'hide', 'fight', 'quit']     
            displayStats(win, player1, monsters[monsterIndex], dayNumber, monsterIndex)
        
        if (dead):
            clearDialog(win)
            text = "  YOU DIED!!!!!!!!"
            displayText(win,text, 36)
            buttonClicked = checkForButtonClick(win,drawOptionButtons(win, ['Any Button', 'Any Button', 'Any Button', 'Any Button', 'Any Button']))
            break
        buttonClicked = checkForButtonClick(win,drawOptionButtons(win, buttonOptions))

       
        # do actions here
        if (not dead): # Still breathing.  Let's see what happens
            if (buttonClicked == 0): # go forward
                if (monsterIndex != -1):
                    displayDialog(win,'You ran smack into the enemy!  That must have hurt A LOT!  Do you have a deathwish or something?  Better luck next time...', True)
                    dead = True
            elif (buttonClicked == 1): # ? button
                displayDialog(win,'You just couldn\'t resist!  Guess you can\'t follow instructions.  It says DO NOT PRESS!', True)
                dead = True
            elif (buttonClicked == 2): # hide
                if monsterIndex != -1:
                    hideWorks = random.randint(0,1)
                    if (hideWorks == 0):
                        displayDialog(win,'You are SOOOOOOOO lucky!!!  Hiding worked and the enemy has gone away...for now!', True)
                    else:
                        displayDialog(win,'Well, that didn\'t work. Next time hide behind something larger than a stick!  HA HA HA', True)
                        dead = True
                else:
                    displayDialog(win,'What are you hiding from?  Your feelings?  You might need to seek professional help...if you know what I mean!!!', True)
            elif (buttonClicked == 3): # fight
                
                if monsterIndex == -1:
                    displayDialog(win,'I guess you are losing your mind a bit being out here all alone.  There is nothing to fight!  You feel ok?', True)
                    
                # Handle battle with Rockzilla ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    
                elif monsterIndex == 0: # Rockzilla
                    if (player1.superPowers > 0):
                        damage = player1.superPowers / 4
                    else:
                        damage = player1.health / 4
                    
                    for r in range (0,4):
                        monsterHitPoint = 1
                        rockImage = g.Image(g.Point(100 + (monsterHitPoint * 60),10),'rock.gif')
                        rockImage.draw(win)
                        #win.autoflush = False          # NEW: set before animation
                        for i in range(100):
                            rockImage.move(0,4)
                            time.sleep(.009)
                            win.update()
                        rockImage.undraw()
                        if (monsterHitPoint == 0): # the monster got a direct hit, other wise they miss you
                            if (player1.superPowers > 0):
                                player1.superPowers -= damage
                                if (player1.superPowers < 0):
                                    player1.superPowers = 0
                            else:
                                player1.health -= damage
                                if (player1.health < 0):
                                    player1.health = 0
                                    dead = True
                        monsters[monsterIndex].health -= int(damage)
                        if (monsters[monsterIndex].health < 0):
                            monsters[monsterIndex].health = 0
                        displayStats(win, player1, monsters[monsterIndex], dayNumber, monsterIndex)
                        win.update()
                        time.sleep(1)
                        # Handle the damage
                        if (player1.health == 100 and player1.superPowers == 100):
                            monsters[0].health = 0
                # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                
                # Handle battle with Zaptron ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    
                elif monsterIndex == 1: # Zaptron
                    if (player1.superPowers > 0):
                        damage = player1.superPowers / 4
                    else:
                        damage = player1.health / 4
                    for r in range (0,3):
                        monsterHitPoint = 0
                        zapImage = g.Image(g.Point(10,420 - (monsterHitPoint * 60)),'lightning.gif')
                        zapImage.draw(win)
                        #win.autoflush = False          # NEW: set before animation
                        for i in range(100):
                            zapImage.move(4,0)
                            time.sleep(.009)
                            win.update()
                        zapImage.undraw()
                        if (monsterHitPoint == 0): # the monster got a direct hit, other wise they miss you
                            if (player1.superPowers > 0):
                                player1.superPowers -= damage
                                if (player1.superPowers < 0):
                                    player1.superPowers = 0
                            else:
                                player1.health -= damage
                                if (player1.health < 0):
                                    player1.health = 0
                                    dead = True
                        monsters[monsterIndex].health -= int(damage)
                        if (monsters[monsterIndex].health < 0):
                            monsters[monsterIndex].health = 0
                        displayStats(win, player1, monsters[monsterIndex], dayNumber, monsterIndex)
                        win.update()
                        time.sleep(1)
                        # Handle the damage
                        if (player1.health == 100 and player1.superPowers == 100):
                            monsters[0].health = 0
                # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                            
                            
                # Handle battle with Cutter ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    
                elif monsterIndex == 2: # Cutter
                    if (player1.superPowers > 0):
                        damage = player1.superPowers / 4
                    else:
                        damage = player1.health / 4
                    for r in range (0,3):
                        monsterHitPoint = 0
                        sawImage = g.Image(g.Point(450,420 - (monsterHitPoint * 80)),'saw.gif')
                        sawImage.draw(win)
                        #win.autoflush = False          # NEW: set before animation
                        for i in range(100):
                            sawImage.move(-4,0)
                            time.sleep(.009)
                            win.update()
                        sawImage.undraw()
                        if (monsterHitPoint == 0): # the monster got a direct hit, other wise they miss you
                            if (player1.superPowers > 0):
                                player1.superPowers -= damage
                                if (player1.superPowers < 0):
                                    player1.superPowers = 0
                            else:
                                player1.health -= damage
                                if (player1.health < 0):
                                    player1.health = 0
                                    dead = True
                        monsters[monsterIndex].health -= int(damage)
                        if (monsters[monsterIndex].health < 0):
                            monsters[monsterIndex].health = 0
                        displayStats(win, player1, monsters[monsterIndex], dayNumber, monsterIndex)
                        win.update()
                        time.sleep(1)
                        # Handle the damage
                        if (player1.health == 100 and player1.superPowers == 100):
                            monsters[0].health = 0
                # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            else: # quit button pressed
                break
        if (not dead):
            nextScreen(win, backImage, playerImage)
        clearDialog(win)
        dayNumber -= 1
    # We are at the end.  Did we win or die?
    if (not dead): # you won!!!
        cave = g.Image(g.Point(331,240),'cave.gif')
        cave.draw(win)
        displayDialog(win, 'YOU are the best adventurer EVER!!!  You made it to the cave.  Now go inside and find your next adventure!!!  Go Luck!  Thanks for playing KAG!!!', True)
    else:
        displayDialog(win,'Thanks for playing KAG!!!', True)
    win.close()
 

#Main Call
main()


