#oop in python

import math

class Circle:
	def __init__(self, radius = 1):
		self.radius = radius
		
	def getArea(self):
		return self.radius**2 * math.pi
		
	def getCircumference(self):
		return self.radius*2 * math.pi
		
	def setRadius(self, radius):
		self.radius = radius
		
		
def main():
	circle1 = Circle()
	print("The area of circle with radius",circle1.radius,"is",circle1.getArea())
	
	circle2 = Circle(25)
	print("The area of circle with radius",circle2.radius,"is",circle2.getArea())
	


#private

class Circle:
	def __init__(self, radius = 1):
		self.__radius = radius
		
	def getArea(self):
		return self.__radius**2 * math.pi
		
	def getCircumference(self):
		return self.__radius*2 * math.pi
		
	def setRadius(self, radius):
		self.__radius = radius
	
	def getRadius(self):
		return self.__radius