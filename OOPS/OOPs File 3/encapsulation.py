# Encapsulation is showing essenyial feature and hiding some data

# Works on the concept of Public and Private

class Car:

    def __init__(self):
        self.__updateSoftware()  # Private Method (precedded by __)

    def drive(self):
        print('driving')

    def __updateSoftware(self):
        print('Update Software')

    def setMaxSoeed(self, speed):
        self.__maxspeed = speed


redcar = Car()
redcar.drive()
redcar.__maxspeed = 10 # Will not change the value as it is private
redcar.setMaxSpeed(320)
redcar.drive()
# redcar._Car__updateSoftware()  # Way to call Private Method


# Can chnage the value using Setter