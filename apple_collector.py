import pygame #importing pygame to this program; calling on pygame
import ctypes #allows access to real peripheral
import time   #importing time function to this program; calling on pygame
import random #importing random function to this program; calling on pygame
import sys    #importing system to this program; calling on pygame

pygame.init() #initializing pygame

display_width = 1086 #assigning the display width variable to 1086 pixels
display_height = 768 #assigning the display height variable to 768 pixels

gameDisplay = pygame.display.set_mode((display_width,display_height)) #setting the game display using variables
pygame.display.set_caption('Apple Collector')                         #naming the game window to "Apple Collector"

black = (0,0,0)           #assigning a variable to set the RGB color value for black
white = (255,255,255)     #assigning a variable to set the RGB color value for white
purple = (87,65,214)      #assigning a variable to set the RGB color value for purple
darkPurple  = (87,25,214) #assigning a variable to set the RGB color value for dark purple
green = (0,205,102)       #assigning a variable to set the RGB color value for green

basket_width = 142        #assigning a variable for the basket image's width
basket_height = 99        #assigning a variable for the basket image's height
apple_width = 50          #assigning a variable for the apple image's width
apple_height = 51         #assigning a variable for the apple image's height
bomb_width = 80           #assigning a variable for the bomb image's width
bomb_height = 82          #assigning a variable for the bomb image's height
goldenApple_width = 80    #assigning a variable for the golden apple image's width
goldenApple_height = 76   #assigning a variable for the golden apple image's height

clock = pygame.time.Clock()                               #assigning a variable to help tract time

backgroundImg = pygame.image.load("Background.jpg")       #assigning the variable and loading the background image
appleImg = pygame.image.load("Apple.png")                 #assigning the variable and loading the apple image
basketImg = pygame.image.load("Basket.png")               #assigning the variable and loading the basket image
bombImg = pygame.image.load("Bomb.png")                   #assigning the variable and loading the bomb image
goldenAppleImg = pygame.image.load("GoldenApple.png")     #assigning the variable and loading the golden apple image
lives3Img = pygame.image.load("Lives3.png")               #assigning the variable and loading the 3 lives left image
lives2Img = pygame.image.load("Lives2.png")               #assigning the variable and loading the 2 lives left image
lives1Img = pygame.image.load("Lives1.png")               #assigning the variable and loading the 1 live left image
lives0Img = pygame.image.load("Lives0.png")               #assigning the variable and loading the 0 lives left image
appleIcon = pygame.image.load("AppleIcon.png")            #assigning the variable and loading the apple image icon for the program

pygame.display.set_icon(appleIcon)                        #displaying the apple image icon on the top left of the window display

pause = False #giving pause a boolean value of false

def apples_collected(count):                                     #defining the numbers of apples collected for counting
    font = pygame.font.SysFont(None,40)                          #making the font size of the "Collected" points to size 40
    text = font.render("Collected: "+str(count), True, white)    #outputting the text of collected points and making the text white
    gameDisplay.blit(text,(800,150))                             #displaying the collected points on the game window

def background(x1,y1):                                           #defining the backround with its x and y value
    gameDisplay.blit(backgroundImg,(x1,y1))                      #displaying the background image on the game window

def apple(x2,y2):                                                #defining apple with its x and y value
    gameDisplay.blit(appleImg,(x2,y2))                           #displaying the apple image on the game window

def basket(x3,y3):                                               #defining basket with its x and y value
    gameDisplay.blit(basketImg,(x3,y3))                          #displaying the basket image on the game window

def bomb (x4,y4):                                                #defining bomb with its x and y value
    gameDisplay.blit(bombImg,(x4,y4))                            #displaying the bomb image on the game window

def goldenApple (x5,y5):                                         #defining golden apple with its x and y value
    gameDisplay.blit(goldenAppleImg,(x5,y5))                     #displaying the golden apple image on the game window

def lives3 (x6,y6):                                              #defining 3 lives left with its x and y value
    gameDisplay.blit(lives3Img,(x6,y6))                          #displaying the 3 lives left image on the game window

