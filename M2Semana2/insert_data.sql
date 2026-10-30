PRAGMA foreign_keys = ON;

INSERT INTO products (code, price, date_created, brand) VALUES ('LAP-001', 650000, '2026-01-15 10:00:00', 'Lenovo');
INSERT INTO products (code, price, date_created, brand) VALUES ('MOU-002', 8500, '2026-01-16 09:30:00', 'Logitech');
INSERT INTO products (code, price, date_created, brand) VALUES ('TEC-003', 22000, '2026-01-16 11:15:00', 'Redragon');
INSERT INTO products (code, price, date_created, brand) VALUES ('MON-004', 120000, '2026-02-01 14:00:00', 'Samsung');
INSERT INTO products (code, price, date_created, brand) VALUES ('AUD-005', 45000, '2026-02-03 08:45:00', 'JBL');

INSERT INTO users (full_name, email, registered_date) VALUES ('Ana Mora', 'ana.mora@mail.com', '2025-11-02');
INSERT INTO users (full_name, email, registered_date) VALUES ('Luis Vargas', 'luis.vargas@mail.com', '2025-11-10');
INSERT INTO users (full_name, email, registered_date) VALUES ('Sofía Jiménez', 'sofia.jimenez@mail.com', '2025-12-01');
INSERT INTO users (full_name, email, registered_date) VALUES ('Carlos Rojas', 'carlos.rojas@mail.com', '2025-12-15');
INSERT INTO users (full_name, email, registered_date) VALUES ('María Solís', 'maria.solis@mail.com', '2026-01-05');
INSERT INTO users (full_name, email, registered_date) VALUES ('Diego Porras', 'diego.porras@mail.com', '2026-01-20');

INSERT INTO payment_method (payment_type, bank_name) VALUES ('Tarjeta de crédito', 'BAC');
INSERT INTO payment_method (payment_type, bank_name) VALUES ('Tarjeta de débito', 'Banco Nacional');
INSERT INTO payment_method (payment_type, bank_name) VALUES ('Efectivo', 'N/A');
INSERT INTO payment_method (payment_type, bank_name) VALUES ('Transferencia', 'BCR');

INSERT INTO invoices (invoice_number, purchase_date, total_amount, user_id, invoice_payment_type, phone_number, employee_code) VALUES (1001, '2026-01-16', 658500, 1, 1, '8888-1111', 7);
INSERT INTO invoices (invoice_number, purchase_date, total_amount, user_id, invoice_payment_type, phone_number, employee_code) VALUES (1002, '2026-02-05', 142000, 2, 2, '8777-2222', 3);
INSERT INTO invoices (invoice_number, purchase_date, total_amount, user_id, invoice_payment_type, phone_number, employee_code) VALUES (1003, '2026-02-10', 45000, 1, 3, '8888-1111', 7);
INSERT INTO invoices (invoice_number, purchase_date, total_amount, user_id, invoice_payment_type, phone_number, employee_code) VALUES (1004, '2026-02-20', 30500, 2, 4, '8777-2222', 5);
INSERT INTO invoices (invoice_number, purchase_date, total_amount, user_id, invoice_payment_type, phone_number, employee_code) VALUES (1005, '2026-03-01', 120000, 4, 1, '8666-3333', 3);

INSERT INTO product_invoice (invoice_id, product_id, quantity, amount) VALUES (1, 1, 1, 650000);
INSERT INTO product_invoice (invoice_id, product_id, quantity, amount) VALUES (1, 2, 1, 8500);
INSERT INTO product_invoice (invoice_id, product_id, quantity, amount) VALUES (2, 4, 1, 120000);
INSERT INTO product_invoice (invoice_id, product_id, quantity, amount) VALUES (2, 3, 1, 22000);
INSERT INTO product_invoice (invoice_id, product_id, quantity, amount) VALUES (3, 5, 1, 45000);
INSERT INTO product_invoice (invoice_id, product_id, quantity, amount) VALUES (4, 2, 1, 8500);
INSERT INTO product_invoice (invoice_id, product_id, quantity, amount) VALUES (4, 3, 1, 22000);
INSERT INTO product_invoice (invoice_id, product_id, quantity, amount) VALUES (5, 4, 1, 120000);

INSERT INTO invoice_payment_method (invoice_id, payment_method_id, payment_amount) VALUES (1, 1, 658500);
INSERT INTO invoice_payment_method (invoice_id, payment_method_id, payment_amount) VALUES (2, 2, 100000);
INSERT INTO invoice_payment_method (invoice_id, payment_method_id, payment_amount) VALUES (2, 3, 42000);
INSERT INTO invoice_payment_method (invoice_id, payment_method_id, payment_amount) VALUES (3, 4, 45000);
INSERT INTO invoice_payment_method (invoice_id, payment_method_id, payment_amount) VALUES (4, 3, 30500);
INSERT INTO invoice_payment_method (invoice_id, payment_method_id, payment_amount) VALUES (5, 1, 120000);

INSERT INTO reviews (product_code, comment, rating, date, user_id, product_invoice_id) VALUES (1, 'Fast laptop, great for work', 5, '2026-01-20 15:00:00', 1, 1);
INSERT INTO reviews (product_code, comment, rating, date, user_id, product_invoice_id) VALUES (2, 'Comfortable mouse, works well', 4, '2026-01-21 09:20:00', 1, 2);
INSERT INTO reviews (product_code, comment, rating, date, user_id, product_invoice_id) VALUES (4, 'Excellent monitor, great colors', 5, '2026-02-12 18:30:00', 2, 3);
INSERT INTO reviews (product_code, comment, rating, date, user_id, product_invoice_id) VALUES (3, 'The keyboard is good but a bit loud', 3, '2026-02-14 10:10:00', 2, 4);