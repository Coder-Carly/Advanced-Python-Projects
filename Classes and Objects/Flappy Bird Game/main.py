import pgzrun
WIDTH = 750
HEIGHT = 750

gravity = 2000.0
class Bouncing_ball:
    def __init__ (self,x,y):
        self.x = x
        self.y = y

        self.vx = 200
        self.vy = 0

        self.radius = 45

    def draw_ball(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, "blue")

object = Bouncing_ball(100,50)

def draw():
    screen.clear()
    object.draw_ball()

def update(dt):
    uy = object.vy
    object.vy += gravity * dt
    object.y += (uy + object.vy) * 0.5 * dt
    if object.y > HEIGHT - object.radius:
        object.y = HEIGHT - object.radius
        object.vy = - object.vy * 0.9

    object.x += object.vx * dt
    if object.x > WIDTH - object.radius or object.x < object.radius:
        object.vx = - object.vx
    if object.y > HEIGHT - object.radius or object.y < object.radius:
        object.vy = - object.vy

def on_key_down(key):
    if key == keys.SPACE:
        object.vy = -500

pgzrun.go()

