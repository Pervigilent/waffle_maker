import tkinter as tk

class WaffleMaker:
	def __init__(self):
		self.reticle_window = ReticleWindow()
		self.wafer_window = WaferWindow(self.reticle_window)
		
	def run(self):
		self.wafer_window.run()
		
class WaferWindow:
	def __init__(self, reticle_window):
		self.window = None
		self.reticle_window = reticle_window
		
	def run(self):
		self.window = tk.Tk()
		self.window.wm_title("Wafer Map")
		self.window.mainloop()

class ReticleWindow:
	def __init__(self):
		self.window = None
		
	def run(self):
		self.window = tk.Tk()
		self.window.wm_title("Reticle Map")
		self.window.mainloop()
		
my_waffle_maker = WaffleMaker()
my_waffle_maker.run()

