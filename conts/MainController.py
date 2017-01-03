from visual import *

from VisualEnvironmentFactory import *
from ModelController import *

import sys
sys.path.append('..')
from model.Model import *
from model.ClassicTrafficIntersection import *

class MainController:
	"""Main windows management"""


	def __init__(self):
		self.scene = VisualEnvironmentFactory.load_from_CSV_file("Classic Intersection" ,"ressources/vClassIntersection.csv", 0)
		self.scene2 = VisualEnvironmentFactory.load_from_CSV_file("Autonomous Intersection" ,"ressources/vAutoIntersection.csv", 600)


	def initialize_simulation(self):
		"""Initialize simulations"""
		m1 = ModelController(self.scene, Model(ClassicTrafficIntersection\
			("ressources/intersectionPaths.csv","ressources/lightPosition.csv")))
		m2 = ModelController(self.scene2, Model(ClassicTrafficIntersection\
			("ressources/intersectionPaths.csv","ressources/lightPosition.csv")))

		m1.start()
		m2.start()

		m1.join()
		m2.join()