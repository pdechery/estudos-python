# Tentando entender como funciona a variável __main__

'''
main program != imported
'''

import mod1

print("mod2 __name__ = %s " % __name__)

if __name__ == "__main__":
    print("mod2 está sendo rodado diretamento. É o \"script principal\"")
else:
    print("mod2 está sendo importado por outro módulo")