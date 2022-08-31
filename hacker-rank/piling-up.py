'''
Piling Up

https://www.hackerrank.com/challenges/piling-up

Dado uma lista de números verificar se é possível empilha-los em ordem decrescente (maior em baixo, menor em cima).

O empilhamento deve ser feito passo a passo e a cada passo só se pode usar um item do canto esquerdo ou direito.

O item de cima sempre tem que ser menor que o de baixo.

Retornar True se for possível criar a pilha e False se não (o ultimo item for maior que o de baixo)

--

Sobre float('inf')

https://www.geeksforgeeks.org/python-infinity/#:~:text=As%20of%202020%2C%20there%20is,to%20represent%20it%20as%20infinity.

'''

from collections import deque

def pile_up(blocks):

	stack = deque()

	num = float('inf')

	result = "Yes"

	while len(blocks):

		if blocks[0] >= blocks[-1]:
			block = blocks.popleft()
		else:
			block = blocks.pop()

		print(blocks)

		# if len(stack) > 0:
		# 	if block > stack[0]:
		# 		result = "No"
		# else:
		# 	stack.appendleft(block)

		if block > num:
			result = "No"
		num = block

		print(num)

	print('block')
	print(block)

	return result


if __name__ == '__main__':

	test_cases = int(input())

	for _ in range(test_cases):

		row = int(input())

		blocks = map(int, input().split())

		res = pile_up(deque(blocks))

		print(res)

'''
Outra Solução:

def Solution(lst):
  pile = float('inf')
  while lst:
    num = lst.pop(0) if lst[0] > lst[-1] else lst.pop(-1)
    if num > pile: return "No"
    pile = num
  return "Yes"

def main():
  t = int(input())
  for _ in range(t):
    n = int(input())
    lst = list(map(int, input().strip().split()))
    print(Solution(lst))
'''

