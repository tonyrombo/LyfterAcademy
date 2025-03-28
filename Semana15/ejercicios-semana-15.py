#1. Crea un bubble_sort por tu cuenta sin revisar el código de la lección.

def bubble_sort(numbers):
    for first_index in range(len(numbers)):
        is_swapped = False
        for second_index in range(len(numbers) - 1 - first_index):
            if numbers[second_index] > numbers[second_index + 1]:
                numbers[second_index], numbers[second_index + 1] = numbers[second_index + 1], numbers[second_index] #Con este codigo se intercambian valores de manera sencilla y se evita el uso de una variable temporal
                is_swapped = True
        if not is_swapped:
            break
    return numbers

# Ejemplo
#my_list = [5, 2, 9, 1, 5, 6, -2]
#print(bubble_sort(my_list))  # [1, 2, 5, 5, 6, 9]

#2. Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero (como en la imagen de abajo).

def reversed_bubble_sort(numbers):
    is_swapped = False
    for first_index in range(len(numbers)):
        for second_index in range(len(numbers) - 1, first_index, -1):  # Se invierte el recorrido del for
            if numbers[second_index] < numbers[second_index - 1]:  # Se intercambian si el anterior es menor
                numbers[second_index], numbers[second_index - 1] = numbers[second_index - 1], numbers[second_index]
                is_swapped = True
        if not is_swapped:
            break
    return numbers

# Ejemplo:
#my_list = [5, 2, 9, 1, 5, 6]
#print(reversed_bubble_sort(my_list))  # [9, 6, 5, 5, 2, 1]


#3 Implemente un bubble_sort que funcione para Linked Lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.top = None

    def append(self, data):
        new_node = Node(data)
        if not self.top:
            self.top = new_node
            return
        
        current = self.top
        while current.next:
            current = current.next
        current.next = new_node

    def print_linked_list(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def swap_nodes(self, prev, node1, node2):#Funcion para intercambiar nodos de posicion y se retornan en orden inverso
        if prev:
            prev.next = node2
        else:
            self.top = node2

        node1.next = node2.next
        node2.next = node1

    def bubble_sort(self, ascending=True):
        if not self.top or not self.top.next:
            return  # Se comprueba que hayan nodos que ordenar

        swapped = True  # Uso recomendado de una bandera para comprobar que hay cambios
        while swapped:
            swapped = False
            prev = None
            current = self.top

            while current and current.next:
                next_node = current.next
                if (ascending and current.data > current.next.data) or (not ascending and current.data < current.next.data): #Con este metodo se comprueba si los nodos deben ser intercambiados
                    self.swap_nodes(prev, current, current.next)
                    swapped = True
                    prev = next_node
                else:
                    prev = current
                    current = current.next #Se actualizan valores de Current y Prev

# Ejemplo:
#Primero se agregan nodos a la lista
my_linked_list = LinkedList()
my_linked_list.append(5)
my_linked_list.append(2)
my_linked_list.append(9)
my_linked_list.append(1)
my_linked_list.append(8)

print("Esta es la lista sin cambios:")
my_linked_list.print_linked_list()

my_linked_list.bubble_sort(ascending=True)  # Orden ascendente
print("\nLista despues de ser ordenada de manera ascendente: ")
my_linked_list.print_linked_list()

my_linked_list.bubble_sort(ascending=False)  # Orden descendente
print("\nLista despues de ser ordenada de manera descendente:")
my_linked_list.print_linked_list()