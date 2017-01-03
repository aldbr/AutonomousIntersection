from Path import *
from KmUnityConverter import *
from TrafficFactory import *

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
				source and destination postions :
				#num, x, y, x2, y2
				0, 0, 2.5, 34, 2.5
				0, 34, 2.5, 34, 34
				...
				not stable at the moment"""
		paths = []
		step = KMUnityConverter.step
		with open(filename, "r") as filePath:
			filePath.readline()
			line = filePath.readline()
			
			while line :
				p = Path([])
				(num, x, y, x2, y2) = line.split(",")
				numRef = num
				
				while line and numRef == num :
					num = int(num)
					x = float(x)
					y = float(y)
					x2 = float(x2)
					y2 = float(y2)

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
						p.positions.append(Position(pos[0], pos[1]))
					
					line = filePath.readline()
					if(line):
						(num, x, y, x2, y2) = line.split(",")
				
				paths.append(p)
		return paths