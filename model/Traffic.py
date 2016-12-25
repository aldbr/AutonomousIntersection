from TrafficPathFactory import *

class Traffic:

	def __init__(self, filename):
		self._paths = TrafficPathFactory.load_from_CSV_src_dst_file(filename, 0.1)

	def _get_paths(self):
		return self._paths
	def _set_paths(self, paths):
		self._paths = paths
	paths = property(_get_paths, _set_paths)
	
