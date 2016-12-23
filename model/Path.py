from Position import *


class Path:

	def __init__(self, positions):
		self._positions = positions

	def _get_positions(self):
		return self._positions
	def _set_positions(self, positions):
		pass
	positions = property(_get_positions,_set_positions)
