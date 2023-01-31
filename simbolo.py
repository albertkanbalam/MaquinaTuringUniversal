# -*- coding: utf-8 -*-


class Simbolo:
    '''
    Representa un símbolo de para la cinta de la Máquina de Turing.

    El símbolo consiste en un arreglo de átomos (se espera que sean
    caracteres, aunque podrían ser de otro tipo). Éste arreglo representa
    múltiples pistas para la cinta.
    '''

    def __init__(self, num_pistas, blanco='_', cabeza='_'):
        '''
        Inicializamos el símbolo con espacios en blanco.
        '''
        self.num_pistas = num_pistas
        self.atomos = [blanco]*self.num_pistas
        self.escribe_cabeza(cabeza)

    def escribe_cabeza(self, a):
        self.atomos[0] = a

    def actualiza_atomos(self, atomos):
        self.atomos = atomos.replace('[', '').replace(']', '').replace(
            "'", '').replace(" ", '').split(',')

    def atomos_representacion_cadena(self):
        cadena = '('
        for e in self.atomos[:-1]:
            cadena = cadena + f"{e}, "
        cadena = cadena + f"{self.atomos[-1]})"
        return cadena

    def first(self):
        return self.atomos[0]

    def __repr__(self):
        return str(self.atomos)
