class Animal:
	def __init__(self, legs = 4, eyes = 2, tail = 1, ears = 2):
		self.legs = legs
		self.eyes = eyes
		self.tail = tail
		self.ears = ears
 
class domestic_animals(Animal):
	def place(self):
		print('humans surroundings')

class wild_animals(Animal):
	def __init__(self, legs = 4, eyes = 2, tail = 1, ears = 2):
		Animal.__init__(self, legs = 4, eyes = 2, tail = 1, ears = 2)
	def place(self):
		print("forest")


class herbivores(wild_animals):
	def  __init__(self, legs = 4, eyes = 2, tail = 1, ears = 2):
		super().__init__(legs = 4, eyes = 2, tail = 1, ears = 2)
	def food(self):
                print("leaves")

class carnivores(wild_animals):
	def food(self):
		print("other animals") 

class lion(carnivores):
    def speak(self):
        print("Roar")
    def colour(self):
        print("Yellow")

class tiger(carnivores):
    def speak(self):
        print("Roar")
    def colour(self):
        print("Yellowish Orange and black stripes")
        
class antelope(herbivores):
    def colour(self):
        print("Black")
        
class elephant(herbivores):
	def speak(self):
		print("trumpet")
	def colour(self):
		print("Grey")
	def food(self):
		herbivores().food()  #overloading
		print("grass")

class hyena(herbivores):
    def colour(self):
        print("brown")

class cat(domestic_animals):
    def speak(self):
        print("meow")
    def colour(self):
        print("brown, white, black")


class dog(domestic_animals):
    def speak(self):
        print("bark")
    def colour(self):
        print("Orange,brown, black, white")
        
        
class cow(Domestic_animals):
    def speak(self):
        print("moo")
    def colour(self):
        print("white, brown, orange")


tommy = cat()
print("tommy.legs = ", tommy.legs)
print("tommy.place = ")
tommy.place()
print("tommy.colour = ") 
tommy.colour()
print("tommy.speak = ") 
tommy.speak()
ele1 = elephant()
print("ele1.legs = ", ele1.legs)
print("ele1.food = ")
ele1.food()
