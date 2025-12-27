class Pessoa:
    nome = "João"
    idade = 25
    altura = 1.75
    peso = 70.0
    eh_estudante = True
    cidade = "São Paulo"
    profissao = "Engenheiro"
    estado_civil = "Solteiro"
    nacionalidade = "Brasileiro"
    genero = "Masculino"
    idioma = "Português"
    hobby = "Futebol"
    comida_favorita = "Feijoada"
    musica_favorita = "Samba"
    def apresentar(self):
        return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e sou {self.profissao}."
eu = Pessoa()
print(eu.apresentar())
print(eu.nome)
print(eu.idade)
print(eu.altura)
print(eu.peso)
print(eu.eh_estudante)
print(eu.cidade)
print(eu.profissao) 
print(eu.estado_civil)
print(eu.nacionalidade)
print(eu.genero)
print(eu.idioma)
print(eu.hobby)
print(eu.comida_favorita)
print(eu.musica_favorita)   