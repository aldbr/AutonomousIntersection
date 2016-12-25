from visual import *

from VisualEnvironmentFactory import *
from ModelController import *

import sys
sys.path.append('..')
from model.Model import *

class MainController:


	def __init__(self):
		self.scene = VisualEnvironmentFactory.load_from_CSV_file("Classic Intersection" ,"ressources/vClassIntersection.csv", 0)
		self.scene2 = VisualEnvironmentFactory.load_from_CSV_file("Autonomous Intersection" ,"ressources/vAutoIntersection.csv", 600)
		random.seed(140)


	def initialize_simulation(self):
		m1 = ModelController(self.scene, Model())
		m2 = ModelController(self.scene2, Model())

		m1.start()
		m2.start()

		m1.join()
		m2.join()