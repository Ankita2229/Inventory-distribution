class Order:
	def __init__(self, purchase_date = None, order_quantity = None, original_price = None, discount_percent = None, tax_percent = None, downPaymentDiscount = None, paid = None):
		self.purchase_date = purchase_date
		self.order_quantity = order_quantity
		self.original_price = original_price
		self.discount_percent = discount_percent
		self.tax_percent = tax_percent
		self.downPaymentDiscount = downPaymentDiscount
		self.paid = paid

	def setPurchaseDate(self, purchase_date):
		self.purchase_date = purchase_date

	def getPurchaseDate(self):
		return self.purchase_date

	def setOrderQuantity(self, order_quantity):
		self.order_quantity = order_quantity

	def getOrderQuantity(self):
		return self.order_quantity

	def setOriginalPrice(self, original_price):
		self.original_price = original_price

	def getOriginalPrice(self):
		return self.original_price

	def setDiscountPercent(self, discount_percent):
		self.discount_percent = discount_percent

	def getDiscountPercent(self):
		return self.discount_percent

	def setTaxPercent(self, tax_percent):
		self.tax_percent = tax_percent

	def getTaxPercent(self):
		return self.tax_percent

	def setdownPaymentDiscount(self, downPaymentDiscount):
		self.downPaymentDiscount = downPaymentDiscount

	def getdownPaymentDiscount(self):
		return self.downPaymentDiscount

	def setPaid(self, paid):
		self.paid = paid

	def getPaid(self):
		return self.paid