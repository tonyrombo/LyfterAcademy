#1. Cree una estructura de objetos que asemeje un Stack.
    #1. Debe incluir los métodos de `push` (para agregar nodos) y `pop` (para quitar nodos).
    #2. Debe incluir un método para hacer `print` de toda la estructura.
    #3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top  = None

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

# Ejemplo
stack = Stack()
stack.push(100)
stack.push(200)
stack.push(300)
stack.push(400)
stack.push(500)
stack.print_stack()
print("Elemento eliminado:", stack.pop())
stack.print_stack()

#2. Cree una estructura de objetos que asemeje un Double Ended Queue.
    #1. Debe incluir los métodos de `push_left` y `push_right` (para agregar nodos al inicio y al final) y `pop_left` y `pop_right` (para quitar nodos al inicio y al final).
    #2. Debe incluir un método para hacer `print` de toda la estructura.
    #3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class Double_Ended_Queue:
    def __init__(self):
        self.head = None
        self.foot = None

    def push_left(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.foot = new_node #Método para asignar el mismo valor a 2 variables: self.head y self.foot al no haber data
        else:
            new_node.next = self.head #self.head pasa a ser el siguiente de new_node
            self.head.prev = new_node #new_node se asigna como el anterior a self.head para tenerlos comunicados entre si
            self.head = new_node #new_node pasa a ser el nuevo head

    def push_right(self, data):
        new_node = Node(data)
        if not self.foot:
            self.head = self.foot = new_node
        else:
            new_node.prev = self.foot
            self.foot.next = new_node
            self.foot = new_node

    def pop_left(self):
        if not self.head:
            print("No hay nodos para eliminar.")
            return None
        
        data = self.head.data
        self.head = self.head.next #el siguiente de head pasa a ser el nuevo head

        if self.head:  # Se verifica si no quedó vacío
            self.head.prev = None
        else:  # Si quedó vacía
            self.foot = None

        return data

    def pop_right(self):
        if not self.foot:
            print("No hay nodos para eliminar.")
            return None
        
        value = self.foot.data
        self.foot = self.foot.prev

        if self.foot:
            self.foot.next = None
        else:
            self.head = None

        return value

    def print_double_ended_queue(self):
        current = self.head
        if not current:
            print("La deque está vacía.")
            return
        
        print(" Double Ended Queue de izquierda a derecha:", end=" ")
        while current:
            print(f"{current.data} ", end="")
            current = current.next
        print("\n" + "-" * 20)

# Ejemplo
deque = Double_Ended_Queue()
deque.push_left(10)
deque.push_right(20)
deque.push_left(5)
deque.push_right(30)

deque.print_double_ended_queue()

print("Elemento izquierdo eliminado:", deque.pop_left())
print("Elemento derecho eliminado:", deque.pop_right())
deque.print_double_ended_queue()

#3. Cree una estructura de objetos que asemeje un Binary Tree.
    #1. Debe incluir un método para hacer `print` de toda la estructura.
    #2. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_data):
        self.root = Node(root_data)

    def insert(self, data):
        self.insert_in_order(self.root, data)

    def insert_in_order(self, node, data):
        if not node:
            return Node(data)
        if data < node.data:
            node.left = self.insert_in_order(node.left, data)
        else:
            node.right = self.insert_in_order(node.right, data)
        return node

    def print_tree(self, node, prefix="", is_left=True):
        if node is None:
            return ""

        result = self.print_tree(node.right, prefix + ("│   " if is_left else "    "), False) #Encontré esta manera para ilustar los Nodos y conectarlos para un entendimiento mas simple
        result += f"{prefix}{'└── ' if is_left else '┌── '}{node.data}\n"
        result += self.print_tree(node.left, prefix + ("│   " if is_left else "    "), True)

        return result

    def __str__(self):
        return self.print_tree(self.root)

# Ejemplo
print("\nBinary Tree con sus diferentes niveles:\n")
tree = BinaryTree(50)
for element in [30, 70, 20, 40, 60, 80]: #Se crea el arbol con su primer nodo raíz y despues en un list se agregan cada uno de los niveles con orden de izquierda a derecha
    tree.insert(element)

print(tree)