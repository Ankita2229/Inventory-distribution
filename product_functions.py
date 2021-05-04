import connection as c, mysql.connector, os
from os import system
from product import Product
from order import Order
import functions as func
from decimal import Decimal

# system('clear')

def printListForSeller(products):
	print("Available products! ")
	print(f'''
		Sr. No.         Manufacturer         Model Name         Model Year         Quantity         Color         Cost
		---------------------------------------------------------------------------------------------------------------
		''')
	count = 1
	for product in products:
		product_id, seller_id, manufacturer, model_name, model_quantity, model_year, color, price = product
		print(f"{count:>20} {manufacturer:>23} {model_name:>18} {model_year:>18} {model_quantity:>16} {color:>13} {price:>13}\n")
		count += 1

def getListOfAvailableProductsForSeller():
	conn = c.returnConnection()
	try:
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM products')
		products = list(cursor.fetchall())
		cursor.close()
		conn.close()
		if products is not None:
			printListForSeller(products)
		else:
			print("No products to display! ")
	except (Exception, mysql.connector.Error) as error:
			print('Error while fetching data from mySQL', error)

def add_inventories(user_id):
	product = Product()
	manufacturer = input('Enter manufacturer name: ')
	product.setMake(manufacturer)
	model_name = input('Enter your Model name: ')
	product.setModel(model_name)    
	model_qty = int(input('Quantity available: '))
	product.setModelQuantity(model_qty)
	model_yr = input('Enter Model year: ')
	product.setModelYear(model_yr)
	color = input('Enter color available: ')
	product.setColor(color)
	cost = input('Enter cost of the Model: ')
	product.setPrice(cost)
	func.insertProductInfo(user_id, product.getMake(), product.getModel(), product.getModelQuantity(), product.getModelYear(), product.getColor(), product.getPrice())

def fetchProductIDForCount(seller_id):
	conn = c.returnConnection()
	cursor = conn.cursor()
	cursor.execute(f"SELECT * FROM products WHERE user_id = '{seller_id}'")
	products = list(cursor.fetchall())
	cursor.close()
	conn.close()
	mapCountAndProdID = {}
	if products is not None:
		ct = 1
		for product in products:
			mapCountAndProdID[ct] = product[0]
			ct += 1
	return mapCountAndProdID

def showAvailableProductsToUpdateAndDelete(seller_id):
	conn = c.returnConnection()
	cursor = conn.cursor(buffered=True)
	# fetch data to update based on user that is logged in - show user products that belongs to that seller ESPECIALLY for Update!
	cursor.execute(f"SELECT * FROM products WHERE user_id = '{seller_id}'")
	products = list(cursor.fetchall())
	if products is not None:
		printListForSeller(products)
	else:
		print("You do not have any products yet!")

def update_inventories(product_id, seller_id):
	conn = c.returnConnection()
	cursor = conn.cursor(buffered=True)
	# fetch data to update based on user that is logged in - show user products that belongs to that seller ESPECIALLY for Update!
	cursor.execute(f"SELECT make, model, model_quantity, model_year, color, price FROM products WHERE product_id = '{product_id}' AND user_id = '{seller_id}'")
	data = cursor.fetchone()
	manufacturer, model_name, model_quantity, model_year, color, price = data
	update_fields = ['Manufacturer', 'Model name', 'Quantity', 'Model Year', 'Color', 'Cost', 'Previous Menu']    
	while(True):
		print(f'Please select the operation you would like to perform: ')
		cnt = 1
		for field in update_fields:
			print(f'{cnt}. {field}')
			cnt += 1
		selection = int(input('Select one above: '))
		product = Product()
		if(selection == 1):
			manufacturer = input('New Manufacturer: ')
			if manufacturer is not None:    product.setMake(manufacturer)
		elif (selection == 2):
			model_name = input('New Model Name: ')
			if model_name is not None:  product.setModel(model_name)
		elif (selection == 3):
			model_quantity = int(input('New Quantity: '))
			if model_quantity is not None:  product.setModelQuantity(model_quantity)
		elif (selection == 4):
			model_year = input('New Model Year: ')
			if model_year is not None:  product.setModel(model_year)
		elif (selection == 5):
			color = input('New Model Color: ')
			if color is not None:  product.setModel(color)
		elif (selection == 6):
			price = float(input('New Model Cost: '))
			if price is not None:  product.setModel(price)
		elif (selection == 7):
			break
		else:
			print('invalid selection')
		func.updateProduct(product_id, manufacturer, model_name, model_quantity, model_year, color, price)

