class CaffeineBeverage:
	def prepareRecipe(self):
		self.boilWater();
		self.brew();
		self.pourInCup();
		self.addCondiments();

	def boilWater(self):
		print('Boiling water')

	def pourInCup(self):
		print('Pouring into cup');


class Coffee(CaffeineBeverage):
	def brew(self):
		print('Dripping Coffee through filter');

	def addCondiments(self):
		print('Adding Sugar and Milk')

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