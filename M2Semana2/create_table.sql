CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code VARCHAR(25) NOT NULL,
    price DECIMAL NOT NULL,
    date_created DATETIME NOT NULL,
    brand VARCHAR(25) NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    registered_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS shopping_cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_email VARCHAR(100) NOT NULL,
    FOREIGN KEY (user_email) REFERENCES users(email)
);

CREATE TABLE IF NOT EXISTS shopping_cart_product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    shopping_cart_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (shopping_cart_id) REFERENCES shopping_cart(id),
    FOREIGN KEY (product_id) REFERENCES products(id),
    UNIQUE (shopping_cart_id, product_id)
);

CREATE TABLE IF NOT EXISTS payment_method (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    payment_type VARCHAR(100) NOT NULL UNIQUE,
    bank_name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_number INTEGER NOT NULL UNIQUE,
    purchase_date DATE NOT NULL,
    total_amount DECIMAL NOT NULL,
    user_id INTEGER NOT NULL,
    invoice_payment_type INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (invoice_payment_type) REFERENCES payment_method(id)
);

CREATE TABLE IF NOT EXISTS product_invoice (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    amount DECIMAL NOT NULL,
    FOREIGN KEY (invoice_id) REFERENCES invoices(id),
    FOREIGN KEY (product_id) REFERENCES products(id),
    UNIQUE (invoice_id, product_id)
);

CREATE TABLE IF NOT EXISTS invoice_payment_method (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER NOT NULL,
    payment_method_id INTEGER NOT NULL,
    payment_amount DECIMAL NOT NULL,
    FOREIGN KEY (invoice_id) REFERENCES invoices(id),
    FOREIGN KEY (payment_method_id) REFERENCES payment_method(id),
    UNIQUE (invoice_id, payment_method_id)
);

CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_code INTEGER NOT NULL,
    comment VARCHAR(250) NOT NULL,
    rating INTEGER NOT NULL,
    date DATETIME NOT NULL,
    user_id INTEGER NOT NULL,
    product_invoice_id INTEGER NOT NULL,
    FOREIGN KEY (product_code) REFERENCES products(id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (product_invoice_id) REFERENCES product_invoice(id),
    UNIQUE (user_id, product_invoice_id)
);