'''

https://www.hackerrank.com/challenges/list-comprehensions


Listar todas coordenadas possiveis de um cubo num gráfico 3D.

Num gráfico 3D as coordenadas são representadas por:

x (eixo horizontal)
y (eixo vertical)
z (eixo profundidade)

Regras:

i < x
j < y
k < z

i,j,k > 0

Dado que: 

x = 1
y = 1
z = 2

As coordenadas possíveis são:

Eixo X => (0,0,0) (1,0,0)

Eixo Y => (0,0,0) (0,1,0)

Eixo Z => (0,0,0) (0,0,1) (0,0,2)


'''

x = 1 
y = 3
z = 2

# Com For

def getCoordinates():

	coordinates = []
	
	for i in range(x+1):
		for j in range(y+1):
			for k in range(z+1):
				coordinates.append([i,j,k])

	return coordinates

# Com List Compreension

def  getCoordinatesListComp():

	#coordinates = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]

	#coordinates = [c for c in coordinates if sum(c) != 3]

	# Segunda versão refatorada
	coordinates = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != 3]

	return coordinates

# Outra solução:
# https://programs.programmingoneonone.com/2021/01/hackerrank-list-comprehensions-solution-python.html

if __name__ == '__main__':

	print(getCoordinatesListComp())

	

