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

