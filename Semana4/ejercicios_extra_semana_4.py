#PSEUDOCODIGO

#EJERCICIO 1
#Cree un pseudocódigo que le pida un precio de producto al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:

#     1. Si el precio es menor a 100, el descuento es del 2%.
#     2. Si el precio es mayor o igual a 100, el descuento es del 10%.
precio_producto = int(input('Ingrese el precio del producto: '))
if(precio_producto < 100):
    precio_producto = precio_producto * 0.98
else:
    precio_producto = precio_producto * 0.9
print(f'El precio del producto es: {precio_producto}')

#EJERCICIO 2
# Cree un pseudocódigo que le pida un tiempo en segundos al usuario y calcule si es menor o mayor a 10 minutos.
# Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos.
# Si es mayor, muestre “Mayor”.
tiempo_en_segundos = int(input('Ingrese el tiempo en segundos: '))
tiempo_faltante = 0
if(tiempo_en_segundos < 600):
    tiempo_faltante = 600 - tiempo_en_segundos
    print(f'El tiempo faltante para 10 minutos es: {tiempo_faltante} segundos')
else:
    print('Mayor')

#EJERCICIO 3
# Cree un algoritmo que le pida un numero al usuario y muestre la suma de todos los números desde 1 hasta ese número.
numero_usuario = int(input('Ingrese un numero: '))
contador = 0
resultado = 0
while(contador < numero_usuario):
    contador = contador + 1
    resultado = resultado + contador
print(f'El resultado es: {resultado}')

#EJERCICIOS EXTRA

#EJERCICIO 1
# Cree un algoritmo que le pida 2 números al usuario, los guarde en dos variables distintas (primero y segundo) y los ordene de menor a mayor en dichas variables.
numero_mayor = 0
numero_menor = 0
primer_numero = int(input('Ingrese el primer numero: '))
segundo_numero = int(input('Ingrese el segundo numero: '))

if(primer_numero > segundo_numero):
    numero_mayor = segundo_numero
    numero_menor = primer_numero
else :
    numero_menor = primer_numero
    numero_mayor = segundo_numero

print(f'A: {numero_menor} , B: {numero_mayor}')

#EJERCICIO 2
# Cree un algoritmo que le pida al usuario una velocidad en km/h y la convierta a m/s.
# Recuerda que 1 km == 1000m y 1 hora == 60 minutos * 60 segundos.
velocidad_kmh = int(input('Ingrese velocidad en km/h: '))
velocidad_ms = velocidad_kmh * (5/18)
print(f'La velocidad en m/s es: {velocidad_ms}')


#EJERCICIO 3
# Cree un algoritmo que le pregunte al usuario por el sexo de 6 personas,
# ingresando 1 si es mujer o 2 si es hombre, y muestre al final el porcentaje de mujeres y hombres.
hombres = 0
mujeres = 0
contador = 0

while(contador < 6):
    dato_usuario = int(input('Ingrese 1 para mujer, 2 para hombre: '))
    if(dato_usuario == 1):
        mujeres = mujeres + 1
    else:
        hombres = hombres + 1
    contador = contador + 1
porcentaje_mujeres = mujeres * 100 / 6
porcentaje_hombres = hombres * 100 / 6

print(f'El porcentaje de mujeres es: {porcentaje_mujeres}')
print(f'El porcentaje de hombres es: {porcentaje_hombres}')

#DIAGRAMAS DE FLUJO
#EJERCICIO 1
# Cree un diagrama de flujo que pida 3 números al usuario.
# Si uno de esos números es 30, o si los 3 sumados dan 30, mostrar “*Correcto*”.
# Sino, mostrar “*incorrecto*”
primer_numero = int(input('Ingrese el primer numero: '))
segundo_numero = int(input('Ingrese el segundo numero: '))
tercer_numero = int(input('Ingrese el tercer numero: '))

if(primer_numero == 30 or segundo_numero == 30 or tercer_numero == 30 or (primer_numero + segundo_numero + tercer_numero == 30)) :
    print('Correcto')
else:
    print("Incorrecto")

#EJERCICIO 2
#Cree un diagrama de flujo que le pida 5 números al usuario y muestre el mayor.
contador = 0
numero_mayor = 0
while(contador < 5):
    contador = contador + 1
    numero_actual = int(input('Ingrese un numero: '))
    if(contador <= 5):
        if(numero_actual > numero_mayor):
            numero_mayor = numero_actual
print(f'El numero mayor es {numero_mayor}')

#EJERCICIO 3
#Cree un diagrama de flujo que le pida un numero al usuario y muestre “Fizz” si es divisible entre 3,
# “Buzz” si es divisible entre 5,
# y “FizzBuzz” si es divisible entre ambos.
numero_usuario = int(input('Ingrese un numero: '))
mensaje = ''
if(numero_usuario % 3 == 0):
    mensaje = 'Fizz'
if(numero_usuario % 5 == 0):
    mensaje = mensaje + 'Buzz'
print(mensaje)

#EJERCICIO 4
#Cree un diagrama de flujo que le pida 100 números al usuario y muestre la suma de todos.
contador = 0
resultado = 0
while(contador < 100):
    numero_usuario = int(input('Ingrese un numero: '))
    resultado = resultado + numero_usuario
    contador = contador + 1
print(f'El resultado es: {resultado}')

#EJERCICIO 5
#Cree un diagrama de flujo que le pida 100 números al usuario y muestre el mayor de todos.
contador = 0
numero_mayor = 0
while(contador < 100):
    numero_usuario = int(input('Ingrese un numero: '))
    if(numero_usuario > numero_mayor):
        numero_mayor = numero_usuario
    contador = contador + 1
print(f'El numero mayor es: {numero_mayor}')