import turtle
import random

# --- Configuration ---
NUMBER_OF_CONFETTI = 50
CONFETTI_RADIUS = 8
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

# --- Setup Screen ---
screen = turtle.Screen()
screen.bgcolor("#000000") # Black background
# FIXED: Changed 'window' to 'screen' to match your variable!
screen.setup(width=WINDOW_WIDTH + 300, height=WINDOW_HEIGHT + 300)
screen.title("Falling Confetti Python Code")
screen.tracer(0) # Turn off automatic screen updates

# --- Setup Gift Box & Writing ---
gift_box = turtle.Turtle()
writing = turtle.Turtle()

# FIXED: Turtle ONLY accepts .gif images! Make sure your file is a .gif
gift_image = "gift-box.gif" 
screen.addshape(gift_image)

gift_box.penup()
gift_box.shape(gift_image)

# Setup the instructions
writing.penup()
writing.hideturtle() # We only want to see the text, not the turtle itself
writing.color("white")
writing.goto(0, 250) # Move it above the box
writing.write("Click on the box!", align="center", font=("Arial", 24, "bold"))

# --- Confetti Class ---
class Confetti(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle() # Hide the confetti initially!
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

        # If it reaches the bottom, reset to the top
        if y < -WINDOW_HEIGHT // 2:
            self.goto(random.randint(-WINDOW_WIDTH // 2, WINDOW_WIDTH // 2), random.randint(WINDOW_HEIGHT // 2, WINDOW_HEIGHT // 2 + 50))
            self.dy = -random.uniform(0, 3)

# --- Create Confetti Pieces ---
confetti_list = []
for _ in range(NUMBER_OF_CONFETTI):
    confetti_list.append(Confetti())

# --- Interaction Logic ---
party_started = False # Our master switch

def open_gift(x, y):
    global party_started
    if not party_started: # Only trigger if the party hasn't started yet
        party_started = True
        
        # 1. Update the Text
        writing.clear() # Erase the instructions
        writing.goto(0, 0) # Move down to the middle of the screen
        writing.write("Happy Birthday!", align="center", font=("Arial", 36, "bold")) 
        
        # 2. Make the box disappear
        gift_box.hideturtle() 
        
        # Make the confetti visible!
        for confetti in confetti_list:
            confetti.showturtle()

# Tell the gift box to listen for a click
gift_box.onclick(open_gift)

# --- Main Animation Loop (The safe way!) ---
def animate():
    if party_started:
        for confetti in confetti_list:
            confetti.fall()
            
    screen.update() # Refresh the screen
    screen.ontimer(animate, 10) # Run this function again in 10 milliseconds

# Start the animation loop and keep the window open
animate()
screen.mainloop()