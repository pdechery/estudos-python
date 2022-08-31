# Tentando entender como funciona a variável __main__

print("mod1 __name__ = %s " % __name__)

if __name__ == "__main__":
    print("mod1 está sendo rodado diretamento. É o \"script principal\"")
else:
    print("mod1 está sendo importado por outro módulo")