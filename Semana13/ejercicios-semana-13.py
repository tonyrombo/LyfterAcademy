from datetime import date

#1. Cree un decorador que haga print de los parámetros y retorno de la función que decore.

def mi_funcion_para_imprimir(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"La función: {func.__name__} recibe args: {args} y kwargs: {kwargs} y devuelve como resultado: {result}")
        return result
    return wrapper

@mi_funcion_para_imprimir
def suma_y_altura(a, b, nombre="Nombre", altura=0):
    resultado = f"\nSuma: {a} + {b} = {a + b}.\nEl usuario {nombre} mide {altura} cm."
    return resultado

suma_y_altura(3, 5, nombre="Carlos", altura=170)


#2. Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.

def validar_numeros(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):#funcionalidad para revisar si es integer o float
                raise ValueError(f"Error, se deben ingresar números y se ha ingresado: {arg}")
        return func(*args)
    return wrapper

@validar_numeros
def multiplicacion(a, b):
    return a * b

#PRUEBAS
print(multiplicacion(6, "x"))  # Error
print(multiplicacion(5, 9))  # Correcto

#3. Cree una clase de `User` que:
    #- Tenga un atributo de `date_of_birth`.
    #- Tenga un property de `age`.
    
    #Luego cree un decorador para funciones que acepten un `User` como parámetro que se encargue de revisar si el `User` es mayor de edad y arroje una excepción de no ser así.

class User:
    def __init__(self, birth_date):
        self.birth_date = birth_date

    @property
    def age(self):
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day)) #Funcionalidad que compara no solo años, sino tambien meses y dia para saber si ya ha cumplido en el año actual

def is_adult(func):
    def wrapper(user, *args, **kwargs):
        if user.age < 18:
            raise PermissionError("El usuario no tiene la edad suficiente para ajercer la votación.")
        return func(user, *args, **kwargs)
    return wrapper

@is_adult
def president_election(user):
    return "Accediendo a al sistema de votación."

# Creando usuarios
user1 = User(date(2005, 6, 15))
user2 = User(date(2010, 7, 20))
#PRUEBAS
print(president_election(user1))  # Puede votar
print(president_election(user2))  # Error: No puede votar