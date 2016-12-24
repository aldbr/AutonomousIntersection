from visual import *
import random

from VisualEnvironmentFactory import *

import sys
sys.path.append('..')
from model.Path import *
from model.BasicVehicle import *
from model.Position import *
from model.IntersectionTraffic import *

class MainController:


	def __init__(self):
		self.scene = VisualEnvironmentFactory.loadFromCSVFile("Classic Intersection" ,"ressources/vClassIntersection.csv", 0)
		self.scene2 = VisualEnvironmentFactory.loadFromCSVFile("Autonomous Intersection" ,"ressources/vAutoIntersection.csv", 600)


	def initialize_simulation(self):
		random.seed(140)
		t = IntersectionTraffic("ressources/intersectionPaths.csv")

		vehicles = []
		boxes = []
		i = 0
		while i < 11:
			vehicles.append(BasicVehicle(t.paths[random.randint(1, len(t.paths))-1]))
			i += 1


		for v in vehicles:
			v.start()

		while(vehicles):
			i = 0
			while i < len(vehicles):
				pos = vehicles[i].position
				if pos is not None:
					boxes.append(box(display=self.scene, pos=(pos.x, 2.5, pos.y), \
						length=2, height=2, width=2, color=color.white))
				else:
					vehicles[i].join()
					del vehicles[i]

				i += 1
			rate(20)
			i = 0
			while i < len(boxes):
				boxes[i].visible = 0
				i += 1
			del boxes[:]

