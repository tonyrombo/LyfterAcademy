#1. Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.
def print_last_name():
    print_name()
    print('Romero')


def print_name():
    print('Tony')


print_last_name()

#2. Experimente con el concepto de scope:
    #1. Intente accesar a una variable definida dentro de una función desde afuera.
    #2.  Intente accesar a una variable global desde una función y cambiar su valor.

hour = '5:00pm'
def print_time():
    day = 'Saturday'
    print(f'Today is {day} and the hour is {hour}')

#3. Cree una función que retorne la suma de todos los números de una lista.
    #1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
    #2. [4, 6, 2, 29] → 41

my_list = [4, 6, 2, 29]

def list_sum(list):
    result = 0
    for number in list:
        result += number
    return result

print(list_sum(my_list))

#4. Cree una función que le de la vuelta a un string y lo retorne.
    #1. Esto ya lo hicimos en iterables.
    #2. “Hola mundo” → “odnum aloH”

def reversed_string(str):
    reversed = ''
    for letter in range(len(str), 0, -1): 
        reversed += str[letter - 1]
    return reversed

print(reversed_string('Hola Mundo'))

#5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
    #1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

def get_upper_and_lower(str):
    uppers = 0
    lowers = 0
    for letter in str:
        if(not letter == ' '):
            if(letter.islower()):
                lowers += 1
            else:
                uppers += 1
    return f'There`s {uppers} upper cases and {lowers} lower cases'

print(get_upper_and_lower('I love Nación Sushi'))


#6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
    #1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
    #2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

def words_order(str):
    return "-".join(sorted(str.split("-")))

print(words_order('python-variable-funcion-computadora-monitor'))


#7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
    #1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
    #2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
    #3. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no.*

my_list = [1, 4, 6, 7, 13, 9, 67]

def is_prime(number):
    if(number <= 1):
        return False
    if(number == 2):
        return True
    
    for i in range(2, number-1):
        if(number%i == 0):
            return False
    return True

def find_primes(list):
    result = []
    for n in list:
        if(is_prime(n)):
            result.append(n)
    return result

print(find_primes(my_list))