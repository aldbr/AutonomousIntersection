import unittest

import sys
sys.path.append('..')
from threading import Thread
import time
import numpy

from model.ClassicTrafficIntersection import *
from model.BasicVehicle import *
from conts.VisualEnvironmentFactory import *

class TestVehicle:

	def test_classic_intersection_sharing(self):
		scene = VisualEnvironmentFactory.load_from_CSV_file\
		("Classic Intersection" ,"vClassIntersection.csv", 0)

		traffic = ClassicTrafficIntersection("ressources/intersectionPathsAndSigns.csv")
		traffic.initialize()
		traffic.start()
		count = 0
		while 1 :
			v = BasicVehicle(traffic.paths[4], \
							traffic, None)
			self.traffic.add(v)
			v2 = BasicVehicle(traffic.paths[6], \
							traffic, None)
			traffic.add(v2)
			v.start()
			v2.start()
			count += 2
			
			size = count
			while i < size:
				pos = traffic[i].position
				if pos is not None:
					boxes.append(box(display=self.scene, pos=(pos.localization.x, 2.5, pos.localization.y), \
						length=2, height=2, width=2, color=color.red))
				else:
					traffic[i].join()
					count -= 1
					size -= 1
					del traffic[i]

				i += 1
			rate(50)

			for b in boxes:
				b.visible = 0
			del boxes[:]
			time.sleep(0.5)

#test = TestVehicle()
#test.test_classic_intersection_sharing()

		
        