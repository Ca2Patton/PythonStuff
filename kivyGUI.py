#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
	def build(self):
		return Button(text='Hello World!')
TestApp().run()
