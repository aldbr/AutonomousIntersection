import math


class KMUnityConverter:

	@classmethod
	def convert_unit_to_KmH(cls):
		pass

	@classmethod
	def convert_KmH_to_unit(cls,kmh):
		km = kmh * (0.05/3600) #1 unity per 0.05s
		m = km * 1000
		u = m / 0.07 #0.07m = 0.1u
		return int(round(u))

#print(KMUnityConverter.convert_KmH_to_unit(5))





