from abc import ABC,abstractmethod

class vehicle(ABC):     #defining classes
    @ abstractmethod
    def speed(self):
        print("Information about the vehicle is: ")

class fourwheeler(vehicle):
    def __init__(self,name,speed1):
        self.name=name
        self.speed1=speed1
    def speed(self):
        super().speed()
        print("The name of the vehicle is: ",self.name)
        print("The speed of the vehicle is: ",self.speed1)

class twowheeler(vehicle):
    def __init__(self,name,speed1):
        self.name=name
        self.speed1=speed1
    def speed(self):
        super().speed()
        print("The name of the vehicle is: ",self.name)
        print("The speed of the vehicle is: ",self.speed1)

vehicle1=fourwheeler("Maruti",20)
vehicle1.speed()
print("\n")
vehicle2=twowheeler("Honda",60)
vehicle2.speed()
