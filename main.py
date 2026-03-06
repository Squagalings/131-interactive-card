import turtle
import random

# setup
NUMBER_OF_CONFETTI = 50
CONFETTI_RADIUS = 8
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

screen = turtle.Screen()
screen.bgcolor("#000000") 
screen.setup(width=WINDOW_WIDTH + 300, height=WINDOW_HEIGHT + 300)
screen.title("Falling Confetti Python Code")
screen.tracer(0)

gift_box = turtle.Turtle()
writing = turtle.Turtle()

gift_image = "gift-box.gif" 
screen.addshape(gift_image)

gift_box.penup()
gift_box.shape(gift_image)

# setup turtles
writing.penup()
writing.hideturtle()
writing.color("white")
writing.goto(0, 250) 
writing.write("Click on the box!", align="center", font=("Arial", 24, "bold"))

# confetti
class Confetti(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.shape("circle")
        self.color(random.choice(["red", "yellow", "blue", "green", "purple", "orange", "pink"]))
        self.radius = CONFETTI_RADIUS
        self.shapesize(stretch_len=self.radius / 8, stretch_wid=self.radius / 8)
        self.goto(random.randint(-WINDOW_WIDTH // 2, WINDOW_WIDTH // 2), random.randint(WINDOW_HEIGHT // 2, WINDOW_HEIGHT // 2 + 100))
        self.dy = -random.uniform(0, 3) 

    def fall(self):
        y = self.ycor() + self.dy
        self.sety(y)

        # if it reaches the bottom, reset to the top
        if y < -WINDOW_HEIGHT // 2:
            self.goto(random.randint(-WINDOW_WIDTH // 2, WINDOW_WIDTH // 2), random.randint(WINDOW_HEIGHT // 2, WINDOW_HEIGHT // 2 + 50))
            self.dy = -random.uniform(0, 3)

# confetti pieces
confetti_list = []
for _ in range(NUMBER_OF_CONFETTI):
    confetti_list.append(Confetti())

# interaction
party_started = False

def open_gift(x, y):
    global party_started
    if not party_started:
        party_started = True
        
        # update the Text
        writing.clear() 
        writing.goto(0, 0)
        writing.write("Happy Birthday!", align="center", font=("Arial", 36, "bold")) 
        
        # make the box disappear
        gift_box.hideturtle() 
        
        # make the confetti visible
        for confetti in confetti_list:
            confetti.showturtle()

gift_box.onclick(open_gift)

def animate():
    if party_started:
        for confetti in confetti_list:
            confetti.fall()
            
    screen.update()
    screen.ontimer(animate, 10) 

animate()
screen.mainloop()
