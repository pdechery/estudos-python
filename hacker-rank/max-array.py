# Encontrar o segundo maior valor em uma lista

if __name__ == '__main__':
    
    n = int(input())
    arr = map(int, input().split())

    scoresList = list(arr)
    maxScore = max(scoresList)
    
    scoresList = list(filter(lambda x:x != maxScore, scoresList))
    
    print(scoresList)
    print(max(scoresList))