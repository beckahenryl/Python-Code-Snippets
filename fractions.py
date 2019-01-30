import math

class Fraction:

	#initializer
	def __init__(self, num, den):
		self.num = num
		self.den = den

		#example of checking for exceptions
		try:
			convertNum = int(self.num)
			convertDem = int(self.num)
		except TypeError:
			return '{} and or {} are not integers'.format(self.num, self.den)

	def getNum(self):
		return '{} is the numerator'.format(self.num)
		
	def getDen(self):
		return '{} is the denominator'.format(self.den)
	
	#greatest common denominator
	def getGCD(self):
		findGCD = math.gcd(self.num, self.den)
		return 'GCD of {} and {} is {}'.format(self.num, self.den, findGCD)

	def provideFraction(self):
		return 'Fraction: {}/{}'.format(self.num, self.den)

	#implentation of sub, mult, and div
	def __sub__(self):
		subtract = self.num - self.den
		return '__sub__ implemented: {}'.format(subtract)
	def __mul__(self):
		mult = self.num * self.den
		return '__mul__ implemented: {}'.format(mult)
	def __truediv__(self):
		div = self.num / self.den
		return '__truediv__ implemented: {}'.format(div)	

getFraction = Fraction(2,4)

print (getFraction.getNum())
print (getFraction.getDen())
print (getFraction.getGCD())
print(getFraction.provideFraction())
print (getFraction.__sub__())
print (getFraction.__mul__())
print (getFraction.__truediv__())