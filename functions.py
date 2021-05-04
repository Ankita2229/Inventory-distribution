import connection as c, mysql.connector
from datetime import date

def insertUserInfo(firstname, lastname, email_id, phone, passwd, disabled, veteran, user_type):
	conn = c.returnConnection()
	try:
		cursor = conn.cursor()
		cursor.execute(f"INSERT INTO users (fname, lname, email, phone, password_provided, disabled, war_veteran, type_of_user) VALUES ('{firstname}', '{lastname}', '{email_id}', '{phone}', MD5('{passwd}'), '{disabled}', '{veteran}', '{user_type}')")
		conn.commit()
		cursor.close()
		conn.close()
	except (Exception, mysql.connector.Error) as error:
		print('Error while fetching data from mySQL', error)

def checkIfUserExist(login_email, login_password):
	conn = c.returnConnection()
	try:
		cursor = conn.cursor(buffered=True)
		cursor.execute(f"SELECT user_id, fname, email, type_of_user FROM users WHERE email = '{login_email}' and password_provided = MD5('{login_password}')")
		data=cursor.fetchone()
		conn.commit()
		cursor.close()
		conn.close()
		return data
	except (Exception, mysql.connector.Error) as error:
		print('Error while fetching data from mySQL', error)

def insertProductInfo(user_id, manufacturer, model_name, model_quantity, model_year, color, cost):
	conn = c.returnConnection()
	try:
		cursor = conn.cursor()
		cursor.execute(f"INSERT INTO products (user_id, make, model, model_quantity, model_year, color, price) VALUES ('{user_id}', '{manufacturer}', '{model_name}', '{model_quantity}', '{model_year}', '{color}', '{cost}')")
		conn.commit()
		cursor.close()
		conn.close()
	except (Exception, mysql.connector.Error) as error:
		print('Error while fetching data from mySQL', error)

def updateProduct(id, make, model_name, qty, year, color, cost):
	conn = c.returnConnection()
	try:
		cursor = conn.cursor()        
		cursor.execute(f"UPDATE products SET make = '{make}', model = '{model_name}', model_quantity = {qty}, model_year = '{year}', color = '{color}', price = '{cost}' WHERE product_id = {id}")
		conn.commit()
		cursor.close()
		conn.close()
	except (Exception, mysql.connector.Error) as error:
		print('Error while fetching data from mySQL', error)

def searchBestMatch(make, model, year, color):
	conn = c.returnConnection()
	try:
		cursor = conn.cursor()
		cursor.execute(f"SELECT * FROM products WHERE make LIKE '%{make}%' OR model LIKE '%{model}%' OR model_year LIKE '%{year}%' OR color LIKE '%{color}%'")
		products = list(cursor.fetchall())
		conn.commit()
		cursor.close()
		conn.close()
		return products
	except (Exception, mysql.connector.Error) as error:
		print('Error while fetching data from mySQL', error)

def fetchPriceFromProduct(product_id):
	conn = c.returnConnection()
	try:
		cursor = conn.cursor()
		cursor.execute(f"SELECT color, price FROM products WHERE product_id = {product_id}")
		data=cursor.fetchone()
		conn.commit()
		cursor.close()
		conn.close()
		return data
	except (Exception, mysql.connector.Error) as error:
		print('Error while fetching data from mySQL', error)

def fetchDisabledOrVeteranFromUser(buyer_id):
	conn = c.returnConnection()
	try:
		cursor = conn.cursor()
		cursor.execute(f"SELECT disabled, war_veteran FROM users WHERE user_id = {buyer_id}")
		data=cursor.fetchone()
		conn.commit()
		cursor.close()
		conn.close()
		return data
	except (Exception, mysql.connector.Error) as error:
		print('Error while fetching data from mySQL', error)

def insertIntoOrder(buyer_id, product_id, order_qty, orig_price, discount, tax, downPayment_discount, paid):
	conn = c.returnConnection()
	try:
		cursor = conn.cursor()
		cursor.execute(f"INSERT INTO orders (user_id, product_id, order_quantity, original_price, discount_percent, tax_percent, downPaymentDiscount, paid) VALUES ('{buyer_id}', '{product_id}', '{order_qty}', '{orig_price}', '{discount}', '{tax}', '{downPayment_discount}', '{paid}')")
		conn.commit()
		cursor.close()
		conn.close()
	except (Exception, mysql.connector.Error) as error:
		print('Error while fetching data from mySQL', error)

def checkOrderQuantityEqualOrLesserThanAvailableProduct(product_id):
	conn = c.returnConnection()
	try:
		cursor = conn.cursor()
		cursor.execute(f"SELECT model_quantity FROM products WHERE product_id = {product_id}")
		data = cursor.fetchone()
		conn.commit()
		cursor.close()
		conn.close()
		return data
	except (Exception, mysql.connector.Error) as error:
		print('Error while fetching data from mySQL', error)
	
