from threading import Thread
from visual import *
import random

import sys
sys.path.append('..')
from model.Path import *
from model.BasicVehicle import *
from model.Position import *
from model.IntersectionTraffic import *
from model.Model import *

class ModelController(Thread):

	def __init__(self, scene, model):
		Thread.__init__(self)
		self.scene = scene
		self.model = model

	def run(self):
			boxes = []
			
			self.model.start()
			while 1 :
				i = 0
				
				size = len(self.model.vehicles)
				while i < size:
					pos = self.model.vehicles[i].position
					if pos is not None:
						boxes.append(box(display=self.scene, pos=(pos.x, 2.5, pos.y), \
							length=2, height=2, width=2, color=color.red))
					else:
						self.model.vehicles[i].join()
						self.model.count -= 1
						size -= 1
						del self.model.vehicles[i]

					i += 1
				rate(500)

				for b in boxes:
					b.visible = 0
				del boxes[:]

			self.model.join()