def performCrudOnSellerOption(seller_id):
	sellerOperationList = ['Add Product', 'View Products (including other sellers)', 'View Products entered by you', 'Update Product', 'Delete Product', 'Quit']
	
	while(True):
		print(f'Please select the operation you would like to perform: ')
		cnt = 1
		for operation in sellerOperationList:
			print(f'{cnt}. {operation}')
			cnt += 1

		selection = int(input('Select one above: '))

		if(selection == 1):
			print("You chose to add a product")
			add_inventories(seller_id)
		elif (selection == 2):
			getListOfAvailableProductsForSeller()
		elif (selection == 3):
			showAvailableProductsToUpdateAndDelete(seller_id)
		elif (selection == 4):
			map = fetchProductIDForCount(seller_id)
			if not map:
				print("You do not have any products to update!")
			else:
				print("Please choose from your added products to update!")
				showAvailableProductsToUpdateAndDelete(seller_id)
				key = int(input("Enter item no. to update: "))
				update_inventories(map[key], seller_id)
		elif (selection == 5):
			map = fetchProductIDForCount(seller_id)
			if not map:
				print("You do not have any products to delete!")
			else:
				print("Please choose from your posted products to delete!")
				showAvailableProductsToUpdateAndDelete(seller_id)
				key = int(input("Enter item no. to delete: "))
				func.delete_inventories(map[key], seller_id)
		elif (selection == 6):
			print('Goodbye!')
			break
		else:
			print('invalid selection')

def printListgetMapForBuyer(products):
	print("Available products! \n")
	print(f'''
		Sr. No.         Manufacturer         Model Name         Model Year         Quantity         Color         Cost
		---------------------------------------------------------------------------------------------------------------
		''')
	count = 1
	mapCountAndProdID = {}
	for product in products:
		product_id, seller_id, manufacturer, model_name, model_quantity, model_year, color, price = product
		mapCountAndProdID[count] = product_id
		print(f"{count:>20} {manufacturer:>23} {model_name:>18} {model_year:>18} {model_quantity:>16} {color:>13} {price:>13}\n")
		count += 1
	return mapCountAndProdID

# Print Order summary	
def createOrder(product_id, buyer_id, prod_qty, color, originalPrice, disabled, veteran, order_qty):
	new_order = Order()
	new_order.setOrderQuantity(order_qty)
	new_order.setOriginalPrice(originalPrice)
	# ($4.57 / 100) x $8,000 - $4.57 per $100 of assessed value
	copyOfOriginalPrice = originalPrice
	# considering 10% down payment for Original Price
	# downPayment = copyOfOriginalPrice * 0.1
	taxOnOriginalPrice = Decimal(copyOfOriginalPrice) * Decimal('0.0457')

	downpaymentDiscount = Decimal('0.0')
	originalPriceDiscount = Decimal('0.0')
	if(color.lower() == 'black'):
		originalPriceDiscount = originalPriceDiscount + (Decimal(copyOfOriginalPrice) * Decimal('0.25'))
	if(color.lower() == 'white'):
		downpaymentDiscount = downpaymentDiscount + 400
	if(disabled == '0' or veteran == '0'):
		originalPriceDiscount = originalPriceDiscount + (Decimal(copyOfOriginalPrice) * Decimal('0.25')) + 500

	# original discount
	new_order.setDiscountPercent(originalPriceDiscount)
	new_order.setTaxPercent(taxOnOriginalPrice)
	new_order.setPaid('0')
	new_order.setdownPaymentDiscount(downpaymentDiscount)
	func.insertIntoOrder(buyer_id, product_id, new_order.getOrderQuantity(), new_order.getOriginalPrice(), new_order.getDiscountPercent(), new_order.getTaxPercent(), new_order.getdownPaymentDiscount(), new_order.getPaid())
	updatedProdQty = prod_qty - order_qty
	func.updateQuantityInProduct(product_id, updatedProdQty)

