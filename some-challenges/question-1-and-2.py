'''
Create a derived class from the base class
  - Inherits all properties and methods from the base class
  - Initialize the properties differently from the base class
  - Add code to the empty methods
'''

from baseclass import BaseCar

class Car(BaseCar):
  def __init__(self, model, color):
    self.model = model 
    self.color = color
    super().__init__()

  def get_model(self):
    print(f'My car\'s model is {self.model}')

  def get_color(self):
    print(f'My car\'s color is {self.color}')

  # Base Class methods

  def get_mileage(cls):
    print(f'My car has {cls.c_mileage} miles driven')

  def get_make(self):
    print(f'My car is a {self.make}')

  def get_year(self):
    print(f'My car was built in {self.year}')

  def get_automatic(self):
    resp = "My car is automatic" if self.automatic else "My car is manual"
    print(resp)


if __name__ == '__main__':
  mycar = Car("Accord", "White")
  mycar.get_make()
  mycar.get_year()
  mycar.get_automatic()
  mycar.get_model()
  mycar.get_color()
  mycar.get_mileage()