from Position import *


class Path:
	"""Path management for vehicle and pedestrian agents"""

	def __init__(self, positions, signs):
		self.positions = positions
		self.signs = signs