def chooseItemToBuy(product_id, buyer_id):
	color, originalPrice = func.fetchPriceFromProduct(product_id) # update product quantity once purchased
	disabled, veteran = func.fetchDisabledOrVeteranFromUser(buyer_id)
	order_qty = int(input("Please enter Order Quantity: "))
	prod_qty = func.checkOrderQuantityEqualOrLesserThanAvailableProduct(product_id)
	if(order_qty > 0):
		if(prod_qty[0] >= order_qty):
			createOrder(product_id, buyer_id, prod_qty[0], color, originalPrice, disabled, veteran, order_qty)
		else:
			print("Sorry! We do not have required products! \n")
	else:
		print("Please enter a valid number! \n")
	# Order Summary!!

def getProductOptionsToBuy(buyer_id):
	conn = c.returnConnection()
	try:
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM products')
		products = list(cursor.fetchall())
		cursor.close()
		conn.close()
		if products is not None:
			productMap = printListgetMapForBuyer(products)
			print(productMap)
			key = int(input("Enter item no. that you wish to buy: "))
			if(key > 0):
				chooseItemToBuy(productMap[key], buyer_id)
			else:
				print("Please enter a valid number! \n")
		else:
			print("No products to display! ")  
	except (Exception, mysql.connector.Error) as error:
			print('Error while fetching data from mySQL', error)

def getUserPreference(buyer_id):
	search_product = Product()
	print("Enter the following details: ")
	manufacturer = input('Make: ')
	search_product.setMake(manufacturer)
	modelName = input('Model: ')
	search_product.setModel(modelName)
	modelYear = input('Year: ')
	search_product.setModelYear(modelYear)
	color = input('Color: ')
	search_product.setColor(color)
	products = func.searchBestMatch(search_product.getMake(), search_product.getModel(), search_product.getModelYear(), search_product.getColor())
	if products is not None:
		productMap = printListgetMapForBuyer(products)
		print(productMap)
		key = int(input("Enter item no. that you wish to buy: "))
		if(key > 0):
			chooseItemToBuy(productMap[key], buyer_id)
		else:
			print("Please enter a valid number! \n")
	else:
		print("Sorry! We cannot find a product that matches your preference!\n")
		getProductOptionsToBuy(buyer_id)

def viewCart(products_withOrderidandOrderQty):
	print("Available products! \n")
	print(f'''
		Order No.         Manufacturer         Model Name         Model Year         Order Quantity         Color         Cost
		------------------------------------------------------------------------------------------------------------------------
		''')
	count = 1
	mapCountAndOrderID = {}
	mapCountAndProdID = {}
	for product in products_withOrderidandOrderQty:
		product_id, manufacturer, model_name, order_quantity, model_year, color, price, order_id = product[0], product[2], product[3], product[9], product[5], product[6], product[7], product[8] 
		mapCountAndProdID[count] = product_id
		mapCountAndOrderID[count] = order_id
		print(f"{count:>21} {manufacturer:>24} {model_name:>18} {model_year:>18} {order_quantity:>16} {color:>20} {price:>13}\n")
		count += 1
	return mapCountAndProdID, mapCountAndOrderID

