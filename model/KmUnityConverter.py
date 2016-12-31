import math


class KMUnityConverter:

	step = 0.001

	@classmethod
	def convert_unit_to_KmH(cls):
		pass

	@classmethod
	def convert_KmH_to_unit(cls,kmh):
		km = kmh * (0.05/3600) #1 unity per 0.05s
		m = km * 1000
		u = m / (0.7*cls.step) #0.0007m = 0.001u
		return int(round(u))




