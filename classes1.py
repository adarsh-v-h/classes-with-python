#class is just a blue print of how an object should be built
# object is just an instanace of this class
# we use clases because it is the best way to organize your code...
#to create class we use keyword: class
class Microwave: 
	#first letter of the class should be capital
	# this is a initailizer, which already exists in the code, but we can call and recreate it if want some differet action to be performed
	# here self is the actual instance of the data, we use self.brand = brand for example, to make sure the characters properly stick to the class
	def __init__(self, brand: str, power_rating: float, tunred_on: bool = False) -> None:
		self.brand = brand
		self.power_rating = power_rating
		self.tunred_on = tunred_on # this is a default value
		# we created some characters to any any object of this class,
	def state(self) -> None:
		# this is a method 
		if self.tunred_on:
			print(f"Microwave {self.brand} is turned on")
		else:
			print(f" Microwave {self.brand} is turned off")
	def action(self) -> None:
		if self.tunred_on:
			self.tunred_on = False
		else:
			self.tunred_on = True
	def run(self, second: int) -> None:
		if self.tunred_on:
			print(f"Running {self.brand} for {second} seconds")
		else:
			print("Turning the microwave on")
			self.action()
			print(f"Running {self.brand} for {second} seconds")

	def __add__(self, other):
		return f"{self.brand} + {other.brand}" # returning a string
		# this is a dunder method, which we can bring in to add 2 classes
	
	def __mul__(self,other):
		return self.power_rating * other.power_rating # returns a floating point

	def __str__(self) -> str:
		return f"{self.brand} (Rating: {self.power_rating})"

	def __repr__(self) -> str:
		return f'Microwave(brand = "{self.brand}", power_rating = "{self.power_rating}")'
# repr does the same thing as __str__ but is used like, "Ouput for devlopers", while str is used like "ouput for user"

samsung: Microwave = Microwave("samsung", 8.7) # here we have not menstioned anything about turned_on, but its still their by deault
# we created an instance of class Microwave, which is an object called samsung
#semg = Microwave()
# this also does the same thing, without type anotation, but its good habit to use it
#print(semg)# this will just return an address 
# print(samsung) # the address output: <__main__.Microwave object at 0x0000021C58D5C530>
# print(samsung.brand) # the brand we initialized to it : samsung
# print(samsung.power_rating) # the power_rating we gave : 8.7
# smeg: Microwave = Microwave(brand = "smeg", power_rating = 7.0)
# print(smeg.brand)
# print(smeg.power_rating)

# now we can call those methods and play with them \
samsung.state() # since by deault value the mircowave instance are off
# output: Microwave samsung is turned off

# now we will perform action on the object, i.e changing its state
samsung.action()# this wont output or return anything but, the object now has true for turned_on
# we can again called state method to check its state
samsung.state()
# output: Microwave samsung is turned on

#now we have a method that takes instance and a value, called seoconds
samsung.run(10)
#output: Running samsung for 10 seconds
# since the last last time when we checked state it was on, we ran it normally

#wtif it was off, lets try
samsung.action() # will turn it off
samsung.state() # will say it turned off,
samsung.run(10)
"""
output:
Turning the microwave on
Running samsung for 10 seconds
"""
#if its off, it runs the action function, turns it on, then run's it for 10 seconds(just for saying)

# print(id(samsung.brand))
# print(id(samsung))
# print(id(samsung.power_rating))
# print(id(samsung.tunred_on))
# id is a fun that returns the memory address, even tho they are characters of same object, they have different address

smeg : Microwave = Microwave(brand= "smeg", power_rating = 7.0, tunred_on = True)
print(samsung + smeg) # output: samsung + smeg
# this calles the dunder __add__ method, note that you dont have to explicitly called any method,
# this happens on it own like __init__, which is also a dunder method, any method that starts __ and ends with __ is a dunder method
print(samsung*smeg) # output: 60.89999999999999
# the operators that are being used tells which dunder method to be called
print(smeg)# output: smeg (Rating: 7.0)
# this time, unlike before it won't return the address, but calls dunder method string 

# to call repr, 
print(repr(smeg)) #output: Microwave(brand = "smeg", power_rating = "7.0")

