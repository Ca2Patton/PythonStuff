#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint, random
from kivy.graphics import Color
from kivy.core.window import Window

class PongPaddle(Widget):
	score = NumericProperty(0)

	def bounce_ball(self, ball):
		if self.collide_widget(ball):
			vx, vy = ball.velocity
			offset = (ball.center_y - self.center_y) / (self.height /2)
			bounced = Vector(-1 * vx , vy)
			vel = bounced * 1.1
			ball.velocity = vel.x, vel.y + offset
			color = (random(), random(), random())
			with self.canvas.before:
				Color(*color)
class PongBall(Widget):

	#velocity of the ball on the X and Y Axis
	velocity_x = NumericProperty(0)
	velocity_y = NumericProperty(0)

	#Shorthand for referencelist
	velocity = ReferenceListProperty(velocity_x, velocity_y)
	
	#Used for ball movement.
	def move(self):
		self.pos = Vector(*self.velocity) + self.pos

class PongGame(Widget):
	ball = ObjectProperty(None)
	player1 = ObjectProperty(None)
	player2 = ObjectProperty(None)

	def __init__(self, **kwargs):
		super(PongGame, self).__init__(**kwargs)
		self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
		self._keyboard.bind(on_key_down=self._on_keyboard_down)

	def _keyboard_closed(self):
		self.keyboard.unbind(on_key_down=self._on_keyboard_down)
		self._keyboard = None

	def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
		if keycode[1] == 'w':
			self.player1.center_y += 10
		elif keycode[1] == 's':
			self.player1.center_y -= 10
		elif keycode[1] == 'k':
			self.player2.center_y += 10
		elif keycode[1] == 'l':
			self.player2.center_y -= 10
		return True

	def serve_ball(self, vel=(4, 0)):
		self.ball.center = self.center
		self.ball.velocity = vel

	def update(self, dt):
		self.ball.move()

		self.player1.bounce_ball(self.ball)
		self.player2.bounce_ball(self.ball)

		#Bounce ball
		if (self.ball.y < 0) or (self.ball.top > self.height):
			self.ball.velocity_y *= -1

		#Scoring
		if self.ball.x < self.x:
			self.player2.score += 1
			self.serve_ball(vel=(4, 0))
		if self.ball.x > self.width:
			self.player1.score += 1
			self.serve_ball(vel=(-4, 0))
	
	def on_touch_move(self, touch):
		if touch.x < self.width / 3:
			self.player1.center_y = touch.y
		if touch.x > self.width - self.width / 3:
			self.player2.center_y = touch.y
class PongApp(App):
	def build(self):
		game = PongGame()
		game.serve_ball()
		Clock.schedule_interval(game.update, 1.0/60.0)
		return game

if __name__ == '__main__':
	PongApp().run()
