## Limitantes de SQLite encontradas

1. **No existe BIGINT.** Se usó INTEGER (64 bits en SQLite).
2. **ALTER TABLE ADD COLUMN con NOT NULL** falla si la tabla ya tiene datos.
3. **ALTER TABLE no puede agregar UNIQUE ni PRIMARY KEY** a una columna existente. Por eso el UNIQUE se definió desde el CREATE TABLE.
4. **Las FOREIGN KEY no se validan por defecto.** Se usa PRAGMA foreign_keys = ON en el archivo de datos.
5. **No hay tipo DATE/DATETIME real.** Las fechas se guardan como texto.

## Mejoras al diseño

1. El diagrama original de Invoice_Payment_Method no tenía invoice_id. Se agregó como FK a invoices(id), porque sin él no se sabe a qué factura pertenece cada pago.
2. invoices.invoice_payment_type es redundante con invoice_payment_method. La fuente de verdad de los pagos es invoice_payment_method. Se conserva como método principal (el de mayor monto) y debe coincidir con él. Limitante: SQLite no permite DROP COLUMN sobre una clave foránea, así que eliminarla requiere recrear la tabla.
3. reviews.product_code se renombró a product_id, porque guarda el id de products y no el código de texto. Se hizo con ALTER TABLE ... RENAME COLUMN (alter_reviews.sql).

## Orden de ejecución

1. create_table.sql (estructura)
2. alter_invoices.sql (columnas nuevas en invoices)
3. alter_reviews.sql (renombra product_code a product_id en reviews)
4. insertar_datos.sql (datos, con PRAGMA foreign_keys = ON)
5. get_data.sql (consultas SELECT)
