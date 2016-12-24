from Path import *

class TrafficPathFactory:

	@staticmethod
	def load_from_CSV_file(filename):
		paths = []
		with open(filename, "r") as filePath:
			filePath.readline()
			line = filePath.readline()
			
			while line :
				p = Path([])
				(num, x, y) = line.split(",")
				numRef = num
				
				while line and numRef == num :
					num = int(num)
					x = float(x)
					y = float(y)
					p.positions.append(Position(x,y))
					line = filePath.readline()
					if(line):
						(num, x, y) = line.split(",")
				
				paths.append(p)
		return paths
