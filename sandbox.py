import tkinter as tk
from PIL import Image, ImageTk


class Device:
	def __init__(self):
		pass
		
class Reticle:
	def __init__(self):
		pass

class Wafer:
	def __init__(self):
		pass

class DeviceWindow:
	def __init__(self):
		pass
		
	def run(self):
		pass

class ReticleWindow:
	def __init__(self, parent_window):
		self.window = None
		self.parent_window = parent_window
		
	def run(self):
		self.window = tk.Toplevel(self.parent_window)
		
		self.panel_left = tk.Frame(master=self.window)
		self.panel_center = tk.Frame(master=self.window)
		self.panel_right = tk.Frame(master=self.window)			
		
		self.panel_left.grid(row=0, column=0)
		self.panel_center.grid(row=0, column=1)
		self.panel_right.grid(row=0, column=2)
		
		splashscreen = Image.open("NXP_PCF8577C_small.jpg")
		ss_width = splashscreen.width
		ss_height = splashscreen.height		
		desired_height = 500
		factor = desired_height / ss_height
		splashscreen = splashscreen.resize((int(ss_width * factor), int(ss_height * factor)), Image.ANTIALIAS)
		self.splashscreen = ImageTk.PhotoImage(splashscreen)
		self.label_splashscreen = tk.Label(master=self.panel_right, image=self.splashscreen)
		self.label_splashscreen.grid(row=0, column=0)
		
		self.window.wm_title("Reticle Map")
		self.window.mainloop()
		
class WaferWindow:
	def __init__(self):
		self.window = None
		self.reticle_window = None
		
	def edit_reticle(self, event):
		self.reticle_window = ReticleWindow(self.window)
		self.reticle_window.run()
		
	def generate_wafer(self, event):
		pass
		
	def run(self):
		self.window = tk.Tk()
		
		# Instantiate widgets
		
		self.panel_left = tk.Frame(master=self.window)
		self.panel_right = tk.Frame(master=self.window)
		
		self.label_diameter = tk.Label(master=self.panel_left, text="Diameter")
		self.label_background = tk.Label(master=self.panel_left, text="Background")
		self.label_reticle_start = tk.Label(master=self.panel_left, text="Reticle Start")
		self.label_reticle_spacing = tk.Label(master=self.panel_left, text="Reticle Spacing")
		self.label_reticle_repetition = tk.Label(master=self.panel_left, text="Repetition")

		self.entry_diameter = tk.Entry(master=self.panel_left)
		self.entry_background = tk.Entry(master=self.panel_left)		
		self.entry_reticle_start = tk.Entry(master=self.panel_left)
		self.entry_reticle_spacing = tk.Entry(master=self.panel_left)
		self.entry_reticle_repetition = tk.Entry(master=self.panel_left)		
		
		self.button_edit = tk.Button(master=self.panel_left, text="Edit")
		self.button_generate = tk.Button(master=self.panel_left, text="Generate")
		
		# Bind widgets

		self.button_edit.bind("<Button-1>", self.edit_reticle)
		self.button_generate.bind("<Button-1>", self.generate_wafer)		

		# Position widgets

		self.panel_left.grid(row=0, column=0)
		self.panel_right.grid(row=0, column=1)
	
		self.label_diameter.grid(row=0, column=0)
		self.label_background.grid(row=1, column=0)
		self.label_reticle_start.grid(row=2, column=0)
		self.label_reticle_spacing.grid(row=3, column=0)
		self.label_reticle_repetition.grid(row=4, column=0)
		
		self.entry_diameter.grid(row=0, column=1)
		self.entry_background.grid(row=1, column=1)
		self.entry_reticle_start.grid(row=2, column=1)
		self.entry_reticle_spacing.grid(row=3, column=1)
		self.entry_reticle_repetition.grid(row=4, column=1)
				
		self.button_edit.grid(row=5, column=0)
		self.button_generate.grid(row=5, column=1)
		
		splashscreen = Image.open("Wafer_2_Zoll_bis_8_Zoll_2.jpg")		
		self.splashscreen = ImageTk.PhotoImage(splashscreen)
		self.label_splashscreen = tk.Label(master=self.panel_right, image=self.splashscreen)
		self.label_splashscreen.grid(row=0, column=0)
		
		self.window.wm_title("Wafer Map")
		self.window.mainloop()

class WaffleMaker:
	def __init__(self):
		self.wafer_window = WaferWindow()
		
	def run(self):
		self.wafer_window.run()
		

		
my_waffle_maker = WaffleMaker()
my_waffle_maker.run()

