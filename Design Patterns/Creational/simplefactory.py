class WoodenDoor:
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

class DoorFactory:
    def __init__(self):
        self.width = 0
        self.height = 0

    def makeDoor(self, width, height):
        self.width = width
        self.height = height
        self.door = WoodenDoor(width, height)
        return self.door

w = DoorFactory()
w.makeDoor(2,4)
print(w.width, w.height)