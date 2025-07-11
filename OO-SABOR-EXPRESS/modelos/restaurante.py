from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
        self.avaliacao = []

    def __str__(self):
        return f'{self._nome} | {self.categoria} '
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'
    
    def alter_state(self):
        self._ativo = not self._ativo

    def recive_aval(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self.avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self.avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self.avaliacao)
        quantidade_de_notas = len(self.avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media