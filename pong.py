import turtle
import winsound
# global variable
wn = turtle.Screen()
wn.title("Pong by George")
wn.bgcolor("black")
# for width mean -400 and 400 and for height mean 300 and -300 use x,y and 0,0 is the center of the screen
wn.setup(width=800, height=600)
# wn tracer to speed up the program movement if not the game is going so slow
wn.tracer(0)
# start with project

# Score
score_a = 0
score_b = 0

# Paddle A
# use turtle to call the file that has been imported and Turtle is the class for create object
paddle_a = turtle.Turtle()
# same as tracer set to fastest speed otherwise it will be really slow not the movement speed
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
# by default a shape is 20px width and length so change to 100, 20 it use multiplication so 5 mean 20 *5 and 1 mean 20
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
# turtle is to draw a line if there is no penup then it will draw line from 0,0 until -350,0 so it need to be disable
paddle_a.penup()
# coordinate as mention prior x -350 mean left and 0 y
paddle_a.goto(-350, 0)


# testing the program each progress is really important
# Paddle B
# copy the same paddle from paddle A and change the location
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
# change to 350 to make it to the right
paddle_b.goto(350, 0)


# copy same as paddle but change the size and  name
# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# variable for the ball movement this mean if x move 2 px and y move 2 px
ball.dx = 0.2
ball.dy = 0.2

# PEN for scoring
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
# to hide the turtle because it is object like an arrow
pen.hideturtle()
# put the pen up
pen.goto(0, 260)
pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center",
          font=("Courier", 24, "normal"))

# Function


def paddle_a_up():
    # ycor from the turtle module to pick up the y coordinate
    y = paddle_a.ycor()
    # plus 20 to the y coordinate mean 20 pixel
    y += 20
    # sety to change the y coordinate to the new y that has been created
    paddle_a.sety(y)
# after the test success than we can copy the up code and set for y down


def paddle_a_down():
    y = paddle_a.ycor()
    # minus 20 to the y coordinate mean 20 pixel
    y -= 20
    # sety to change the y coordinate to the new y that has been created
    paddle_a.sety(y)
# if both of this work than copy the code and change to paddle b


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
# this listen is to listen the keyboard input
wn.listen()
# onkeypress is a function and the first parameter is the function that get executed and the second parameter is the key input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
# to use up arrow and down arrow for keyboard input Up = arrow up and Down = arrow down
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    # wn update mean to keep the screen update
    wn.update()
    # move the ball
    # set the ball by the ball coord and plus by the movement inside ball variable which is 2
    ball.setx(ball.xcor() + ball.dx)
    # ball movement for the y coord
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # border check for up border maximum so y coordinate use 290 more because 20 px ball
    if ball.ycor() > 290:
        # if the ball reach more than 290 x than set the x to 290 first
        ball.sety(290)
        # the dy movement * -1 to make negative movement mean the ball will come back at other direction
        ball.dy *= -1
        #winsound.PlaySound('bounce.wav', winsound.SND_FILENAME)
    # time to check and if it work the ball bounce then copy
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        #winsound.PlaySound('bounce.wav', winsound.SND_FILENAME)
    # check again and set the ball.dy to = -0.2 to check when the ball crossing the below border
    # For border x it is different to add
    if ball.xcor() > 390:
        # set the ball again to the first again because one side is win
        # mean that a win or get 1 point
        score_a += 1
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    # if work then paste the code
    if ball.xcor() < -390:
        # mean that b win or get 1 point
        score_b += 1
        ball.goto(0, 0)
        ball.dx *= -1
        # to clear the before write statement first so not overwrite
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b),
                  align="center", font=("Courier", 24, "normal"))

    # check again and set the ball.dx = -0.2 to check the other side

    # paddle and ball collision
    # if x cor of the ball is more than 340 which is when it collide or not and when ball ycor is inside example paddle y = 0 then inside -50<ycor>50 or the paddle
    # to make sure no glitch make the ball doesnt go beyond 350
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    # check if it work as ususal and then copy
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
