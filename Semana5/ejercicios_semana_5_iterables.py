#1. Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']
for index in range(0, len(first_list)):
    print(first_list[index], second_list[index])

#2. Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
my_string = 'Pizza con piña'
for letter in range(len(my_string), 0, -1): #primer parametro: cantidad de elementos, segundo: hasta donde llega el contador, tercero: cantidad de elementos por iteraccion, en negativo es hacia atrás.
    print(my_string[letter - 1])

#3. Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
my_list = [4, 3, 6, 1, 7]
first_item = my_list[0]
my_list[0] = my_list[len(my_list) - 1]
my_list[len(my_list) - 1] = first_item

print(my_list)

#4. Cree un programa que elimine todos los números impares de una lista.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for item in my_list:
    if(item % 2 != 0):
        my_list.remove(item)

print(my_list)

#5. Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
counter = 0
my_list = []
highest_number = 0
while (counter < 10):
    user_number = int(input('Ingrese un numero: '))
    my_list.append(user_number)
    if(user_number > highest_number): highest_number = user_number
    counter += 1
print(my_list)
print(f'El numero mas alto fue: {highest_number}')
