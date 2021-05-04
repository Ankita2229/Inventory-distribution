import os 
from os import system
import user_registration as user_reg, product_functions as pd_func 

# system('clear')

def checkForBuyerOrSeller(data):
	buyer_id = data[0]
	if(data[-1] == "buyer"):
		pd_func.promptWhetherUserRequireListOrPreference(buyer_id)
	else:
		# gives direct prompt to add manufactor - see what are other ways to change it
		# pass data[0] for seller_id - need it to store it as foreign key in products table
		seller_id = data[0]
		pd_func.performCrudOnSellerOption(seller_id)

user_options = ['New User', 'Existing User']
print('Hey there! Welcome. Please select if you are an existing User or a new User: ')
count = 1
for user_option in user_options:
	print(f'{count}. {user_option}')
	count += 1

selection = int(input('Select one above: '))

if(selection == 1):
	print('Please register: ')
	data = user_reg.initial_registration() # [..., type_of_user]
	checkForBuyerOrSeller(data)
elif (selection == 2):
	attempt = 1
	flag = True
	print('Please Login: ')
	while(flag and attempt < 4):
		print(f'Attempt #{attempt}: ')
		data = user_reg.authentication() # [user_id, fname, email, type_of_user]
		if data is not None:
			print("Login Successful!")
			flag = False
			checkForBuyerOrSeller(data)
		else:
			attempt += 1
else:
  print('invalid selection')