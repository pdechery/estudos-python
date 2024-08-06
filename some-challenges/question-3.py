# Use list comprehension and a lambda function to extract all of the even integers out of a list of integers

integers = list(range(12))
is_even = lambda i: i % 2 == 0
even_integers_list = [i for i in integers if is_even(i) == True]

if __name__ == '__main__':
  print(even_integers_list)