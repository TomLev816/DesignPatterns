
class Duck:
	def quack(self):
		print('Quack')

	def fly(self):
		print('Im flying')

class Turkey: 
	def gobble(self):
		print('Gobble gobble')

	def fly(self):
		print('Im flying a short distance')


class TurkeyAdapter:
	def __init__(self, turkey):
		self.turkey = turkey;

	def quack(self):
		self.turkey.gobble();

	def fly(self):
		i =0 
		while(i <= 5):
			i += 1
			self.turkey.fly()
   

def testDuck(duck):
	print('The Duck says ')
	duck.quack()
	duck.fly()

def testTurkey(turkey):
	print('Turkey says ') 
	turkey.gobble()
	turkey.fly()

print('============')
mallard = Duck()
testDuck(mallard)

print('============')
wildTurkey = Turkey()
testTurkey(wildTurkey)

print('============')
adaptedTurkey = TurkeyAdapter(wildTurkey)
testDuck(adaptedTurkey)


