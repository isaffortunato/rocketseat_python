#@classmethod
#@staticmethod

class MinhaClasse:
    valor = 10 #parâmetro estático - Atributo de classe
    def __init__(self, nome) -> None:
        self.nome = nome #Atributo da instância

    #requer uma instância pra ser chamado
    def metodo_instância(self):
        return f"Método de instância chamado para {self.nome}" #poderia ser self.valor, ele consegue acessar atributos da classe
    
    @classmethod
    def metodo_classe(cls):
        return f"Método da classe chamado para valor = {cls.valor}"
    
    @staticmethod
    def metodo_estatico():
        return "Método estático chamado"


obj = MinhaClasse(nome="Classe Exemplo")
print(obj.metodo_instância())
'''
print(MinhaClasse.metodo_instância())
não é possível acessar diretamente pela classe, ele requer uma instância pra ser chamado (obj)
'''
print(MinhaClasse.valor) #dessa forma tb funciona, pq não precisa de instância p acessar atributo da classe
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

#exemplo de uso @classmethod
class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))

configuracao1 = "Toyota,Corolla,2022"
carro1 = Carro.criar_carro(configuracao1)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}")


#exemplo de uso @staticmethod
class Matematica:
    @staticmethod
    def somar(a, b):
        return a+b
    
print(Matematica.somar(a=20, b=15))
    