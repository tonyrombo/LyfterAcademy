import math

class Circle:
    
    radius = 45

    def getArea(self, radius):
        pi = math.pi
        area = pi * (radius * radius)
        return area
    

#new_circle = Circle()
#print(new_circle.getArea(Circle.radius))


class Bus:
    max_passengers = 50
    current_Passengers=24

    def addPassengers(self, Person):
        if self.current_Passengers < self.max_passengers:
            self.current_Passengers += int(int(Person))
            print(f"Hay {self.current_Passengers} pasajeros")
        else: print("El bus se encuentra en su capacidad máxima")
    
    def removePassenger(self):
        if self.current_Passengers > 0:
            self.current_Passengers -= 1
            print(f"Hay {self.current_Passengers} pasajeros")
        else: print("El bus no tiene pasajeros para bajar.")

# new_bus = Bus()
# new_bus.removePassenger()

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

print(f"Human's head has {human.head.eyes} eyes, a {human.head.nose_size} nose, and a {human.head.mouth_gesture} mouth.")
print(f"Right hand has {human.right_arm.hand.fingers} fingers.")
print(f"Left foot has {human.left_leg.foot.toes} toes.")