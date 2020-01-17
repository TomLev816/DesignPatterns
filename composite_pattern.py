class MenuItem():
	def __init__(self, name,description,vegetarian,price):
		self.name = name
		self.description = description
		self.vegetarian = vegetarian
		self.price = price

	def getName(self):
		return self.name;

	def getDescription(self):
		return self.description;

	def getPrice(self):
		return self.price;

	def isVegetarian(self):
		return self.vegetarian;

	def printMenu(self):
		print(self.getName())
		if (self.isVegetarian()):
			print('(v)')
		print(str(self.getPrice()));
		print(' -- ' + self.getDescription())


class Menu():
	def __init__(self, name,description):
		self.name = name;
		self.description = description;
		self.menuComponents = []

	def add(self, menuComponent):
		self.menuComponents.append(menuComponent)

	def remove(self, menuComponent):
		self.menuComponents.remove(menuComponent)

	def getChild(self, i):
		return self.menuComponents.get(i);

	def getName(self):
		return self.name;

	def getDescription(self):
		return self.description;

	def printMenu(self):
		print(self.getName());
		print(self.getDescription())
		print('---------------------');

		for item in self.menuComponents:
			item.printMenu()

class Waitress:
	def __init__(self, allMenus):
		self.allMenus = allMenus;

	def printAllMenu(self):
		self.allMenus.printMenu()



pancakeHouseMenu = Menu('PANCAKE HOUSE MENU', 'Breakfast');
dinerMenu = Menu('DINER MENU', 'Lunch');
cafeMenu = Menu('CAFE MENU', 'Dinner');
dessertMenu = Menu('DESSERT MENU', 'Dessert of course!');

allMenus = Menu('ALL MENUS', 'All menus combined');
allMenus.add(pancakeHouseMenu); 
allMenus.add(dinerMenu); 
allMenus.add(cafeMenu);

# add menu items here
dinerMenu.add(MenuItem('Pasta', 'Spaghetti with Marinara Sauce, and a slice of sourdough bread', True, 3.89));
dinerMenu.add(dessertMenu);
dessertMenu.add(MenuItem( 'Apple Pie','Apple pie with a flakey crust, topped with vanilla icecream', True,1.59));
# add more menu items here

waitress = Waitress(allMenus);
waitress.printAllMenu();








