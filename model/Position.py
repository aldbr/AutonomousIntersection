
class Position:
	"""Position management"""

	def __init__(self, x, y):
		self._x = x
		self._y = y

	def _get_x(self):
		return self._x
	def _set_x(self, x):
		self.x = x
	x = property(_get_x, _set_x)

	def _get_y(self):
		return self._y
	def _set_y(self, y):
		self.y = y
	y = property(_get_y, _set_y)

