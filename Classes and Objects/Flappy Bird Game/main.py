import pgzrun

WIDTH = 750
HEIGHT = 750

gravity = 2000.0


class Bouncing_ball:
    def __init__(self, x, y, colour, radius, bounce):
        self.x = x
        self.y = y

        self.vx = 200
        self.vy = 0

        self.radius = radius
        self.colour = colour
        self.bounce = bounce

    def draw_ball(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, self.colour)

    def update_ball(self, dt):
        uy = self.vy
        self.vy += gravity * dt
        self.y += (uy + self.vy) * 0.5 * dt

        if self.y > HEIGHT - self.radius:
            self.y = HEIGHT - self.radius
            self.vy = -self.vy * self.bounce

        self.x += self.vx * dt

        if self.x > WIDTH - self.radius or self.x < self.radius:
            self.vx = -self.vx

        if self.y > HEIGHT - self.radius:
            self.y = HEIGHT - self.radius
            self.vy = -self.vy


# Create the balls

ball1 = Bouncing_ball(100, 50, "blue", 45, 0.9)
ball2 = Bouncing_ball(250, 100, "red", 30, 0.7)
ball3 = Bouncing_ball(400, 150, "green", 55, 0.5)
ball4 = Bouncing_ball(600, 200, "purple", 25, 0.95)


# Put all the ball objects into a list

balls = [ball1, ball2, ball3, ball4]


def draw():
    screen.clear()

    for ball in balls:
        ball.draw_ball()


def update(dt):

    for ball in balls:
        ball.update_ball(dt)


def on_key_down(key):
    if key == keys.SPACE:

        for ball in balls:
            ball.vy = -500


pgzrun.go()