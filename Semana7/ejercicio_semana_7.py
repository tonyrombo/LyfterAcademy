#1. Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
#1. Suma
#2. Resta
#3. Multiplicación
#4. División
#5. Borrar resultado
#Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
#Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.

def calculator():
    first_number = 0
    print(first_number)

    try:
        first_number = int(input("Ingrese un numero: "))
    except ValueError:
        print("Debe ser un numero")

    try:
        operator = input("Ingrese una operacion entre +, -, * o /: ")
        if operator not in ["+", "-", "*", "/"]:
            raise ValueError()
    except ValueError:
        print(f"Debe ingresar una operacion válida.")
    
    try:
        second_number = int(input("Ingrese el otro numero: "))
    except ValueError:
        print("Debe ingresar un numero")

    match operator:
        case "+":
            print(f"El resultado es: {first_number + second_number}")
        case "-":
            print(f"El resultado es: {first_number - second_number}")
        case "*":
            print(f"El resultado es: {first_number * second_number}")
        case "/":
            print(f"El resultado es: {first_number / second_number}")



calculator()