import tkinter as tk
from PIL import Image, ImageTk


class Device:
	def __init__(self):
		self.device_name = None
		#self.image_file = None
		self.device_file = None
		self.device_size = (0, 0)
		self.device_location = (0, 0)
		self.pixels_per_micrometer = 0
		
class Chip:
	def __init__(self):
		self.devices = []
		self.chip_size = (0, 0)
		self.chip_location = (0, 0)
		self.pixels_per_micrometer = 0
		
class Reticle:
	def __init__(self):
		self.chips = []
		self.devices = []		
		
		self.reticle_size = (0, 0)
		self.pixels_per_micrometer = 0

class Wafer:
	def __init__(self,
		diameter,
		reticle,
		reticle_start,
		reticle_spacing,
		reticle_repetition,
		background):
		self.diameter = diameter
		self.reticle = reticle
		self.reticle_start = reticle_start
		self.reticle_spacing = reticle_spacing
		self.reticle_repetition = reticle_repetition
		self.background = background

class DeviceWindow:
	def __init__(self):
		pass
		
	def run(self):
		pass
		
class ChipWindow:
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
		
		# Instantiate widgets
		
		self.panel_left = tk.Frame(master=self.window)
		self.panel_center = tk.Frame(master=self.window)
		self.panel_right = tk.Frame(master=self.window)
		
		self.panel_center_top = tk.Frame(master=self.panel_center)
		self.panel_center_bottom = tk.Frame(master=self.panel_center)

		self.device_name = None
		self.image_file = None
		self.device_size = (0, 0)
		self.device_location = (0, 0)
		self.pixels_per_micrometer = 0
		
		self.label_device_name = tk.Label(master=self.panel_left, text="Device Name")
		self.label_device_file = tk.Label(master=self.panel_left, text="Image File")
		self.label_device_size = tk.Label(master=self.panel_left, text="Device Size")
		self.label_device_location = tk.Label(master=self.panel_left, text="Device Location")
		self.label_device_length = tk.Label(master=self.panel_left, text="Device Pixels per Micrometer")		

		self.entry_device_name = tk.Entry(master=self.panel_left)
		self.entry_device_file = tk.Entry(master=self.panel_left)
		self.entry_device_size = tk.Entry(master=self.panel_left)
		self.entry_device_location = tk.Entry(master=self.panel_left)
		self.entry_device_length = tk.Entry(master=self.panel_left)		
			
		self.button_add = tk.Button(master=self.panel_left, text="Add")
		self.button_remove = tk.Button(master=self.panel_left, text="Remove")
		
		self.list_devices = tk.Listbox(master=self.panel_center_top)
		self.text_device_info = tk.Text(master=self.panel_center_bottom, width=24)
		
		# Position widgets
		
		self.panel_left.grid(row=0, column=0)
		self.panel_center.grid(row=0, column=1)
		self.panel_right.grid(row=0, column=2)
		
		self.panel_center_top.grid(row=0, column=0)
		self.panel_center_bottom.grid(row=1, column=0)
		
		self.list_devices.pack()
		self.text_device_info.pack()
		
		self.label_device_name.grid(row=0, column=0)
		self.entry_device_name.grid(row=0, column=1)
		self.label_device_file.grid(row=1, column=0)
		self.entry_device_file.grid(row=1, column=1)
		self.label_device_size.grid(row=2, column=0)
		self.entry_device_size.grid(row=2, column=1)
		self.label_device_location.grid(row=3, column=0)
		self.entry_device_location.grid(row=3, column=1)		
		self.label_device_length.grid(row=4, column=0)
		self.entry_device_length.grid(row=4, column=1)
		
		self.button_add.grid(row=5, column=0)
		self.button_remove.grid(row=5, column=1)
		
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
		self.current_reticle = None
		self.current_wafer = None
		
	def edit_reticle(self, event):
		self.reticle_window = ReticleWindow(self.window)
		self.reticle_window.run()
		
	def generate_wafer(self, event):
		self.current_wafer = self.parse_wafer()
		self.update_wafer_image()
		
	def parse_wafer(self):
		diameter = float(self.entry_diameter.get())
		background = self.entry_background.get()
		start = [float(temporary.strip(',')) for temporary in self.entry_reticle_start.get().strip('()').split()]		
		spacing = [float(temporary.strip(',')) for temporary in self.entry_reticle_spacing.get().strip('()').split()]
		repetition = [float(temporary.strip(',')) for temporary in self.entry_reticle_repetition.get().strip('()').split()]
		
		return Wafer(diameter=diameter,
			reticle=self.current_reticle,
			reticle_start=start,
			reticle_spacing=spacing,
			reticle_repetition=repetition,
			background=background)
			
	def update_wafer_image(self):
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

