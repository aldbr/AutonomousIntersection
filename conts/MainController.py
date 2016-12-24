from visual import *

from VisualEnvironmentFactory import *
from ModelController import *

class MainController:


	def __init__(self):
		self.scene = VisualEnvironmentFactory.load_from_CSV_file("Classic Intersection" ,"ressources/vClassIntersection.csv", 0)
		self.scene2 = VisualEnvironmentFactory.load_from_CSV_file("Autonomous Intersection" ,"ressources/vAutoIntersection.csv", 600)
		random.seed(140)


	def initialize_simulation(self):
		m1 = ModelController(self.scene)
		m2 = ModelController(self.scene2)

		m1.start()
		m2.start()

		m1.join()
		m2.join()
		#random.seed(140)
		#t = IntersectionTraffic("ressources/intersectionPaths.csv")
#
		#vehicles = []
		#boxes = []
		#i = 0
		#while i < 10:
		#	vehicles.append(BasicVehicle(t.paths[random.randint(1, len(t.paths))-1]))
		#	i += 1
#
#
		#for v in vehicles:
		#	v.start()
#
		#while(vehicles):
		#	i = 0
		#	while i < len(vehicles):
		#		pos = vehicles[i].position
		#		if pos is not None:
		#			boxes.append(box(display=self.scene, pos=(pos.x, 2.5, pos.y), \
		#				length=2, height=2, width=2, color=color.red))
		#		else:
		#			vehicles[i].join()
		#			del vehicles[i]
#
		#		i += 1
		#	rate(20)
		#	i = 0
		#	while i < len(boxes):
		#		boxes[i].visible = 0
		#		i += 1
		#	del boxes[:]

