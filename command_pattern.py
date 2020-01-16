#  Command Pattern
# Client -> Command -> Invoker -> Command -> Reciver

class RemoteControl: # Invoker
	def __init__(self):
		self.commands = []
		self.lastCommand = 0

	def setCommand(self, command):
		self.commands.append(command)

	def buttonWasPressed(self, slotInt):
		self.lastCommand = self.commands[slotInt]
		self.commands[slotInt].execute()

	def undoButtonWasPressed(self):
		self.lastCommand.unExecute()

################ Commands ###################

class LightOnCommand: #Command
	def __init__(self, light):
		self.light = light

	def execute(self):
		self.light.on()

	def unExecute(self):
		self.light.off()

class LightOffCommand: #Command
	def __init__(self, light):
		self.light = light

	def execute(self):
		self.light.off()

	def unExecute(self):
		self.light.on()


############## Recievers ######################

class Light: #Reciever
	def __init__(self, name):
		self.name = name

	def on(self):
		print('=========================')
		print(self.name + ' Light is on')
		print('')

	def off(self):
		print('=========================')
		print('Light is off')	
		print('')

class Fan: #Reciever
	def __init__(self, name):
		self.name = name

	def on(self):
		print(self.name + ' Fan is on')

	def off(self):
		print('Fan is off')	

############## Remote ######################

def createRemote(name):
	remote = RemoteControl()
	light =  Light(name)
	lightOn = LightOnCommand(light)
	lightOff = LightOffCommand(light)
	remote.setCommand(lightOn)
	remote.setCommand(lightOff)
	return remote

def showRemote(remote):
	print('0 - Light on')
	print('1 - Light off')
	print('2 - Undo')
	print('3 - Exit')

	userInput = int(raw_input('Press a button: '))

	if ( userInput  <= 1):
		remote.buttonWasPressed(userInput)
		showRemote(remote)		
	elif (userInput  == 2):
		remote.undoButtonWasPressed()
		showRemote(remote)
	else:
		return 0

userInput = raw_input('Enter room Light is in : ')	
remote = createRemote(userInput)
showRemote(remote)





