# Programação Orientada a Objetos (POO) em Python
class MinhaClasse:
    nome = "Gerson"
    idade = 68
    def minha_apresentacao(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.") 

eu = MinhaClasse()
eu.minha_apresentacao()
# Saída: Olá, meu nome é Gerson e tenho 68 anos.
print(eu.nome)  # Saída: Gerson
print(eu.idade)  # Saída: 68