def lives2 (x7,y7):                                              #defining 2 lives left with its x and y value
    gameDisplay.blit(lives2Img,(x7,y7))                          #displaying the 2 lives left image on the game window

def lives1 (x8,y8):                                              #defining 1 live left with its x and y value
    gameDisplay.blit(lives1Img,(x8,y8))                          #displaying the 1 live left image on the game window

def lives0 (x9,y9):                                              #defining 0 lives left with its x and y value
    gameDisplay.blit(lives0Img,(x9,y9))                          #displaying the 0 lives left image on the game window

def In(addr):                                                    #Function you use to get data from peripheral
    return ctypes.windll.inpout32.Inp32(addr)                    #ctypes function to read byte from address addr of parallel port

def Out(addr, byte):                                             #Function you will use to send data to peripheral 
    ctypes.windll.inpout32.Out32(addr,byte)                      #ctypes function to send byte to address addr of parallel port

def miss():                                                      #defining miss for outputting it as a text and display
    gameDisplay.fill(green)                                      #making the game display "miss" to fill the colour green
    largeText = pygame.font.Font('freesansbold.ttf', 75)         #using large text font 
    TextSurf, TextRect = text_objects('GAME OVER!' , largeText)  #outputting "Game Over!" message to the user if they miss
    TextRect.center = ((display_width/2),(250))                  #outputting the text at certain pixels in the game window
    gameDisplay.blit(TextSurf, TextRect)                         #outputting the texts on the game display

    while True:                                                  #using the while loop to determine if the user "Plays" or "Quits" the game
        for event in pygame.event.get():                         #getting the input from the user if they want to "Play" or "Quit"
            if event.type == pygame.QUIT:                        #using the selection structure to determine if the user quits; then the application closes
                pygame.quit()                                    #function to quit the game
                quit()                                           #exits the application

        button("PLAY AGAIN!",270,450,175,70,darkPurple,purple,game_loop)  #setting text at certain pixel value with colors of the button changing if use hovers the mouse over it; this button leads to gameplay again
        button("QUIT",625,450,175,70,darkPurple,purple,quitgame)          #setting text at certain pixel value with colors of the button changing if use hovers the mouse over it; this button leads to quitting the game
            
        pygame.display.update()  #updating the display after adding button
        clock.tick(15)           #running the program at no more than 15 frames per second to make it smooth

def text_objects(text, font):                           #defining text and its font
    textSurface = font.render(text, True, black)        #assigning text to normal format with colour black
    return textSurface, textSurface.get_rect()          #outputting text in the display window

def text_objects1(text, font):                          #defining text and its font
    textSurface = font.render(text, True, white)        #assigning text to normal format with colour black
    return textSurface, textSurface.get_rect()          #outputting text in the display window

def button(msg,x,y,w,h,ic,ac,action=None):              #defining the button's message, x and y coordinates, its width and height, its active colour(mouse hover colour) and inactive colour
    mouse = pygame.mouse.get_pos()                      #assigning a variable mouse to get the mouse's position
    click = pygame.mouse.get_pressed()                  #assigning a variable click to get an input if any button on the mouse is clicked
        
    if x+w > mouse[0] > x and y+h > mouse[1] > y:       #using selection structure to determine if the user clicks buttons
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))     #outputting game display
        if click[0] == 1 and action != None:            #using selection structure to determine when to call the function action(); depending on which button is clicked
            action()                                    #calls the function action()
    else:                                               #using else to determine next command
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))     #outputting game display

    smallText = pygame.font.Font("freesansbold.ttf",25) #using small text font
    textSurf, textRect = text_objects1(msg, smallText)  #outputting a message to the user in small text
    textRect.center = ((x+(w/2)), y+(h/2))              #outputting the text at certain pixels in the game window
    gameDisplay.blit(textSurf, textRect)                #outputting the texts on the game display

def quitgame():     #defining quit game
    pygame.quit()   #function to quit the game
    quit()          #exits the application

def unpause():      #defining unpause 
    global pause    #making "pause" a global variable for flexibility
    pause = False   #giving pause a boolean expression of false

