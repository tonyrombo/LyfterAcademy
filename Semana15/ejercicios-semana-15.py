#1. Crea un bubble_sort por tu cuenta sin revisar el código de la lección.

def bubble_sort(numbers): #o(n)
    for first_index in range(len(numbers)):#o(n)
        is_swapped = False#o(n)
        for second_index in range(len(numbers) - 1 - first_index):#o(n2)
            if numbers[second_index] > numbers[second_index + 1]: #o(n)
                numbers[second_index], numbers[second_index + 1] = numbers[second_index + 1], numbers[second_index] #Code to swap values in a simple way and avoid the use of a temporary variable
                is_swapped = True
        if not is_swapped:
            break
    return numbers

# Example
my_list = [5, 2, 9, 1, 5, 6, -2]
print(bubble_sort(my_list))

#2. Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero (como en la imagen de abajo).

def reversed_bubble_sort(numbers):
    is_swapped = False
    for first_index in range(len(numbers)):
        for second_index in range(len(numbers) - 1, first_index, -1):  # Reversing the for loop
            if numbers[second_index] < numbers[second_index - 1]:  # Swapping if previous is lower
                numbers[second_index], numbers[second_index - 1] = numbers[second_index - 1], numbers[second_index]
                is_swapped = True
        if not is_swapped:
            break
    return numbers

# Example:
my_list = [5, 2, 9, 1, 5, 6]
print(reversed_bubble_sort(my_list))


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

    def swap_nodes(self, prev, node1, node2):#Function to swap position of nodes and returns the reversed order
        if prev:
            prev.next = node2
        else:
            self.top = node2

        node1.next = node2.next
        node2.next = node1

    def bubble_sort(self, ascending=True):
        if not self.top or not self.top.next:
            return  # Verifies that there are nodes to order

        swapped = True  # Recommended use of a flag to verify that there are changes
        while swapped:
            swapped = False
            prev = None
            current = self.top

            while current and current.next:
                next_node = current.next
                if (ascending and current.data > current.next.data) or (not ascending and current.data < current.next.data): # This method verifies if the nodes nedd to be swapped
                    self.swap_nodes(prev, current, current.next)
                    swapped = True
                    prev = next_node
                else:
                    prev = current
                    current = current.next # Updating values of Current and Prev

# Example:
# Adding nodes to the list first
my_linked_list = LinkedList()
my_linked_list.append(5)
my_linked_list.append(2)
my_linked_list.append(9)
my_linked_list.append(1)
my_linked_list.append(8)

print("Linked List without changes:")
my_linked_list.print_linked_list()

my_linked_list.bubble_sort(ascending=True)  # Ascending order
print("\nLinked List after being sorted in ascending order: ")
my_linked_list.print_linked_list()

my_linked_list.bubble_sort(ascending=False)  # Descending order
print("\nLinked List after being sorted in descending order:")
my_linked_list.print_linked_list()