#carexample5.py

class Car:

    c_mileage_units = "Mi"

    __max_speed = 200

    def __init__(self, color, miles, model):
        self.i_color = color
        self.i_mileage = miles
        self.__no_doors = 4
        self._model = model

    def __str__(self):
        return f"car with color {self.i_color}, mileage {self.i_mileage}, model {self._model} and doors {self.__doors()}"

    def __doors(self):
        return self.__no_doors

    @property
    def max_speed(self):
        return self.__max_speed

    @property
    def no_doors(self):
        return self.__no_doors

if __name__ == "__main__":

    car = Car("blue", 1000, "Camry")

    print (car)

    # Dá erro
    # print (car.__no_doors)

    # assim pode
    # print (car._Car__doors())