def paused():                                               #defining pause if the user decides to pause the game
    gameDisplay.fill(green)                                 #making the game display "pause" to fill the colour green
    largeText = pygame.font.Font('freesansbold.ttf', 75)    #using large text font 
    TextSurf, TextRect = text_objects('Paused' , largeText) #outputting "Paused" message to the user if they paused the game
    TextRect.center = ((display_width/2),(250))             #outputting the text at certain pixels in the game window
    gameDisplay.blit(TextSurf, TextRect)                    #outputting the texts on the game display

    while pause:                                            #using a while loop to determine if the user pauses
        for event in pygame.event.get():                    #getting the input from the user if they want to continue or quit the game
            if event.type == pygame.QUIT:                   #using the selection structure to determine if the user quits; then the application closes
                pygame.quit()                               #function to quit the game
                quit()                                      #exits the application

        button("CONTINUE",270,450,175,70,darkPurple,purple,unpause)     #setting text at certain pixel value with colors of the button changing if use hovers the mouse over it; this button coninues the play of the game
        button("QUIT",625,450,175,70,darkPurple,purple,quitgame)        #setting text at certain pixel value with colors of the button changing if use hovers the mouse over it; this button leads to quitting the game
            
        pygame.display.update() #updating the display after adding button
        clock.tick(15)          #running the program at no more than 15 frames per second to make it smooth

def game_intro():                           #defining the game intro
    intro = True                            #setting intro to a boolean expression of true
    while intro:                            #using a while loop to determine the start of the game           
        for event in pygame.event.get():    #getting the input from the user if they want to play or quit the game
            if event.type == pygame.QUIT:   #using the selection structure to determine if the user quits; then the application closes
                pygame.quit()               #function to quit the game
                quit()                      #exits the application
        gameDisplay.fill(green)             #making the game display "game intro" to fill the colour green
        largeText = pygame.font.Font('freesansbold.ttf', 75)                #using large text font
        TextSurf, TextRect = text_objects('Apple Collector' , largeText)    #outputting a message to the user of the title of the game
        TextRect.center = ((display_width/2),(250))                         #outputting the text at certain pixels in the game window
        gameDisplay.blit(TextSurf, TextRect)                                #outputting the texts on the game display

        button("PLAY!",270,450,175,70,darkPurple,purple,game_loop)          #setting text at certain pixel value with colors of the button changing if use hovers the mouse over it; this button coninues the play of the game
        button("QUIT",625,450,175,70,darkPurple,purple,quitgame)            #setting text at certain pixel value with colors of the button changing if use hovers the mouse over it; this button leads to quitting the game
            
        pygame.display.update()     #updating the display after adding button
        clock.tick(15)              #running the program at no more than 15 frames per second to make it smooth
        
