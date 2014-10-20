#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
from kivy.app import App
from kivy.uix.widget import Widget

class PongGame(Widget):
	pass

class PongApp(App):
	def build(self):
		return PongGame()

if __name__ == '__main__':
	pongApp().run()
