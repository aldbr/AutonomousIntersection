from abc import ABCMeta, abstractmethod

class TrafficFactory:
	__metaclass__=ABCMeta

	@abstractmethod
	def load_from_CSV_file(cls, filename):
		pass
