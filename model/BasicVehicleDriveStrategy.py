from Vehicle import *
from DriveStrategy import *

from abc import ABCMeta, abstractmethod

class BasicVehicleDriveStrategy(DriveStrategy):
	__metaclass__=ABCMeta

	@abstractmethod
	def drive(self, vehicle):
		pass