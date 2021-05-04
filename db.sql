use myDB;
-- Hackathon Tables

DROP TABLE users;

SELECT * FROM users;

CREATE TABLE IF NOT EXISTS users
(
	user_id SMALLINT PRIMARY KEY AUTO_INCREMENT,
	fname VARCHAR(20) NOT NULL,
	lname VARCHAR(20) NOT NULL,
	email VARCHAR(255) NULL,
	phone VARCHAR(10) NOT NULL,
	password_provided CHAR(60) NOT NULL,
	disabled TINYINT(1) NOT NULL DEFAULT '0',
	war_veteran TINYINT(1) NOT NULL DEFAULT '0',
	type_of_user VARCHAR(15) NOT NULL
);

DESCRIBE users;

INSERT INTO users (fname, lname, email, phone, password_provided, disabled, war_veteran, type_of_user)
VALUES ("qwe", "qwe", "q@q.com", "121212", "xa1\xf1\xe0|\x0fZ\x9f\x87x\xbd\xe8|", "0", "0", "buyer");

DROP TABLE products;

SELECT * FROM products;

DESCRIBE products;

SELECT color, price FROM products WHERE product_id = 1;

CREATE TABLE IF NOT EXISTS products
(
	product_id SMALLINT PRIMARY KEY AUTO_INCREMENT,
	user_id SMALLINT,
	FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE ON UPDATE CASCADE,
	make VARCHAR(15) NOT NULL,
	model VARCHAR(15) NOT NULL,
	model_quantity INT NOT NULL,
	model_year VARCHAR(15) NOT NULL,
	color VARCHAR(15) NOT NULL,
	price DECIMAL(20,2) NOT NULL
);

DROP TABLE orders;

DESCRIBE orders;

SELECT * FROM orders;

CREATE TABLE IF NOT EXISTS orders
(
	order_id SMALLINT PRIMARY KEY AUTO_INCREMENT,
	user_id SMALLINT,
	FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE ON UPDATE CASCADE,
	product_id SMALLINT,
	FOREIGN KEY (product_id) REFERENCES products (product_id) ON DELETE CASCADE ON UPDATE CASCADE,
	purchase_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	order_quantity INT NOT NULL,
	original_price DECIMAL(20,2) NOT NULL,
	discount_percent DECIMAL(10,2) NOT NULL,
	tax_percent DECIMAL(10,2) NOT NULL,
	downPaymentDiscount DECIMAL(20,2) NOT NULL,
	paid TINYINT(1) NOT NULL DEFAULT '0'
);

DROP TABLE login_attempts;

CREATE TABLE IF NOT EXISTS login_attempts
(
	login_id SMALLINT PRIMARY KEY AUTO_INCREMENT,
	user_id SMALLINT,
	FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE ON UPDATE CASCADE,
	login_stamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	attempt VARCHAR(10) NOT NULL
);
