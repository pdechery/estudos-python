#methodsexample1.py

class Car:

    c_mileage_units = "Mi"

    def __init__(self, color, miles):
        self.i_color = color
        self.i_mileage = miles

    def print_color(self):
        print(f"Color of the car is {self.i_color}")

    @classmethod # método da classe
    def print_units(cls):
        print (f"mileage unit are {cls.c_mileage_units}")
        print(f"class name is {cls.__name__}")

    @staticmethod # método estático
    def print_hello():
        print ("Hello from a static method")

if __name__ == "__main__":

    car = Car("blue", 1000)

    # método de instância (objeto criado, recebe self como parâmetro)
    car.print_color()

    # método da classe sendo chamado do objeto
    car.print_units()

    # método da classe estático (não passa classe como parâmetro)
    car.print_hello()

    # se quero chamar um método de instância direto da classe preciso passar um objeto
    Car.print_color(car);

    Car.print_units();

    Car.print_hello()