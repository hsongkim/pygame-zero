# Add Rules
# every time the fox gets a coin he gets faster

import pgzrun
from random import randint

# WIDTH and HEIGHT should always be capitalized
# This changes the size of the screen
WIDTH=400       
HEIGHT=400

health=15
score=0
speed=2
game_over=False

fox=Actor("fox")
fox.pos=100,100
fox_width = 62
fox_hight = 83

coin=Actor("coin")
coin.pos=200,200

def draw():
    screen.fill ("green")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))
    screen.draw.text("Health: " + str(int(health)), color="black", topleft=(10, 30))

    if(game_over):
        screen.fill ("pink")
        screen.draw.text("Final score:" + str(score), topleft=(10, 10), fontsize=60)

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over=True

def update():
    # UnboundLocalError: local variable 'speed' referenced before assignment
    # ^^=global
    global score, speed, health

    if(game_over == False):                     # because the game only plays when game_over is False so if game over is true the game stop.
        if(health>=0) :
            health-=1/60

        if(keyboard.left):
            if(fox.x<(0+(fox_width/2))):        # if fox goes out of the screen (left) we have to add x so that it will come back in sight every time 
                                                # the fox goes out of sight. However because the center is the default you have to code it 
                                                # to go right half the fox so that when its side meet the wall it will stay in the screen 
                fox.x = (0+(fox_width/2))
            else :
                fox.x = fox.x-speed
        elif(keyboard.right):
            if(fox.x>(400-(fox_width/2))):
                fox.x=(400-(fox_width/2))
            else:
                fox.x = fox.x+speed

        if(keyboard.up):
            if(fox.y<(0+(fox_hight/2))):
                fox.y=(0+(fox_hight/2))
            else:
                fox.y = fox.y-speed
        elif(keyboard.down):
            if(fox.y>(400-(fox_hight/2))):
                fox.y=(400-(fox_hight/2))
            else:
                fox.y = fox.y+speed

        coin_collected=fox.colliderect(coin)

        if(coin_collected):
            score=score+10
            speed=speed+2
            place_coin()

           
clock.schedule(time_up, health)    # clock lets the program call a function after specified amount of time. 
place_coin()

pgzrun.go()