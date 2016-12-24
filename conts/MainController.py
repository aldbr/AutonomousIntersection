from visual import *
import random

import sys
sys.path.append('..')
from model.Path import *
from model.BasicVehicle import *
from model.Position import *
from model.IntersectionTraffic import *

class MainController:


	def __init__(self):
		self.scene = display(title='Classic intersection',
     x=0, y=0, width=600, height=600,
     center=(5,0,0), background=(0.62,0.90,0.33), forward=-vector(0.25,0.25,0.25))

		self.scene2 = display(title='Autonomous intersection',
     x=0, y=0, width=600, height=600,
     center=(5,0,0), background=(0.62,0.90,0.33), forward=-vector(0.25,0.25,0.25))


		distant_light(display=self.scene, direction=(1,0,1), color=(0.62,0.90,0.33))
		distant_light(display=self.scene2, direction=(1,0,1), color=(0.62,0.90,0.33))

		#creation de l'environnement autonome
		aintersection = box(display=self.scene2, pos=(0,0,0), length=10, height=0.5, width=10, color=color.gray(0.5))

		aroad1 = box(display=self.scene2, pos=(0,0,20), length=10, height=0.5, width=30, color=color.gray(0.5))
		aroad2 = box(display=self.scene2, pos=(0,0,-20), length=10, height=0.5, width=30, color=color.gray(0.5))
		aroad3 = box(display=self.scene2, pos=(20,0,0), length=30, height=0.5, width=10, color=color.gray(0.5))
		aroad4 = box(display=self.scene2, pos=(-20,0,0), length=30, height=0.5, width=10, color=color.gray(0.5))

		adelim1 = box(display=self.scene2, pos=(0,0.1,20), length=0.2, height=0.5, width=30)
		adelim1 = box(display=self.scene2, pos=(0,0.1,-20), length=0.2, height=0.5, width=30)
		adelim1 = box(display=self.scene2, pos=(20,0.1,0), length=30, height=0.5, width=0.2)
		adelim1 = box(display=self.scene2, pos=(-20,0.1,0), length=30, height=0.5, width=0.2)


		#creation de l'environnement classique
		intersection = box(display=self.scene, pos=(0,0,0), length=10, height=0.5, width=10, color=color.gray(0.5))

		road1 = box(display=self.scene, pos=(0,0,20), length=10, height=0.5, width=30, color=color.gray(0.5))
		road2 = box(display=self.scene, pos=(0,0,-20), length=10, height=0.5, width=30, color=color.gray(0.5))
		road3 = box(display=self.scene, pos=(20,0,0), length=30, height=0.5, width=10, color=color.gray(0.5))
		road4 = box(display=self.scene, pos=(-20,0,0), length=30, height=0.5, width=10, color=color.gray(0.5))

		delim1 = box(display=self.scene, pos=(0,0.1,20), length=0.2, height=0.5, width=30)
		delim1 = box(display=self.scene, pos=(0,0.1,-20), length=0.2, height=0.5, width=30)
		delim1 = box(display=self.scene, pos=(20,0.1,0), length=30, height=0.5, width=0.2)
		delim1 = box(display=self.scene, pos=(-20,0.1,0), length=30, height=0.5, width=0.2)

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

