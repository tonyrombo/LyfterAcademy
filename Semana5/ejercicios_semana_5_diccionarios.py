#1. Cree un diccionario que guarde la siguiente información sobre un hotel:
    # nombre
    # numero_de_estrellas
    # habitaciones
# El key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información:
    # numero
    # piso
    # precio_por_noche

informacion_hotel = {
    'nombre': 'La Antonia Resort',
    'numero_estrellas': 3,
    'habitaciones': [
        {'numero': 1, 'piso': 1, 'precio_noche': 60},
        {'numero': 2, 'piso': 1, 'precio_noche': 60},
        {'numero': 3, 'piso': 1, 'precio_noche': 60},
        {'numero': 4, 'piso': 1, 'precio_noche': 100},
        {'numero': 5, 'piso': 1, 'precio_noche': 100},
        {'numero': 1, 'piso': 2, 'precio_noche': 120},
        {'numero': 2, 'piso': 2, 'precio_noche': 120},
        {'numero': 3, 'piso': 2, 'precio_noche': 140},
        {'numero': 4, 'piso': 2, 'precio_noche': 140},
        {'numero': 5, 'piso': 2, 'precio_noche': 200}
    ]
}

#2. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
list_a = ['first_name', 'last_name', 'role']
list_b = ['Tony', 'Romero', 'Software Engineer']
user_info={}

if(len(list_a) == len(list_b)):
    for index in range(0, len(list_a)):
        user_info[list_a[index]] = list_b[index]
print(user_info)

#3. 3. Cree un programa que use una lista para eliminar keys de un diccionario.
list_of_keys = ['access_level', 'age']
employee = {'name': 'John', 'email': 'john@ecorp.com', 'access_level': 5, 'age': 28}

for key in list_of_keys:
    for item in list(employee):
        if (key == item):
            employee.pop(item)
print(employee)

#EJERCICIO EXTRA
sales = [
	{
		'date': '27/02/23',
		'customer_email': 'joe@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Iron',
				'upc': 'ITEM-324',
				'unit_price': 32.45,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 12.54,
			},
		],
	},
	{
		'date': '27/02/23',
		'customer_email': 'david@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 5.42,
			},
		],
	},
	{
		'date': '26/02/23',
		'customer_email': 'amanda@gmail.com',
		'items': [
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 3.42,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 17.54,
			},
		],
	},
]

result = {}

for sale in sales:
    for item in sale['items']:
        if(not result.get(item['upc'])):
            result[item['upc']] = item['unit_price']
        else:
            result[item['upc']] += item['unit_price']
print(result)