SELECT * FROM products;

SELECT * FROM products WHERE price > 50000;

SELECT * FROM product_invoice WHERE product_id = 2;

SELECT product_id, SUM(quantity) FROM product_invoice GROUP BY product_id; 

SELECT * FROM invoices WHERE user_id = 1;

SELECT * FROM invoices ORDER BY total_amount DESC;

SELECT * FROM invoices WHERE invoice_number = 1001;