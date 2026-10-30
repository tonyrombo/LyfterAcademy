## Limitantes de SQLite encontradas

1. **No existe BIGINT.** Se usó INTEGER (64 bits en SQLite).
2. **ALTER TABLE ADD COLUMN con NOT NULL** falla si la tabla ya tiene datos.
3. **ALTER TABLE no puede agregar UNIQUE ni PRIMARY KEY** a una columna existente. Por eso el UNIQUE se defidefinenió desde el CREATE TABLE.
4. **Las FOREIGN KEY no se validan por defecto.** Se usa PRAGMA foreign_keys = ON en el archivo de datos.
5. **No hay tipo DATE/DATETIME real.** Las fechas se guardan como texto.

## Mejoras al diseño

1. El diagrama original de Invoice_Payment_Method no tenía invoice_id. Se agregó como FK a invoices(id), porque sin él no se sabe a qué factura pertenece cada pago.

## Orden de ejecución

1. create_table.sql (estructura)
2. alter_invoices.sql (columnas nuevas en invoices)
3. insertar_datos.sql (datos, con PRAGMA foreign_keys = ON)
4. get_data.sql (consultas SELECT)
