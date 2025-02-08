from abc import ABC, abstractmethod
import math


#EJERCICIO 1
class BankAccount:
    def __init__(self, balance):
        if balance < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")
        self.balance = balance

    def deposit_money(self, amount):
        if amount <= 0:
            print("El monto a depositar debe ser mayor que 0.")
            return
        self.balance += amount
        print(f"Depósito exitoso. Saldo actual: ${self.balance:.2f}") #Método para pasar el numero a 2 decimales

    def withdraw_money(self, amount):
        if amount <= 0:
            print("El monto a retirar debe ser mayor que 0.")
            return
        if amount > self.balance:
            print("Fondos insuficientes.")
            return
        self.balance -= amount
        print(f"Retiro exitoso. Saldo actual: ${self.balance:.2f}")

    def current_balance(self):
        return self.balance
    

class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)  # Se utiliza super() para acceder a los metodos de la clase padre
        self.min_balance = min_balance

    def withdraw_money(self, amount):
        if self.balance - amount < self.min_balance:
            print(f"No se pueden retirar ${amount:.2f}. El saldo debe permanecer sobre ${self.min_balance}.")
        else:
            super().withdraw_money(amount)
            print(f"Retiro exitoso. Saldo actual: ${self.balance:.2f}")

# print("\nSavings Account")
# savings = SavingsAccount(1000, 300)  
# savings.withdraw_money(500)
# savings.withdraw_money(250)  
# savings.deposit_money(100)


#EJERCICIO 2
class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter

    def calculate_area(self):
        area = math.pi * self.radius ** 2 
        return area
    
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        perimeter = 4 * self.side
        return perimeter

    def calculate_area(self):
        area = self.side ** 2
        return area
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter

    def calculate_area(self):
        area = self.width * self.height
        return area
    

print("\nPerimetro y Area de figuras")
circle = Circle(5)
square = Square(4)
rectangle = Rectangle(3, 7)
print(f"El perimetro del círculo es: {circle.calculate_perimeter():.2f}")
print(f"El área del círculo es: {circle.calculate_area():.2f}")
print(f"El perimetro del cuadrado es: {square.calculate_perimeter():.2f}")
print(f"El área del cuadrado es: {square.calculate_area():.2f}")
print(f"El perímetro del rectángulo es: {rectangle.calculate_perimeter():.2f}")
print(f"El área del rectángulo es: {rectangle.calculate_area():.2f}")

#EJERCICIO 3
#print("\nUtilidad de la Herencia Múltiple en Clases.")
answer = 'Según lo visto en las clases podemos decir que la herencia multiple se utiliza para heredar de mas de una clase padre y asi podemos utilizar métodos de varias clases en una clase hija.\nSirve para:\n\t1. Utilizar metodos en diferentes clases.\n\t2. Tener ceodigo reutilizable.\n\n'
#print(answer)
#EJEMPLO
class Plant:
    def __init__(self, name):
        self.name = name

    def photosynthesis(self):
        return f"{self.name} realiza fotosíntesis para producir su alimento."

class FloweringPlant:
    def bloom(self):
        return f"{self.name} tiene la capacidad de producir flores."
    
class FruitingPlant:
    def produce_fruit(self):
        return f"{self.name} tiene la capacidad de producir frutas que sirven de alimento."

class RoseAppleTree(Plant, FloweringPlant, FruitingPlant):
    def __init__(self, name):
        super().__init__(name)

tree = RoseAppleTree("Árbol de Manzana Rosa")

# print(tree.photosynthesis())
# print(tree.bloom())
# print(tree.produce_fruit())