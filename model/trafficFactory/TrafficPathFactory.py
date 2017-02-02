import sys
import os
CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
PARENT_FOLDER = os.path.dirname(CURRENT_FOLDER)
sys.path.append(PARENT_FOLDER)
from path.Path import *
from converter.KmUnityConverter import *
from TrafficFactory import *
from path.Light import *
from path.Coordinate import *

class TrafficPathFactory(TrafficFactory):
	"""Factory of traffic paths"""

	@classmethod
	def frange(cls, x, y, jump):
		if x < y:
			while x < y:
				yield x
				x += jump
		else:
			while x > y:
				yield x
				x -= jump

	@classmethod
	def load_from_CSV_file(cls, filename):
		"""Load paths from CSVFile which must only contains path with 
				source and destination postions, and roadsigns present on the path :
				#nb//x1, y1, x2, y2//nbsigns//x, y,axis
				1
				2.5, 34, 2.5, -34, 270
				1
				light, 2.5, 7, 90
				...
				probably not stable at the moment"""
		paths = []
		step = KMUnityConverter.step
		with open(filename, "r") as filePath:
			filePath.readline()
			
			line = filePath.readline()
			while line:
				p = Path([], [])

				nb = int(line)
				for i in range(nb):
					line = filePath.readline()
					
					(x, y, x2, y2, axis) = line.split(",")
					x = float(x)
					y = float(y)
					x2 = float(x2)
					y2 = float(y2)
					axis = float(axis)


					xlist = []
					ylist = []
					if x == x2:
						ylist = list(cls.frange(y,y2,step))
						for i in ylist:
							xlist.append(x)
					elif y == y2:
						xlist = list(cls.frange(x,x2,step))
						for i in xlist:
							ylist.append(y)
					else:
						xlist = list(cls.frange(x,x2,step))
						ylist = list(cls.frange(y,y2,step))

					positions = zip(xlist,ylist)
					for pos in positions:
							p.positions.append(Position(Coordinate(pos[0], pos[1]), Coordinate(axis, None)))
				
				line = filePath.readline()
				nb = int(line)
				for i in range(nb):
					line = filePath.readline()
					(sign, x, y, axis) = line.split(",")
					x = float(x)
					y = float(y)
					axis = float(axis)

					s = None
					if sign == "light":
						s = Light(Position(Coordinate(x,y), Coordinate(axis,None)))

					if s != None:
						p.signs.append(s)

				line = filePath.readline()
				paths.append(p)
		return paths