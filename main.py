import turtle as t
from turtle import Screen
import random



#TODO 1 hirst 10 by 10
#TODO 2 each dot 20 in size and 50 between spaces

color_list = [(202, 164, 110),  (149, 75, 50), (222, 201, 136),
 (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
              (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208),
              (168, 99, 102)]

tim = t.Turtle()
t.colormode(255)

#draw 10 dots (20 in size, 50 between spaces)
#go up by one row (50 between spaces)
#repeat the process 10 times
def moving_forward():
    """Dots are moving forward anc they change colors"""
    for i in range(10):
        tim.penup()
        tim.sety(i *50)
        tim.setx(-200)
        for _ in range(10):
            tim.dot(20, random.choice(color_list))
            tim.penup()
            tim.forward(50)
            tim.pendown()



moving_forward()
tim.exitonclick()





# def move_up(size_of_gap):
#     for _ in range(int( / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
