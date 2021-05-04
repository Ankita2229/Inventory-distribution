import os
from os import system
from user import User
import functions as func, getpass, re

system('clear')

# Make a regular expression for validating an Email
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

def initial_registration():
	user = User()
	fname = input('Enter your first name: ')
	user.setFirstName(fname)
	lname = input('Enter your last name: ')
	user.setLastName(lname)
	
	email = input('Enter your email: ')

	check = True
	while(check):
		if (re.search(regex,email)):
			user.setEmail(email)
			check = False
		else:
			email = input('Invalid Format. For eg - "example@example.com": ')

	phone = input('Enter your phone: ')
	user.setPhone(phone)

	password = getpass.getpass('Enter your password: ')
	user.setPasswordProvided(password)

	# 0 - false and 1 - true
	# Check database default value - In case it's false - keep condition that gives an idea whether to provide discount.
	disabled = input('Do you identify yourself as Disabled? [y/n]: ')
	user.setDisabled('1') if(disabled == 'y') else user.setDisabled('0')

	veteran = bool(input('Are you a war veteran? [y/n]: '))
	user.setWarVeteran('1') if(veteran == 'y') else user.setWarVeteran('0')

	typeOfUser = input('Are you a buyer or a seller? ')
	if(typeOfUser.lower() == "seller" or typeOfUser.lower() == "buyer"): user.setTypeOfUser(typeOfUser)

	func.insertUserInfo(user.getFirstName(), user.getLastName(), user.getEmail(), user.getPhone(), user.getPasswordProvided(), user.getDisabled(), user.getWarVeteran(), user.getTypeOfUser())
	data = [user.getFirstName(), user.getLastName(), user.getEmail(), user.getPhone(), user.getDisabled(), user.getWarVeteran(), user.getTypeOfUser()]
	return data

def authentication():
	login_email = input('Enter your email: ')
	login_password = getpass.getpass('Enter your password: ')
	data = func.checkIfUserExist(login_email, login_password)
	return data