'''
-class attribute- it is the same for all instances (all dogs)
-to create instance of a class, use the class name following by parenthesis	
-when you create a new instance of the class, python automatically determines what self is and passes it to the init method
-instance methods are defined inside of the class and are used to get contents of an instance
-they can also be used to perform operations with attributes of objects.  the first argument is always self
-inheritance: one class takes on the attributes and methods of another
newly formed classes are called child classes and the classes that
the child classes are derived from are called parent classes
-child classes override/extend the functionality (attributes and behaviors) of parent classes
'''

class Dog(): 
	#class attribute applies to all instances
	species = 'mammal'

	#initializer/ instance attributes
	def __init__(self, name, age, height): #self is used to refer to the object Dog
		self.name = name
		self.age = age
		self.height = height

#instantiate the dog object

philo = Dog("Philo", 5, 50)
mikey = Dog("Mikey", 7, 49)

print (philo.species)

#explaining inheritance below

# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child classes inherit attributes and
# behaviors from the parent class
jim = Bulldog("Jim", 12)
print(jim.description())

# Child classes have specific attributes
# and behaviors as well
print(jim.run("slowly"))
