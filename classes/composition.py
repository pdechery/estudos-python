# composition

class Job:
    def __init__(self, job):
        self.job = job
    
    def __str__(self):
        return f"Meu trabalho é ser {self.job}"

class Geo:
    def __init__(self, pais):
        self.pais = pais

    def __str__(self):
        return f"{self.pais}"

class Pessoa:
    def __init__(self, nome, job, pais):
        self.nome = nome
        self.job = Job(job)
        self.pais = Geo(pais)
        self.__salario = 20

    @staticmethod
    def body():
        return "Todas as pessoas possuem dois braços e duas pernas"

    @property
    def salario(self):
        salario = self.__salario-10
        return f"{salario}K"

    @salario.setter
    def salario(self, novo_salario):
        self.__salario = novo_salario+10

    def __str__(self):
        return f"Meu nome é {self.nome} e eu trabalho como {self.job} e moro no {self.pais}"


if __name__ == "__main__":
    
    pessoa = Pessoa("Pierre", "Dev", "Brasil")
    pessoa.salario = 100

    print(pessoa.nome)
    print(pessoa.job)
    print(pessoa.salario)
