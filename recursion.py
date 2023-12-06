# https://realpython.com/python-recursion
# https://realpython.com/python-thinking-recursively/

"""
  Exemplo retirado de: https://99x.io/blog/recursion-is-not-hard-here-is-the-right-way-to-think
  
  Explicando:

  1) Call Stack

    getSum(3) -> a original
    getSum(2) -> feita de forma recursiva dentro da original
    getSum(1) -> segunda chamada recursiva

  2) Execução explicada

    O Call Stack trabalha em modo LIFO (Last In First Out). 
    Isso significa que a ultima chamada será a primeira a ser processada, e ai por diante.

    getSum(1) retorna 1 (if n == 1 return 1)

    getSum(2) será chamada em seguida.

    getSum(2) retorna 3, pois, dentro da função:
      - n = 2 
      - getSum(1) = 1

    Finalmente, getSum(3) será chamado.
      - n agora é 3
      - getSum(2) retornou 3

  Desse modo o final será 6, pois 3 + 3 = 6

"""
def getSum(n):
  if n == 1:
    return 1
  return n + getSum(n - 1)


"""
  Example with two consecutive recursive calls with instructions after calls

  Original dataset is [20, 6, 8, 19]

  At first it'll be divided in half and this line will run:

  recursiveExample(l_arr)

  This call will recursively be fed with this data:

  [20, 6]

  [20]

  As seen, only left side arrays so far (l_arr)

  When the parameter is [20] there'll be no more recursive call because of "len(dataset) > 1" rule.

  That means the function will be free to run next line. So it'll run -> recursiveExample(r_arr). 

  This time r_arr should be [6].

  Again no recursive calls, since len([6]) == 1. 

  At that point recursive calls are exhausted. The Call Stack will begin processing the stored 
  function calls in reverse order. That means [20,6] will be processed.

  We aren't doing anything so the function will complete its execution. But everything will start over again because of the next line: recursiveExample(r_arr)

  Now dataset is [8, 19].

  Same process will happen. [8,19] and then [8]

  After processing the recursive calls the callstack will pop the original call with [20, 6, 8, 19]

"""
def recursiveCompositionExample(dataset):
  print(f'this is the given data {dataset}')

  if len(dataset) > 1:
    print('started working (condition passed)')
    mid = len(dataset) // 2
    l_arr = dataset[:mid]
    r_arr = dataset[mid:]

    recursiveExample(l_arr)
    print('done with left side')
    recursiveExample(r_arr)
    print('done with right side')

    print(f'this is the final data after recursive calls {dataset}')


def is_palindrome(word):
  """Return True if word is a palindrome, False if not."""
  if len(word) <= 1:
    return True
  else:
    return word[0] == word[-1] and is_palindrome(word[1:-1])



if __name__ == '__main__':
  
  lindo_array = [20, 6, 8, 19]

  #print(is_palindrome('arara'))
  #recursiveCompositionExample(lindo_array)

