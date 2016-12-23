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

		#v1 = BasicVehicle(t.paths[random.randint(1, len(t.paths))-1])
		#v2 = BasicVehicle(t.paths[random.randint(1, len(t.paths))-1])
		
		v1 = BasicVehicle(t.paths[0])
		v2 = BasicVehicle(t.paths[1])
		v3 = BasicVehicle(t.paths[2])
		v4 = BasicVehicle(t.paths[3])
		v5 = BasicVehicle(t.paths[4])
		v6 = BasicVehicle(t.paths[5])
		v7 = BasicVehicle(t.paths[6])
		v8 = BasicVehicle(t.paths[7])
		v9 = BasicVehicle(t.paths[8])
		v10 = BasicVehicle(t.paths[9])
		v11 = BasicVehicle(t.paths[10])
		v12 = BasicVehicle(t.paths[11])
	
		self.scene.mouse.getclick()
		v1.start()
		v2.start()
		v3.start()
		v4.start()
		v5.start()
		v6.start()
		v7.start()
		v8.start()
		v9.start()
		v10.start()
		v11.start()
		v12.start()

		while(1):
			
			b1 = box(display=self.scene, pos=(v1.position.x, 2.5, v1.position.y), length=2, height=2, width=2, color=color.white)
			b2 = box(display=self.scene, pos=(v2.position.x, 2.5, v2.position.y), length=2, height=2, width=2, color=color.white)
			b3 = box(display=self.scene, pos=(v3.position.x, 2.5, v3.position.y), length=2, height=2, width=2, color=color.white)
			b4 = box(display=self.scene, pos=(v4.position.x, 2.5, v4.position.y), length=2, height=2, width=2, color=color.white)
			b5 = box(display=self.scene, pos=(v5.position.x, 2.5, v5.position.y), length=2, height=2, width=2, color=color.white)
			b6 = box(display=self.scene, pos=(v6.position.x, 2.5, v6.position.y), length=2, height=2, width=2, color=color.white)
			b7 = box(display=self.scene, pos=(v7.position.x, 2.5, v7.position.y), length=2, height=2, width=2, color=color.white)
			b8 = box(display=self.scene, pos=(v8.position.x, 2.5, v8.position.y), length=2, height=2, width=2, color=color.white)
			b9 = box(display=self.scene, pos=(v9.position.x, 2.5, v9.position.y), length=2, height=2, width=2, color=color.white)
			b10 = box(display=self.scene, pos=(v10.position.x, 2.5, v10.position.y), length=2, height=2, width=2, color=color.white)
			b11 = box(display=self.scene, pos=(v11.position.x, 2.5, v11.position.y), length=2, height=2, width=2, color=color.white)
			b12 = box(display=self.scene, pos=(v12.position.x, 2.5, v12.position.y), length=2, height=2, width=2, color=color.white)
			rate(20)
			b1.visible = 0
			b2.visible = 0
			b3.visible = 0
			b4.visible = 0
			b5.visible = 0
			b6.visible = 0
			b7.visible = 0
			b8.visible = 0
			b9.visible = 0
			b10.visible = 0
			b11.visible = 0
			b12.visible = 0
			del b1
			del b2
			del b3
			del b4
			del b5
			del b6
			del b7
			del b8
			del b9
			del b10
			del b11
			del b12