def game_loop():        #defining game loop
    global pause        #making "pause" a global variable for flexibility
    
    x1 = (0)            #assigning x1 a value for the background image
    y1 = (0)            #assigning y1 a value for the background image
    
    x2 = random.randrange(0, display_width - apple_width)   #assigning x2 a random value for the apple image
    y2 = -600                                               #assigning y2 a value for the apple image

    appleImg_speed = 3  #assigning the apple image speed of falling                        
    
    x3 = (543)          #assigning x3 a value for the basket image
    y3 = (630)          #assigning y3 a value for the basket image
    
    x4 = random.randrange(0, display_width - bomb_width)    #assigning x4 a random value for the bomb image
    y4 = -3000                                              #assigning y4 a value for the bomb image
    
    bombImg_speed = 6   #assigning the bomb image speed of falling
    
    x5 = random.randrange(0, display_width - goldenApple_width)     #assigning x5 a random value for the golden apple image
    y5 = -10000                                                      #assigning y5 a value for the golden apple image
    
    goldenAppleImg_speed = 6    #assigning the golden apple image speed of falling
    
    x6 = 786    #assigning x6 a value for three lives left image
    y6 = 30     #assigning y6 a value for three lives left image

    x7 = 786    #assigning x7 a value for two lives left image
    y7 = 30     #assigning y7 a value for two lives left image

    x8 = 786    #assigning x8 a value for one live left image
    y8 = 30     #assigning y8 a value for one live left image

    x9 = 786    #assigning x9 a value for zero lives left image
    y9 = 30     #assigning y9 a value for zero lives left image
    
    x_change = 0    #assigning x change for the basket to move left or right

    collected = 0   #assigning the collected apples value to 0

    misses = 0      #assigning missed apple values to 0

    left = False    #assiging left a boolean expression of false for the left movement of the basket
    right = False   #assiging right a boolean expression of false for the right movement of the basket
    missed = False  #assiging missed a boolean expression of false

    while not missed:           #using a while loop to determine if not missed, then continue to use the input from peripheral

        sInput = In(0x379)                          #(base +1) is address of parallel port status register
        if (sInput == 248) or (sInput == 40):       #current values for the button for moving left
            left = True                             #variable left's boolean expression is true
        elif (sInput == 56) or (sInput == 232):     #current values for the button for moving right
            right = True                            #variable right's boolean expression is true
        else:                                       #using the selection structure to make both values false
            left = False                            #variable left's boolean expression is false
            right = False                           #variable right's boolean expression is false
        
        for event in pygame.event.get():        #getting the input from the user if they want to quit the game
            if event.type == pygame.QUIT:       #using the selection structure to determine if the user quits; then the application closes
                missed = True                   #function to quit the game
                quit()                          #exits the application
                
            if event.type == pygame.KEYDOWN:        #using selection structure to determine if any keyboard keys were pressed
                if event.key == pygame.K_p:         #if the p on the keyboard is pressed, it pauses
                    pause = True                    #pause is true
                    paused()                        #it pauses the game 
                    
        if left and right:      #using the selection structure to determine if the user hits both of the buttons
            x_change *= 1       #gives x change value of 1 (moves basket image)
        elif left:              #using the selection structure to determine if the user hits left button
            x_change = -15      #gives x change value of -15 (moves basket image)
        elif right:             #using the selection structure to determine if the user hits right button
            x_change = 15       #gives x change value of 15 (moves basket image)
        else:                   #other than that, the x value remains the same
            x_change = 0        #gives x change value of 0 (moves basket image)

        x3 += x_change          #if buttons are hit, the basket's x3 value is added from the x change depending on if it's the right or left button
        
        background(x1,y1)       #outputting the background image to the x1 and y1 values
        
        basket(x3,y3)           #outputting the basket image to the x3 and y3 values
        
        apple(x2,y2)            #outputting the apple image to the x2 and y2 values
        y2 += appleImg_speed    #setting the apple's drop speed
        
        bomb(x4,y4)             #outputting the bomb's image to the x4 and y4 values
        y4 += bombImg_speed     #setting the bomb's drop speed

        goldenApple(x5,y5)          #outputting the golden apple's image to the x5 and y5 values
        y5 += goldenAppleImg_speed  #setting the golden apple's drop speed
        
        apples_collected(collected) #outputting the number of apples collected during the gameplay
        
        if misses==0:           #using selection structure to determine the number of lives
            lives3(x6,y6)       #outputs the lives as only 3 golden apple remaining
        elif misses==1:         #using selection structure to determine the number of lives
            lives2(x7,y7)       #outputs the lives as only 2 golden apple remaining
        elif misses==2:         #using selection structure to determine the number of lives
            lives1(x8,y8)       #outputs the lives as only 1 golden apple remaining
        elif misses==3:         #using selection structure to determine the number of lives
            miss()              #it ends the program to the closing
            Out(0x378,8)        #calls on the output of the peripheral
            time.sleep(5)       #remains for 5 seconds
            Out(0x378,0)        #send 0 to parallel port to reset peripheral

        
        if x3 > display_width:  #using selection structure to allow the basket to move through the boundries apprearing on opposite side
            x3 = -142           #setting x3 a value of -142
        elif x3 <=-142:         #using selection structure to allow the basket to move through the boundries apprearing on opposite side
            x3 = display_width  #setting x3 a value of the display width

        if y2 > display_height:                                 #using selection structure to determine what happens when the y value of apple image drops below the y value of basket
            y2 = -300                                           #setting y value of the apple image to -300
            x2 = random.randrange(0,display_width-apple_width)  #setting x value of the apple image to random in the range of display width
            collected -=1                                       #assigning collected apples to -1
            Out(0x378,1)                                        #calls on the output of the peripheral
            time.sleep(0.125)                                   #remains for 0.125 seconds
            Out(0x378,0)                                        #send 0 to parallel port to reset peripheral
            misses +=1                                          #adds 1 to the misses because it missed the apple
            appleImg_speed += 0.20                              #it increases the apple image's drop speed
            
        if y4 > display_height:                                 #using selection structure to determine what happens when the y value of bomb image drops below the y value of basket
            y4 = 0 - y4                                         #setting y value of the bomb image to y4(original y location)
            x4 = random.randrange(0,display_width-bomb_width)   #setting x value of the bomb image to random in the range of display width
            bombImg_speed += 0.50                               #it increases the bomb image's drop speed

        if y5 > display_height:                                         #using selection structure to determine what happens when the y value of golden apple image drops below the y value of basket
            y5 = -10000                                                 #setting y value of the golden apple's image to -10000
            x5 = random.randrange(0,display_width-goldenApple_width)    #setting x value of the golden apple's image to random in the range of display width

        if (y3 + 70 < y4+bomb_height) and (y3 + 70 > y4):                                                                   #using selection structure to determine what happens if the y value of bomb touches the y value of basket                          
            if (x4 > x3 and x4 < x3 + basket_width) or (x4 + bomb_width > x3 and x4 + bomb_width < x3 + basket_width):      #using selection structure to determine what happens if the x value of bomb touches the x value of basket
                y4 = -500               #setting y4 of bomb image back to -500 pixels
                collected -= 1          #score of collected apple deducts 1 point
                Out(0x378,1)            #calls on the output of the peripheral
                time.sleep(0.125)       #remains for 0.125 seconds
                Out(0x378,0)            #send 0 to parallel port to reset peripheral
                misses += 1             #adds 1 to the misses because it touched the bomb
                
        if (y3 + 70 < y2+apple_height) and (y3 + 70 > y2):                                                                  #using selection structure to determine what happens if the y of value apple image touches the y value of basket
            if (x2 > x3 and x2 < x3 + basket_width) or (x2 + apple_width > x3 and x2 + apple_width < x3 + basket_width):    #using selection structure to determine what happens if the x of value apple image touches the x value of basket
                y2 = -300                                           #setting y3 of apple image back to -300 pixels
                x2 = random.randrange(0,display_width-apple_width)  #setting x value of the apple image to random in the range of display width
                collected += 1                                      #score of collected apple adds 1 point
                Out(0x378,4)                                        #calls on the output of the peripheral
                time.sleep(0.125)                                   #remains for 0.125 seconds
                Out(0x378,0)                                        #send 0 to parallel port to reset peripheral
                appleImg_speed += 0.40                              #it increases the apple image's drop speed

        if (y3 + 70 < y5+goldenApple_height) and (y3 + 70 > y5):                                                                            #using selection structure to determine what happens if the y value of golden apple image touches the y value of basket
            if (x3 > x5 and x3 < x5 + goldenApple_width) or (x3 + goldenApple_width > x5 and x3 + goldenApple_width < x5 + basket_width):   #using selection structure to determine what happens if the x value of golden apple image touches the x value of basket
                y5 = -10000                                                  #setting y5 of golden apple image back to -10000 pixels
                x5 = random.randrange(0,display_width-goldenApple_width)    #setting x value of the bomb image to random in the range of display width
                collected += 5      #score of collected apple adds 5 points
                Out(0x378,4)        #calls on the output of the peripheral
                time.sleep(0.125)   #remains for 0.125 seconds
                Out(0x378,0)        #send 0 to parallel port to reset peripheral
                if misses <= 0:     #using the selection structure to keep the misses 0 to determine lives
                    misses == 0     #make the misses value to 0
                else:               #using the selection structure ti determine lives
                    misses -= 1     #make the misses value to -1
        
        pygame.display.update()     #updating the display after adding button
        clock.tick(60)              #running the program at no more than 15 frames per second to make it smooth

game_intro()                        #calling on the function game intro
game_loop()                         #calling on the function game loop
pygame.quit()                       #function to quit the game
quit()                              #exits the application