def updateQuantityInProduct(product_id, updatedProdQty):
	conn = c.returnConnection()
	try:
		cursor = conn.cursor()        
		cursor.execute(f"UPDATE products SET model_quantity = {updatedProdQty} WHERE product_id = {product_id}")
		conn.commit()
		cursor.close()
		conn.close()
	except (Exception, mysql.connector.Error) as error:
		print('Error while fetching data from mySQL', error)

def getProductIDForViewCartForCurrentUser(buyer_id, paid):
	conn = c.returnConnection()
	try:
		cursor = conn.cursor()        
		cursor.execute(f"SELECT product_id, order_id, order_quantity FROM orders WHERE user_id = {buyer_id} AND paid = '{paid}'")
		prod_ids = list(cursor.fetchall())
		conn.commit()
		cursor.close()
		conn.close()
		return prod_ids
	except (Exception, mysql.connector.Error) as error:
		print('Error while fetching data from mySQL', error)

def getProductsFromProductID(product_id, order_id, order_qty):
	conn = c.returnConnection()
	try:
		cursor = conn.cursor()        
		cursor.execute(f"SELECT * FROM products WHERE product_id = {product_id}")
		data = cursor.fetchone()
		ls = list(data)
		ls.append(order_id)
		ls.append(order_qty)
		data = tuple(ls)
		conn.commit()
		cursor.close()
		conn.close()
		return data
	except (Exception, mysql.connector.Error) as error:
		print('Error while fetching data from mySQL', error)

def delete_inventories(product_id, seller_id):
	conn = c.returnConnection()
	try:
		cursor = conn.cursor()
		cursor.execute(f"DELETE FROM products WHERE product_id = '{product_id}' AND user_id = '{seller_id}'")
		conn.commit()
		cursor.close()
		conn.close()
	except (Exception, mysql.connector.Error) as error:
		print('Error while fetching data from mySQL', error)

def deleteOrder(order_id):
	conn = c.returnConnection()
	try:
		cursor = conn.cursor()
		cursor.execute(f"DELETE FROM orders WHERE order_id = '{order_id}'")
		conn.commit()
		cursor.close()
		conn.close()
	except (Exception, mysql.connector.Error) as error:
		print('Error while fetching data from mySQL', error)

def fetchQuantity(order_id):
	conn = c.returnConnection()
	try:
		cursor = conn.cursor()
		cursor.execute(f"SELECT order_quantity FROM orders WHERE order_id = '{order_id}'")
		qty = cursor.fetchone()
		conn.commit()
		cursor.close()
		conn.close()
		return qty
	except (Exception, mysql.connector.Error) as error:
		print('Error while fetching data from mySQL', error)

def fetchProdQuantity(product_id):
	conn = c.returnConnection()
	try:
		cursor = conn.cursor()
		cursor.execute(f"SELECT model_quantity FROM products WHERE product_id = '{product_id}'")
		qty = cursor.fetchone()
		conn.commit()
		cursor.close()
		conn.close()
		return qty
	except (Exception, mysql.connector.Error) as error:
		print('Error while fetching data from mySQL', error)

def getUserDetailsForOrderSummary(buyer_id):
	conn = c.returnConnection()
	try:
		cursor = conn.cursor()
		cursor.execute(f"SELECT fname, lname, email, phone FROM users WHERE user_id = '{buyer_id}'")
		data = cursor.fetchone()
		conn.commit()
		cursor.close()
		conn.close()
		return data
	except (Exception, mysql.connector.Error) as error:
		print('Error while fetching data from mySQL', error)
	
def getProductDetailsForOrderSummary(product_id):
	conn = c.returnConnection()
	try:
		cursor = conn.cursor()
		cursor.execute(f"SELECT make, model, model_year, color FROM products WHERE product_id = '{product_id}'")
		data = cursor.fetchone()
		conn.commit()
		cursor.close()
		conn.close()
		return data
	except (Exception, mysql.connector.Error) as error:
		print('Error while fetching data from mySQL', error)

def getOrderDetailsForSummary(order_id):
	conn = c.returnConnection()
	try:
		cursor = conn.cursor()
		cursor.execute(f"SELECT original_price, order_quantity, discount_percent, tax_percent, downPaymentDiscount FROM orders WHERE order_id = '{order_id}'")
		data = cursor.fetchone()
		conn.commit()
		cursor.close()
		conn.close()
		return data
	except (Exception, mysql.connector.Error) as error:
		print('Error while fetching data from mySQL', error)

def updatePaidInOrder(order_id, paid):
	conn = c.returnConnection()
	try:
		cursor = conn.cursor()        
		cursor.execute(f"UPDATE orders SET paid = '{paid}' WHERE order_id = {order_id}")
		conn.commit()
		cursor.close()
		conn.close()
	except (Exception, mysql.connector.Error) as error:
		print('Error while fetching data from mySQL', error)