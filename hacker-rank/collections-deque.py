from collections import deque

d = deque()

if __name__ in '__main__':

    n = input()

    for _ in range(int(n)):

        res = input().split()
        
        if len(res) > 1:
            action = f'd.{res[0]}({res[1]})'
        else:
            action = f'd.{res[0]}()'
        
        eval(action)

    print(' '.join(map(lambda x: str(x), d)))