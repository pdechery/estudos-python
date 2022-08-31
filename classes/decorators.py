# carexample7.py

class Car:

    __mileage_units = "Mi"

    def __init__(self, col, mil):
        self.__color = col
        self.__mileage = mil

    def __str__(self):
        return f"car with color {self.color} and mileage {self.mileage}"

    '''
    getter "tradicional" não pythônico
    def get_color(self):
        return self.__color
    '''

    # getter pythônico usando decorator
    @property
    def color(self):
        return self.__color

    @property
    def mileage(self):
        return self.__mileage

    # setter pythônico
    @mileage.setter
    def mileage (self, new_mil):
        self.__mileage = new_mil

    @color.setter
    def color (self, new_color):
        self.__color = new_color

if __name__ == "__main__":

    car = Car ("blue", 1000)

    print (car)

    print (car.color)

    print(car.mileage)

    car.mileage = 2000

    print (car.color)

    print(car.mileage)