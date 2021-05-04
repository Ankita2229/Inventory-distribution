class User:
	def __init__(self, fname = None, lname = None, email = None, phone = None, password_provided = None, disabled = None, war_veteran = None, type_of_user = None):
		self.fname = fname
		self.lname = lname
		self.email = email
		self.phone = phone
		self.password_provided = password_provided
		self.disabled = disabled
		self.war_veteran = war_veteran
		self.type_of_user = type_of_user

	def setFirstName(self, fname):
		self.fname = fname

	def getFirstName(self):
		return self.fname

	def setLastName(self, lname):
		self.lname = lname

	def getLastName(self):
		return self.lname

	def setEmail(self, email):
		self.email = email

	def getEmail(self):
		return self.email

	def setPhone(self, phone):
		self.phone = phone

	def getPhone(self):
		return self.phone

	def setPasswordProvided(self, password_provided):
		self.password_provided = password_provided

	def getPasswordProvided(self):
		return self.password_provided
	
	def setDisabled(self, disabled):
		self.disabled = disabled

	def getDisabled(self):
		return self.disabled

	def setWarVeteran(self, war_veteran):
		self.war_veteran = war_veteran

	def getWarVeteran(self):
		return self.war_veteran

	def setTypeOfUser(self, type_of_user):
		self.type_of_user = type_of_user

	def getTypeOfUser(self):
		return self.type_of_user

    