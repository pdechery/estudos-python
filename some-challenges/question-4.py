'''
Use the next() function to find the first element in a list of dictionaries whose attribute ‘x’ = 5. 
Default to an empty dictionary if not found.
'''

list_of_dicts = [
  {
    'x':1,
    'y':4,
    'z':5
  },
  {
    'x':5,
    'y':12,
    'z':3
  },
  {
    'x':7,
    'y':2,
    'z':3
  }
]

def find_the_right_x(dataset, right_value):
  it = iter(dataset)
  if next(it)['x'] == right_value:
    return dataset[0]
  elif next(it)['x'] == right_value:
    return dataset[1]
  elif next(it)['x'] == right_value:
    return dataset[2]
  else:
    return {}
    

if __name__ == '__main__':
  print(find_the_right_x(list_of_dicts, 5))
  


