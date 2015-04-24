#!/usr/bin/env python

import Tkinter as tk

#Learning how to use classes and Tkinter

class Application(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.grid()
		self.createWidgets()

	def createWidgets(self):
		self.quitButton = tk.Button(self, text='Quit', command=self.quit)
		self.quitButton.grid()
		self.helloWorld = tk.Button(self, text='Hello World!', command=self.quit)
		self.helloWorld.grid()
app = Application()
app.master.title('Hello World!')
app.mainloop()
