import pgzrun

# screen and title
WIDTH = 600
HEIGHT = 600
TITLE = "Bouncy balls"
# gravity
GRAVITY = 500

class Circle():
    def __init__(self, x, y, radius, colour):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.vx = 30
        self.vy = 0   
    
    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, self.colour)

# objects
circle1 = Circle(200, 300, 50, "Green")
circle2 = Circle(400, 200, 40, "Red")  # Added second ball

# functions
def draw():
    screen.clear()
    circle1.draw()
    circle2.draw()  # Draw second ball

def update(dt):
    # Update first circle (Green ball)
    circle1.x = circle1.x + circle1.vx * dt
    uy = circle1.vy
    circle1.vy += GRAVITY * dt
    circle1.y += (uy + circle1.vy) * 0.5 * dt
    if circle1.y >= 550:
        circle1.y = 550
        circle1.vy = circle1.vy * -0.9
    if circle1.x >= 550 or circle1.x <= 50:
        circle1.vx = circle1.vx * -0.9
    if keyboard.space:
        circle1.vy = -500

    # Update second circle (Red ball)
    circle2.x = circle2.x + circle2.vx * dt
    uy2 = circle2.vy
    circle2.vy += GRAVITY * dt
    circle2.y += (uy2 + circle2.vy) * 0.5 * dt
    if circle2.y >= 550:
        circle2.y = 550
        circle2.vy = circle2.vy * -0.9
    if circle2.x >= 550 or circle2.x <= 50:
        circle2.vx = circle2.vx * -0.9
    if keyboard.space:
        circle2.vy = -500

pgzrun.go()