def printOrderSummary(buyer_id, productMap, orderMap):
	fname, lname, email, phone = func.getUserDetailsForOrderSummary(buyer_id)
		
	print(f'''
	Name: {fname.capitalize()} {lname.capitalize()}\n
	Email: {email}\n
	Contact: {phone}\n
	''')

	print(f'''
		Sr. No.         Manufacturer         Model Name         Model Year         Color         Cost         Order Quantity         Calculated Amount
		------------------------------------------------------------------------------------------------------------------------------------------------
		''')
	
	tax = Decimal('0.0')
	discount = Decimal('0.0')
	down_payment = Decimal('0.0')
	amt = Decimal('0.0')
	count = 1
	for (counter, product_id), (key2, order_id) in zip(productMap.items(), orderMap.items()):
		make, model, model_year, color = func.getProductDetailsForOrderSummary(product_id)
		original_price, order_quantity, discount_percent, tax_percent, downPaymentDiscount = func.getOrderDetailsForSummary(order_id)
		paid = 1
		func.updatePaidInOrder(order_id, paid)
		tax = tax + (order_quantity * tax_percent)
		discount = discount + discount_percent
		down_payment = down_payment + downPaymentDiscount
		# considering 10% down payment for Original Price
		# downPayment = copyOfOriginalPrice * 0.1
		amt = amt + (order_quantity * original_price) + tax - discount - down_payment
		print(f'''
		{count:>6} {make:>21} {model:>18} {model_year:>18} {color:>13} {original_price:>13} {order_quantity:>16} {order_quantity * original_price:>28}
		''')
		count+=1

	print(f'''
	                                                     								Tax..........................${tax}\n
		                                                     							Discount.....................${discount}\n
		                                                     							Down Payment Discount........${down_payment}\n
		                                                     							Amount.......................${amt}\n
	''')

def promptWhetherUserRequireListOrPreference(buyer_id):
	initialBuyerOptions = ['To enter your preference. [Make/ Model/ Year/ Color]', 'To view the list of available products!', 'View Cart', 'Delete Item', 'Checkout', 'Quit']
		
	while(True):
		print(f'Please select the operation you would like to perform: ')
		count = 1
		for operation in initialBuyerOptions:
			print(f'{count}. {operation}')
			count += 1
		selection = int(input('Select one above: '))
		if(selection == 1):
			getUserPreference(buyer_id)
		elif (selection == 2):
			getProductOptionsToBuy(buyer_id)
		elif (selection == 3):
			# passing paid = 0 as user haven't paid for the items yet --- update it to 1 once they checkout!
			paid = 0
			prod_ids = func.getProductIDForViewCartForCurrentUser(buyer_id, paid)
			products_withOrderidandOrderQty = []
			for product_id in prod_ids:
				data = func.getProductsFromProductID(product_id[0], product_id[1], product_id[2])
				products_withOrderidandOrderQty.append(data)
			
			if(len(products_withOrderidandOrderQty) > 0):
				productMap, orderMap = viewCart(products_withOrderidandOrderQty)
			else:
				print("Your Cart is Empty!!")

		elif (selection == 4):
			paid = 0
			prod_ids = func.getProductIDForViewCartForCurrentUser(buyer_id, paid)
			products_withOrderidandOrderQty = []
			for product_id in prod_ids:
				data = func.getProductsFromProductID(product_id[0], product_id[1], product_id[2])
				products_withOrderidandOrderQty.append(data)

			if(len(products_withOrderidandOrderQty) > 0):
				productMap, orderMap = viewCart(products_withOrderidandOrderQty)
				delete_order = int(input("Enter order no. that you would like to delete! "))
				if(delete_order > 0):
					order_qty = func.fetchQuantity(orderMap[delete_order])
					prod_qty = func.fetchProdQuantity(productMap[delete_order])
					updated_after_deletion_prod_qty = prod_qty[0] + order_qty[0]
					func.updateQuantityInProduct(productMap[delete_order], updated_after_deletion_prod_qty)
					func.deleteOrder(orderMap[delete_order]) # update product table once deleted!!
				else:
					print("Please enter a valid number! \n")
			else:
				print("Your Cart is Empty!!")
	
		elif (selection == 5):
			# fetch similar data from view and display order summary
			paid = 0
			prod_ids = func.getProductIDForViewCartForCurrentUser(buyer_id, paid)
			products = []
			for product_id in prod_ids:
				data = func.getProductsFromProductID(product_id[0], product_id[1], product_id[2])
				products.append(data)


			if(len(products) > 0):
				mapCountAndOrderID = {}
				mapCountAndProdID = {}
				for product in products:
					product_id, order_id = product[0], product[8] 
					mapCountAndProdID[count] = product_id
					mapCountAndOrderID[count] = order_id
					count += 1
	
				printOrderSummary(buyer_id, mapCountAndProdID, mapCountAndOrderID)		
		elif (selection == 6):
			break
		else:
			print('invalid selection')