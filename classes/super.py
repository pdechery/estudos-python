class Rectangle:
	def __init__(self, length, width):
		print('Rectangle init')
		self.length = length
		self.width = width

	def area(self):
		return self.length * self.width

	def perimeter(self):
		return 2 * self.length + 2 * self.width


class Square(Rectangle):
	def __init__(self, length):
		print('Square init')
		# Calling super class' __init__ so that I can change its signature
		super().__init__(length, length)

	def me(self):
		'''
		Even if this doesn't use any properties from the class or the super-class __init__ funcion will be called
		'''
		return "I\'m a Square"

class Cube(Square):
	'''
	No __init__ here. 
	But parent's class __init__ will be called on instantiation.
	'''
	def surface_area(self):
		face_area = super().area() # that's a delegate object to a parent class, Rectangle (where area() is defined)
		return face_area * 6

	def volume(self):
		face_area = super().area()
		return face_area * self.length

if __name__ == '__main__':

	sq = Square(4)
	print(sq.me())

	cb = Cube(4)
	print(cb.surface_area())
	print(cb.area())