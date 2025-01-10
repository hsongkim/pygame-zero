# a cock flys to a person that spawns randomly on the screen and kill the person


import pgzrun

WIDTH=600
HEIGHT=600

cock=Actor("cock")
cock_fly=Actor("cock fly")
person=Actor("person")
person_scared=Actor("person scared")
person_dead=Actor("person dead")


def draw():
    screen.fill ("green")
    cock.draw()
    person.draw()
    








pgzrun.go()