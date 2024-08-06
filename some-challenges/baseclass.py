'''
Create a base class with:
   - Three properties initialized at construction
   - One empty classmethod
   - One empty instance method
'''

class BaseCar:

  c_mileage =  75000 

  def __init__(self):
    self.make = "Honda"
    self.year = 2020
    self.automatic = True

  @classmethod
  def get_mileage(cls):
    pass

  def get_make(self):
    pass





