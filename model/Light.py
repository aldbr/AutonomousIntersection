from RoadSign import *

class Light(RoadSign):

	def __init__(self, position):
		RoadSign.__init__(self,position)
		self.is_green = False