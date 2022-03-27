from turtle import Turtle,Screen
tim = Turtle()
tim.speed("fastest")

def GoForward():
    tim.forward(10)

def GoBackward():
    tim.backward(10)

def GoLeft():
    tim.left(10)

def GoRight():
    tim.right(10)


def Clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()    


screen = Screen()
screen.listen()

screen.onkeypress(GoForward,'w')
screen.onkeypress(GoBackward,'s')
screen.onkeypress(GoLeft,'a')
screen.onkeypress(GoRight,'d')
screen.onkeypress(Clear,'c')

screen.exitonclick()
