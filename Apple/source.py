# Add Rules
# if catches an apple get one point, if not -5 points, (game over when point = -1) (win when point goes over 10)

import pgzrun
from random import randint

point=0
# print(point)

apple=Actor("apple")

def draw():                     # draw()는 이미 있는 function이기 때문에 따로 실행 필요 없음
    screen.clear()
    apple.draw()


def place_apple():              # place_apple()은 만든 function이기 때문에 실행 필요함
    apple.x=randint(10, 800)    # randint() is a function that picks a random number between 10 to 800 
    apple.y=randint(10, 600)    # x=가로 y=세로


def on_mouse_down(pos):         # after () is :, on_mouse_down = mouse click event
    global point                # global is 밖에있는거 가져오기기(local is opposite)

    if(apple.collidepoint(pos)):
        print("STOP!")
        place_apple()
        point=point+1
        print(point)
    else:
        print("HA! YOU MISSED!")
        point=point-5
        print(point)

    if(point<0):
        print("YOU LOSE!")
        quit()
    elif(point>=10):            # if two ifs can't work at the same time change one of them into elif
        print("WIN!")
        quit()


place_apple()                   # Run place_apple()
pgzrun.go()