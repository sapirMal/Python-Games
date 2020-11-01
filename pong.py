import turtle
import winsound

win = turtle.Screen()
win.title("Pong by @TokyoEdTech")
win.bgcolor("#000960")
win.setup(width=800, height=600)
win.tracer(0)


def init(left, ball=False):
    player = turtle.Turtle()
    player.speed(0)  # maximun speed
    player.shape("square")
    player.color("#F7F7F7")
    player.penup()

    if ball:
        player.goto(0, 0)
    else:
        player.shapesize(stretch_wid=5, stretch_len=1)
        if left:
            player.goto(-350, 0)
        else:
            player.goto(350, 0)
    return player


# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = init(True)

# Paddle B
paddle_b = init(False)

# Ball
ball = init(False, True)
ball.dx = 0.2  # move by 0.2 px
ball.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align="center",
          font=("Ariel", 20, "normal"))


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20  # add 20 px to the new y
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20  # sub 20 px to the new y
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20  # add 20 px to the new y
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20  # sub 20 px to the new y
    paddle_b.sety(y)


# Keyboard binding (input)
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "z")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # reverse the direction
        winsound.PlaySound("ball.wav", winsound.SND_ASYNC)

    if ball.ycor() < (-290):
        ball.sety(-290)
        ball.dy *= -1  # reverse the direction
        winsound.PlaySound("ball.wav", winsound.SND_ASYNC)


    if ball.xcor() > 390:
        ball.goto(0, 0)  # disqualification
        ball.dx *= -1
        score_a += 1
        winsound.PlaySound("ball.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center",
                  font=("Ariel", 20, "normal"))

    if ball.xcor() < (-390):
        ball.goto(0, 0)  # disqualification
        ball.dx *= -1
        score_b += 1
        winsound.PlaySound("ball.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center",
                  font=("Ariel", 20, "normal"))

   # Paddle and ball collisions
    if 350 > ball.xcor() > 340 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("ball.wav", winsound.SND_ASYNC)

    if -350 < ball.xcor() < -340 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("ball.wav", winsound.SND_ASYNC)

