import serial

class Machine:
    def __init__(self):
        self._position = [0,0,0] # X Y Z

    def homeMachine (self):
        command = "G28"
        printer.write(command.encode())
        response = printer.readline().decode()
        print(response)

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