class CaffeineBeverage:
	def prepareRecipe(self):
		self.boilWater();
		self.brew();
		self.pourInCup();
		if(self.customerWantsCondiments()):
			self.addCondiments();

	def boilWater(self):
		print('Boiling water')

	def pourInCup(self):
		print('Pouring into cup');

	def customerWantsCondiments(self):
		return True

class Coffee(CaffeineBeverage):
	def brew(self):
		print('Dripping Coffee through filter');

	def addCondiments(self):
		print('Adding Sugar and Milk')

	def customerWantsCondiments(self):
		print('Do you want condiments?')
		userInput = raw_input('Enter (y/n): ')
		if (userInput.lower() == 'y'):
			return True;
		else:
			return False

class Tea(CaffeineBeverage):
	def brew(self):
		print('Steeping the tea');

	def addCondiments(self):
		print('Adding Lemon')

tomCoffee = Coffee()
tomCoffee.prepareRecipe()
print('============')
tomTea = Tea()
tomTea.prepareRecipe()