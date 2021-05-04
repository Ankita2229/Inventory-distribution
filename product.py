class Product:
	def __init__(self, make = None, model = None, model_quantity = None, model_year = None, color = None, price = None):
		self.make = make
		self.model = model
		self.model_quantity = model_quantity
		self.model_year = model_year
		self.color = color
		self.price = price

	def setMake(self, make):
		self.make = make

	def getMake(self):
		return self.make

	def setModel(self, model):
		self.model = model

	def getModel(self):
		return self.model

	def setModelQuantity(self, model_quantity):
		self.model_quantity = model_quantity

	def getModelQuantity(self):
		return self.model_quantity

	def setModelYear(self, model_year):
		self.model_year = model_year

	def getModelYear(self):
		return self.model_year

	def setColor(self, color):
		self.color = color

	def getColor(self):
		return self.color
	
	def setPrice(self, price):
		self.price = price

	def getPrice(self):
		return self.price

    