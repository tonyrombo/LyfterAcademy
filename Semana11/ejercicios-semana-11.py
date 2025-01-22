import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        pi = math.pi
        area = pi * (self.radius ** 2)
        return area
    

# new_circle = Circle(25)
# print(new_circle.getArea())


class Person:
    def __init__(self, name):
        self.name = name

class Bus:
    def __init__(self, max_passengers=50, current_passengers=0):
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers
        self.passengers = []

    def add_passengers(self, *persons): #Se utiliza * antes del parametro para indicar que se pueden agregar varios del mismo
        try:

            for person in persons:
                if not isinstance(person, Person): #Se utiliza este metodo para validar que el elemento es una instancia de Person
                    raise TypeError(f"{person} debe ser una instancia de la clase Person")

                if self.current_passengers + 1 > self.max_passengers:
                    print(f"No hay espacio para {person.name}. El autobús está lleno.")
                else:
                    self.passengers.append(person)
                    self.current_passengers += 1
                    print(f"{person.name} ha subido al autobús. Pasajeros actuales: {self.current_passengers}/{self.max_passengers}.")

        except TypeError as error:
            print(f"Error: {error}")

    def remove_passenger(self, person_name):
        try:
            for person in self.passengers:
                if person.name == person_name:
                    self.passengers.remove(person)
                    self.current_passengers -= 1
                    print(f"{person_name} ha bajado del autobús.")
                    return
                else:
                    print(f"{person_name} no está en el autobús.")
        except TypeError as error:
            print(f"Error: {error}")

new_bus = Bus()
person1 = Person("Tony")
person2 = Person("Carlos")
person3 = Person("Emily")

new_bus.add_passengers(person1)
new_bus.add_passengers(person2, person3)


class Head:
    def __init__(self, eyes, nose_size, mouth_gesture):
        self.eyes = eyes
        self.nose_size = nose_size
        self.mouth_gesture = mouth_gesture

class Torso:
    def __init__(self, head, right_arm, left_arm, legs):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.legs = legs

class Arm:
    def __init__(self, hand, muscles):
        self.hand = hand
        self.muscles = muscles

class Hand:
    def __init__(self, fingers):
        self.fingers = fingers

class Leg:
    def __init__(self, foot, muscles):
        self.foot = foot
        self.muscles = muscles

class Feet:
    def __init__(self, toes):
        self.toes = toes

class Human:
    def __init__(self, head, torso, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.torso = torso
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg

right_hand = Hand(5)
left_hand = Hand(5)

right_arm = Arm(right_hand, "strong")
left_arm = Arm(left_hand, "weak")

right_foot = Feet(5)
left_foot = Feet(5)

right_leg = Leg(right_foot, "strong")
left_leg = Leg(left_foot, "average")

head = Head(2, "small", "smiling")

torso = Torso(head, right_arm, left_arm, [right_leg, left_leg])

human = Human(head, torso, right_arm, left_arm, right_leg, left_leg)

# print(f"Human's head has {human.head.eyes} eyes, a {human.head.nose_size} nose, and a {human.head.mouth_gesture} mouth.")
# print(f"Right hand has {human.right_arm.hand.fingers} fingers.")
# print(f"Left foot has {human.left_leg.foot.toes} toes.")