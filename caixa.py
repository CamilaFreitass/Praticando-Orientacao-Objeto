
class Caixa:

    def __init__(self, operador, codigo, tipo):
        print(f'Construindo o objeto {self}')
        self.__operador = operador
        self.__codigo = codigo
        self.__tipo = tipo

    @property
    def operador(self):
        return self.__operador

    @property
    def codigo(self):
        return self.__codigo

    @property
    def tipo(self):
        return self.__tipo

    @operador.setter
    def operador(self, operador):
        print('Mudando o operador...')
        self.__operador = operador

    @staticmethod
    def abrir_fechar_caixa():
        return { '1': 'ABERTA', '0': 'FECHADA'}

