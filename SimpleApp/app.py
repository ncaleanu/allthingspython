from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.resources import resource_add_path, resource_find
from kivy.core.window import Window


class Paddle(Widget):
    score = NumericProperty(0)
    speedup = 1.2

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y)/(self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * self.speedup
            ball.velocity = vel.x, vel.y + offset


class Ball(Widget):
    """
    Class for the game's ball
    """
    # Define the x-y coordinates of the ball at start
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        """
        Method to update ball position
        """
        self.pos = Vector(*self.velocity) + self.pos


class Game(Widget):
    """
    Create class for the game
    """
    MAX_SCORE = 5
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def check_score(self):
        if self.player1.score >= self.MAX_SCORE or\
                self.player2.score >= self.MAX_SCORE:
            Window.close()
        else:
            pass

    def update(self, dt):

        #  Define the ball's movements throughout game
        self.ball.move()

        # Bouncing off either player's paddle
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # Bouncing off bottom or top wall
        if self.ball.y < 0 or self.ball.top > self.height:
            self.ball.velocity_y *= -1

        if self.ball.x < self.x:
            self.player2.score += 1
            self.check_score()
            self.serve_ball(vel=(4, 0))
        if self.ball.x > self.width:
            self.player1.score += 1
            self.check_score()
            self.serve_ball(vel=(-4, 0))

    def on_touch_move(self, touch):
        if touch.x < self.width/3:
            self.player1.center_y = touch.y
        if touch.x > self.width-self.width/3:
            self.player2.center_y = touch.y


class MyApp(App):
    """
    Create App to create instance of the game
    """
    def build(self):
        resource_add_path('C:/Users/Noah/Documents/allthingspython/SimpleApp')
        resource_find('ball.jpg')
        resource_find('field.jpg')
        game = Game()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1/60.0)
        return game


if __name__ == '__main__':
    MyApp().run()

