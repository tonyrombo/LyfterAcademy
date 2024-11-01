import random

#EJERCICIO 1
mi_lista = ['gato', 'perro','elefante','koala']
mi_otra_lista = ['auto', 'moto', 'barco', 'avion']
un_int = 5
un_string = 'Hola Mundo'
un_float =  1.834762
un_bool = False
print('Bienvenido, ' + un_string)
print(un_string + un_int) #TypeError: can only concatenate str (not "int") to str
print(un_int + un_string) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(mi_lista + mi_otra_lista) # ['gato', 'perro', 'elefante', 'koala', 'auto', 'moto', 'barco', 'avion']
print(un_string + mi_lista) # TypeError: can only concatenate str (not "list") to str
print(un_float + un_int) # 6.834762
print(un_bool + True) # 1, segun entiendo los boolean tambien tienen valor numerico de 0 (False) y 1 (True)

#EJERCICIO 2
nombre_usuario = input("Ingrese su nombre: ")
apellido_usuario = input("Ingrese su apellido: ")
edad_usuario = int(input("Ingrese su edad: "))
respuesta = f"Hola, {nombre_usuario} {apellido_usuario}. Segun su edad, usted es: "

if(edad_usuario > 0 and edad_usuario < 2):
    print(respuesta + "bebe")
elif(edad_usuario > 2 and edad_usuario < 12):
    print(respuesta + "nino")
elif(edad_usuario > 12 and edad_usuario < 18):
    print(respuesta + "adolescente")
elif(edad_usuario > 18 and edad_usuario < 35):
    print(respuesta + "adulto joven")
elif(edad_usuario > 35 and edad_usuario < 60):
    print(respuesta + "adulto")
elif(edad_usuario > 60):
    print(respuesta + "adulto mayor")

#EJERCICIO 3
numero_secreto = random.randint(1, 10)
numero_usuario = int(input("Ingrese un numero entre 1 y 10: "))

while(numero_secreto != numero_usuario):
    print("Fallaste, intenta de nuevo!")
    numero_usuario = int(input("Ingresa un numero entre 1 y 10: "))
if(numero_secreto == numero_usuario):
    print("Adivinaste el numero!")

#EJERCICIO 4
lista_numeros = []
numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el primer numero: "))
numero_3 = int(input("Ingrese el primer numero: "))
lista_numeros += [numero_1, numero_2, numero_3]
lista_numeros.sort()
print(f'El numero mayor es: {lista_numeros[len(lista_numeros) - 1]}')

#EJERCICIO 5
total_notas = int(input('Ingrese el total de notas: '))
contador = 0
notas_aprobadas = 0
notas_desaprobadas = 0
promedio_aprobadas = 0
promedio_desaprobadas = 0
promedio_total = 0

while(contador < total_notas):
    nota_actual = int(input(f'Ingrese la nota numero {contador + 1}: '))
    if(nota_actual < 70):
        notas_desaprobadas = notas_desaprobadas + 1
        promedio_desaprobadas = promedio_desaprobadas + nota_actual
    else:
        notas_aprobadas = notas_aprobadas + 1
        promedio_aprobadas = promedio_aprobadas + nota_actual
    contador = contador + 1
    promedio_total = promedio_total + (nota_actual / total_notas)
if(notas_desaprobadas > 0) : promedio_desaprobadas = promedio_desaprobadas / notas_desaprobadas
if(notas_aprobadas > 0) : promedio_aprobadas = promedio_aprobadas / notas_aprobadas

print(f'El estudiante tiene {notas_aprobadas} notas aprobadas')
print(f'Y el promedio de aprobadas es: {promedio_aprobadas}')
print(f'El estudiante tiene {notas_desaprobadas} notas desaprobadas')
print(f'Y el promedio de desaprobadas es: {promedio_desaprobadas}')
print(f'Este es el promedio total: {promedio_total}')