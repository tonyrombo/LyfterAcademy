#1. Crea un bubble_sort por tu cuenta sin revisar el código de la lección.

def bubble_sort(list):
    for first_index in range(len(list)):
        for second_index in range(len(list) - 1 - first_index):
            if list[second_index] > list[second_index + 1]:
                list[second_index], list[second_index + 1] = list[second_index + 1], list[second_index] #Con este codigo se intercambian valores de manera sencilla y se evita el uso de una variable temporal
    return list

# Ejemplo
my_list = [5, 2, 9, 1, 5, 6, -2]
print(bubble_sort(my_list))  # [1, 2, 5, 5, 6, 9]

#2. Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero (como en la imagen de abajo).

def reversed_bubble_sort(list):
    for first_index in range(len(list)):
        for second_index in range(len(list) - 1, first_index, -1):  # Se invierte el recorrido del for
            if list[second_index] < list[second_index - 1]:  # Se intercambian si el anterior es menor
                list[second_index], list[second_index - 1] = list[second_index - 1], list[second_index]
    return list

# Ejemplo:
my_list = [5, 2, 9, 1, 5, 6]
print(reversed_bubble_sort(my_list))  # [9, 6, 5, 5, 2, 1]


#3 Implemente un bubble_sort que funcione para Linked Lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("No hay nodos para eliminar")
            return None

        removed_data = self.top.data
        self.top = self.top.next
        return removed_data

    def print_stack(self):
        current = self.top
        if not current:
            print("No hay nodos para mostrar.")
            return

        print("Mostrando stack de arriba hacia abajo:")
        while current:
            print(f"| {current.data} |")
            current = current.next
        print("------")

    def bubble_sort(self):
        if not self.top or not self.top.next:
            return  # Si solo hay un nodo o está vacío, se salta el sort

        swapped = True
        while swapped:
            swapped = False
            current = self.top
            while current.next: #se compara que el current.next no es None
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data #Se hace el swap si cumplen con la comparacion de valores
                    swapped = True
                current = current.next #Se actualiza con el nodo siguiente

# Ejemplo:
#Se agregan nodos al Stack
stack = Stack()
stack.push(5)
stack.push(1)
stack.push(4)
stack.push(2)
stack.push(3)

print("Antes de Bubble Sort:")
stack.print_stack()

print("Después de Bubble Sort:")
stack.bubble_sort()
stack.print_stack()