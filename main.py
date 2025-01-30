import serial

class Machine:
    def __init__(self):
        self.xSize = 250
        self.ySize = 250
        self.zSize = 250
        self._position = [0,0,0] # X Y Z
        self._homed = False # Has the printer been homed so it knows where it is

    def homeMachine (self):
        command = "G28"
        printer.write(command.encode())
        response = printer.readline().decode()
        self._homed = True
        print(response)
        return True

    def moveToPoint (self,x,y,z):
        if x > self.xSize or y > self.ySize or z > self.zSize or x < 0 or y < 0 or z < 0 :
            print("Movement would exced machine limits, Tried To move to:", x, y, z, "x,y,z")
            return False
        if not self._homed:
            print("Machine needs to be homed first (g28 Command) before it can move")
            return False
        xDist = str(x - self._position[0])
        yDist = str(y - self._position[1])
        zDist = str(z - self._position[2])
        command = "G0" + "x" + xDist + "y" + yDist + "z" + zDist
        printer.write(command.encode())
        response = printer.readline().decode()
        print(response)
        self._position = [x,y,z]

    def absMove (self,x,y,z):
        if x + self._position[0] > self.xSize or y + self._position[1] > self.ySize or z + self._position[2] > self.zSize or x + self._position[0] < 0 or y+ self._position[1] < 0 or z + self._position[2] < 0 :
            print("Movement would exced machine limits, Tried To move to:", x, y, z, "x,y,z")
            return False
        if not self._homed:
            print("Machine needs to be homed first (g28 Command) before it can move")
            return False
        xDist = str(x)
        yDist = str(y)
        zDist = str(z)
        command = "G0" + "x" + xDist + "y" + yDist + "z" + zDist
        printer.write(command.encode())
        response = printer.readline().decode()
        print(response)
        self._position = [self._position[0] + x, self._position[1] + y, self._position[2a]+ z]

class Bottle:
    def __init__(self):
        self._size = [0,0] # X Y
        self._position = [0,0] # X Y
        self.content = ""

class Chemical:
    def __init__(self):
        self._name = "None"
        self._description = "Something Interesting"

# Create a machine if one does not exist

# Connect to machine via serial
printer = serial.Serial('COM3', 9600)