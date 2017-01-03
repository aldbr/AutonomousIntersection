from TrafficFactory import *
from Position import *

class LightFactory(TrafficFactory):
	"""Factory of light positions"""


	@classmethod
	def load_from_CSV_file(cls, filename):
		"""Load light positions from CSVFile :
				#num, x, y
				0, 7, 2.5,
				0, -7, -2.5,
				...
				not stable at the moment"""
		lights = []
		with open(filename, "r") as filePath:
			filePath.readline()
			line = filePath.readline()
			
			while line :
				(num, x, y) = line.split(",")
				
				x = float(x)
				y = float(y)

				lights.append(Position(x,y))
					
				line = filePath.readline()
		return lights