from visual import *

class VisualEnvironmentFactory:
	"""Road environment factory"""

	@staticmethod
	def load_from_CSV_file(name, filename, position):
		"""Load an environment from a CSV file : not stable at the moment"""
		scene = display(title=name,x=position, y=0, width=600, height=600, \
			center=(1,0,0), background=(0.62,0.90,0.33), forward=-vector(0.25,0.25,0.25))
		distant_light(display=scene, direction=(1,0,1), color=(0.62,0.90,0.33))
		with open(filename, "r") as filePath:
			filePath.readline()
			line = filePath.readline()
			while line :
				obj = line.split(",")
				typeObj = obj[0]
				
				if typeObj == "box":
					box(display=scene, pos=(float(obj[1]),float(obj[2]),float(obj[3])), length=float(obj[4]), \
						height=float(obj[5]), width=float(obj[6]), color=(float(obj[7]), float(obj[8]), float(obj[9])))
				elif typeObj == "curve": #Warning : not stable
					curve(display=scene, pos=[(float(obj[1]),float(obj[2]),float(obj[3])),(float(obj[4]),float(obj[5]),float(obj[6])),(float(obj[7])\
						,float(obj[8]),float(obj[9]))], radius=float(obj[10]), color=(float(obj[11]), float(obj[12]), float(obj[13])))
				
				line = filePath.readline()
		return scene