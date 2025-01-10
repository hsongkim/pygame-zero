# Add Rules
# every time the color of the line changes randomly.
# even though the player miss, the game keep on going
#The game continues to run without ending, and when cleared, it relocates again and continues with the game.


import pgzrun
from random import randint

WIDTH=400
HEIGHT=400


# list makes one variable to hold more then one things. For example a can be a=[0, 1, "hi"]. when using a list you should use[] not()
dots=[]   #has 10 images of dot( dots.append(actor) 
lines=[]
next_dot=0


for dot in range(0, 10, 1):                                                #repeat to make 10 dots
    actor=Actor("dot")          
    actor.pos=randint(20, WIDTH - 20), randint(20, HEIGHT -20)          # make dot go to a random place
    dots.append(actor)                                                # append(value) function make the value to go to the back of the list


def draw():
    screen.fill("black")

    number=1
    for dot in dots:                                                    #for loop에서 range()가 아니라 list가 사용되면 리스트의 내용을 가지고 오면서 반복.
                                                                        #반복 횟수는 리스트의 값의 수만큼 반복, 여기서 리스트의 경우 dots 임임
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))
        dot.draw()
        number=number+1

    for line in lines:
        # screen.draw.line(line[0],line[1], (100, 0, 0))
        # apple.x=randint(10, 800)    # randint() is a function that picks a random number between 10 to 800
        # randint(0, 255)
        screen.draw.line(line[0],line[1], (randint(0, 255), randint(0, 255), randint(0, 255)))  # randint(100,0,0)아니고 (randint(0, 255),randint(0, 255),randint(0, 255))

def on_mouse_down(pos):
    global next_dot, dots
    global lines
    
    if(next_dot<10):    # 1에서 10까지 클릭하면 index 번호가 9이기때문에 index번호가 10보다 작을 때까지만 코드가 실행되게하면 된다.
        if(dots[next_dot]. collidepoint(pos)):
            if(next_dot):
                lines.append((dots[next_dot-1].pos, dots[next_dot].pos))
                # print(next_dot)
            next_dot=next_dot+1
        #else:
            #lines=[]
            #next_dot=0
    
    if(next_dot==10):   # next_dot=10 means next_dot is same as 10. However, next_dot==10 means checking if next_dot is 10. 
        # dots=[] means deleting what was inside dots
        dots=[]   #has 10 images of dot( dots.append(actor) 
        lines=[]
        next_dot=0

        for dot in range(0, 10, 1):                                                #repeat to make 10 dots
            actor=Actor("dot")          
            actor.pos=randint(20, WIDTH - 20), randint(20, HEIGHT -20)          # make dot go to a random place
            dots.append(actor)   


pgzrun.go()