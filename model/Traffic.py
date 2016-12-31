from TrafficPathFactory import *
from KmUnityConverter import *

from abc import ABCMeta, abstractmethod
from threading import Thread

class Traffic(Thread):
	__metaclass__=ABCMeta

	def __init__(self, filename):
		Thread.__init__(self)
		self._paths = TrafficPathFactory.load_from_CSV_src_dst_file(filename, KMUnityConverter.step)

	def _get_paths(self):
		return self._paths
	def _set_paths(self, paths):
		self._paths = paths
	paths = property(_get_paths, _set_paths)


	@abstractmethod
	def __getitem__(self, index):
		pass

	@abstractmethod
	def __delitem__(self, index):
		pass

	@abstractmethod
	def run(self):
		pass
	
