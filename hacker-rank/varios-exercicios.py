
def find_twice_char(word):
    '''
    Verificar se a string possui dois caracteres iguais *consecutivos*.
    '''

    for i,v in enumerate(word):
        if i < len(word)-1:
            if v == word[i+1]:
                return True
        
    return False

def find_median(arr):

    '''
    Encontrar a mediana da lista.
    Mediana é o elemento do meio que subdivide a lista em subgrupos com o mesmo numero de elementos
    Exemplo:
    [1,4,3,5,8]
    Mediana = 3
    '''
    
    arr.sort() # Sort IN PLACE and returns None

    # So, this doesn't work
    # test = arr.sort()
    # test
    # None

    median = len(arr) // 2
    
    return arr[median+1]


def diagonal_difference(m):

    '''
    Calcular a soma das diagonais numa matriz e retornar a diferença absoluta dessas somas
    '''

    l = len(m[0])

    dg1 = [m[x][y] for x in range(l) for y in range(l) if x == y]

    dg2 = [m[x][y] for x in range(l) for y in range(l) if y == (l-1)-x]

    return abs(sum(dg1) - sum(dg2))


if __name__ == '__main__':
    
    #res = find_median([0,1,2,4,6,5,3])

    l1 = '11 2 4'
    l2 = '4 5 6'
    l3 = '10 8 -12'

    m = list()

    m = [
        [int(i) for i in l1.split(' ')],
        [int(i) for i in l2.split(' ')],
        [int(i) for i in l3.split(' ')]
    ]

    #res = diagonal_difference(m)

    res = find_twice_char('hello')

    print(f'res {res}')