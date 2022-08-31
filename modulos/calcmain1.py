# calcmain1.py with a main function

from mycalculator import add as my_add
from mycalculator import subtract as my_subtract
from myrandom import random_2d, random_1d

def my_main( ):

    """ This is a main function which generates two random\     numbers and then apply calculator functions on them """

    x = random_2d( )

    y = random_1d( )

    sum = my_add(x, y)

    diff = my_subtract(x, y)

    print("x = {}, y = {}".format(x, y))

    print("sum is {}".format(sum))

    print("diff is {}".format(diff))

if __name__ == "__main__":

    my_main()