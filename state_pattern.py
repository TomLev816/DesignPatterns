SOLD_OUT = 0
NO_QUARTER = 1
HAS_QUARTER = 2
SOLD = 3;

class GumballMachine:
	def __init__(self, count):
		self.state = SOLD_OUT
		self.count = count
		if (count > 0):
			self.state = NO_QUARTER
	
	def insertQuarter(self):
		if (self.state == HAS_QUARTER):
			print('You cant insert another quarter')
		elif (self.state == NO_QUARTER):
			self.state = HAS_QUARTER;
			print('You inserted a quarter')
		elif (self.state == SOLD_OUT):
			print('You cant insert a quarter, the machine is sold out')
		elif (self.state == SOLD):
			print('Please wait, were already giving you a gumball')

	def ejectQuarter(self):
		if (self.state == HAS_QUARTER):
			print('Quarter returned');
			self.state = NO_QUARTER;
		elif (self.state == NO_QUARTER):
			print('You havent inserted a quarter');
		elif (self.state == SOLD):
			print('Sorry, you already turned the crank')
		elif (self.state == SOLD_OUT):
			print('You cant eject, you havent inserted a quarter yet')

	def turnCrank(self):
		if (self.state == SOLD):
			print('Turning twice doesnt get you another gumball!')
		elif (self.state == NO_QUARTER):
			print('You turned but theres no quarter')
		elif (self.state == SOLD_OUT):
			print('You turned, but there are no gumballs')
		elif (self.state == HAS_QUARTER):
			print('You turned...')
			self.state = SOLD;
			self.dispense();

	def dispense(self):
		if (self.state == SOLD):
			print('A gumball comes rolling out the slot')
			self.count = self.count - 1
			if (self.count == 0):
				print('Oops, out of gumballs!');
				self.state = SOLD_OUT
			else:
				self.state = NO_QUARTER;
		elif(self.state == NO_QUARTER):
			print('You need to pay first')
		elif(self.state == SOLD_OUT):
			print('No gumball dispensed');
		elif (self.state == HAS_QUARTER):
			print('No gumball dispensed');

def test():
	gumballMachine = GumballMachine(5)
	print(gumballMachine.count);
	gumballMachine.insertQuarter()
	gumballMachine.turnCrank();
	print(gumballMachine.count);
	gumballMachine.insertQuarter()
	gumballMachine.ejectQuarter()
	gumballMachine.turnCrank();
	print(gumballMachine.count);
	gumballMachine.insertQuarter()
	gumballMachine.turnCrank()
	gumballMachine.insertQuarter()
	gumballMachine.turnCrank()
	gumballMachine.ejectQuarter();
	print(gumballMachine.count);
	gumballMachine.insertQuarter()
	gumballMachine.insertQuarter()
	gumballMachine.turnCrank()
	gumballMachine.insertQuarter()
	gumballMachine.turnCrank()
	gumballMachine.insertQuarter()
	gumballMachine.turnCrank();
	print(gumballMachine.count)

test()
#####################NEW#####################
class GumballMachine:

State soldOutState; State noQuarterState; State hasQuarterState; State soldState;
State state = soldOutState; int count = 0;

def __init__ (self,numberGumballs):
	soldOutState = new SoldOutState(this);
	noQuarterState = new NoQuarterState(this);
	hasQuarterState = new HasQuarterState(this);
	soldState = new SoldState(this);
	this.count = numberGumballs;
	if (numberGumballs > 0):
		state = noQuarterState; 

	def insertQuarter():
		state.insertQuarter();

	def ejectQuarter():
		state.ejectQuarter();

	def turnCrank():
		state.turnCrank(); state.dispense();

void setState(State state) { this.state = state;
}
void releaseBall() {
System.out.println(“A gumball comes rolling out the slot...”); if (count != 0) {
count = count - 1; }
}
// More methods here including getters for each State... }



class NoQuarterState:
	def __init__(self, gumball_machine):
		self.gumball_machine = gumball_machine	

	def insertQuarter():
		print('You inserted a quarter')
		self.gumball_machine.setState(gumball_machine.getHasQuarterState())

	def ejectQuarter():
		print('You haven’t inserted a quarter');

	def turnCrank():
		print('You turned, but there’s no quarter');
	
	def dispense():
		print('You need to pay first')		


class HasQuarterState:
	def __init__(self,gumballMachine):
		self.gumballMachine = gumballMachine;

	def insertQuarter():
		print('You can’t insert another quarter');

	def ejectQuarter():
		print('Quarter returned'); 
		self.gumballMachine.setState(self.gumballMachine.getNoQuarterState());

	def turnCrank():
		print('You turned...'); 
		self.gumballMachine.setState(self.gumballMachine.getSoldState());

	def dispense():
		print('No gumball dispensed');


class SoldState:
	def __init__(self,gumballMachine):
		self.gumballMachine = gumballMachine;

	def insertQuarter():
		print('Please wait, we’re already giving you a gumball');

	def ejectQuarter():
		print('Sorry, you already turned the crank');

	def turnCrank():
		print('Turning twice doesn’t get you another gumball!');

	def dispense():
		self.gumballMachine.releaseBall();
		if (self.gumballMachine.getCount() > 0):
			self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
     	else:
     		print('Oops, out of gumballs!');
			self.gumballMachine.setState(self.gumballMachine.getSoldOutState());


class SoldOutState:
	def __init__(self, gumballMachine)
		self.gumballMachine = gumballMachine;

	def insertQuarter():
		print('You can’t insert a quarter, the machine is sold out');

	def ejectQuarter():
		print('You can’t eject, you haven’t inserted a quarter yet');

	def turnCrank():
		print('You turned, but there are no gumballs');

	def dispense():
		print('No gumball dispensed')