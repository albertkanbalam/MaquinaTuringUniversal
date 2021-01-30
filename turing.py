# -*- coding: utf-8 -*-
"""
Implementación del Algoritmo universal. Lee la descripción
de una Máquina de Turing y la ejecuta.
"""
import sys

from simbolo import Simbolo


class MaquinaTuringUniversal:
    '''
    Simula una Máquina de Turing procesando una cadena.

    - La especificación de la Máquina de Turing se encuentra
    en un archivo cuyo nombre es recibido como primer parámetro.
    - La cadena se recibe como un string en el segundo parámetro.

    La máquina por default permite una cinta con multiples pistas.
    '''

    def __init__(self, descripcion_mt, cadena):

        self.MT = descripcion_mt
        self.cadena = cadena
        self.estado_inicial = self.MT['Inicial']
        self.estados_finales = self.MT['Finales']
        self.blanco = self.MT['Blanco']

        # El número de pistas se toma del tamaño del arreglo de los símbolos
        self.num_pistas = len(self.MT['Transiciones'][0][1])

        # Inicializamos la cinta con dos blancos
        self.cinta = [
            Simbolo(self.num_pistas, blanco=self.blanco, cabeza=self.blanco),
            Simbolo(self.num_pistas, blanco=self.blanco, cabeza=self.blanco)
        ]

        # Las transiciones quedan guardadas como diccionario
        self.transiciones = self.__parsea_transiciones()

        # Estado y simbolo que está leyendo la cabeza
        self.estado = self.estado_inicial
        self.simbolo = Simbolo(
            self.num_pistas, blanco=self.blanco, cabeza=self.blanco)

        # La posición la cabeza de la máquina dentro de la cadena
        self.indice_cabeza = 0

        self.contador_transiciones = 0

    def __parsea_transiciones(self):
        '''
        Lee las transiciones de la especificación JSON
        y las trasnforma en diccionario.
        '''
        if len(self.MT['Transiciones']) == 0:
            print("\n  No hay transiciones en el archivo de descripción.\n")
            sys.exit()
        if not isinstance(self.MT['Transiciones'][0][1], type([])):
            print(
                "\n  Los símbolos del alfabeto de la cinta en "
                "las transiciones  deben ser arreglos.")
            sys.exit()
        if not isinstance(self.MT['Transiciones'][0][3], type([])):
            print(
                "\n  Los símbolos del alfabeto de la cinta en "
                "las transiciones deben ser arreglos.")
            sys.exit()

        transiciones_dict = {}
        for t in self.MT['Transiciones']:
            transiciones_dict[(t[0], str(t[1]))] = (t[2], str(t[3]), t[4])
        return transiciones_dict

    def __formato_descr(self, name, lista):
        '''
        Método auxiliar para el método 'muestra_maquina()'.
        '''
        print(name, "{", end='')
        for e in lista[:-1]:
            print("{}, ".format(e), end="")
        print("{}}}".format(lista[-1]))

    def muestra_maquina(self):
        '''
        Muestra una representación amigable de especificación de
        la Máquina de Turing.
        '''
        print("\n  Máquina de Turing: ({} pista{})".format(
            self.num_pistas, ((self.num_pistas-1)*'s')[:1]))
        self.__formato_descr("\tQ: ", self.MT["Estados"])
        self.__formato_descr("\t\u03A3: ", self.MT['Entrada'])
        self.__formato_descr("\t\u0393: ", self.MT['Cinta'])
        self.__formato_descr("\tF: ", self.estados_finales)
        print("\tq0:", self.estado_inicial)
        print("\tTransiciones: ")
        for t in self.MT["Transiciones"]:
            print("\t\t\u03B4({}, {}) = ({}, {}, {})".format(t[0],
                                                             t[1],
                                                             t[2],
                                                             t[3],
                                                             t[4]))
        print("\n")

    def muestra_instantanea(self):
        '''
        Construye y muestra una representación amigable de la
        configuración de la Máquina de Turing en el momento en que
        se llama al método.
        '''
        pista_principal = "{}{}".format(
            ''.join(list(map(lambda s: '| {} '.format(s.first()),
                             self.cinta[:self.indice_cabeza]))),
            ''.join(list(map(lambda s: '| {} '.format(s.first()),
                             self.cinta[self.indice_cabeza:]))))

        print("        ", end='')
        for s in self.cinta:
            print("____", end='')
        print("_", end='')

        print("\npista1: {}|".format(pista_principal))
        for i in range(1, self.num_pistas):
            pista = "pista{}: {}{}|".format(
                i+1,
                ''.join(list(map(lambda s: '| {} '.format(s.atomos[i]),
                                 self.cinta[:self.indice_cabeza]))),
                ''.join(list(map(lambda s: '| {} '.format(s.atomos[i]),
                                 self.cinta[self.indice_cabeza:]))))
            print(pista)
        print("        ", end='')
        print("{}|{}{}|{}".format(
            ''.join(list(map(lambda s: '    '.format(s.first()),
                             self.cinta[:self.indice_cabeza]))),
            self.estado,
            ' '*(3-len(self.estado)),
            ''.join(list(map(lambda s: '    '.format(s.first()),
                             self.cinta[self.indice_cabeza:])))))

    def lee_simbolo(self):
        '''
        Obtiene el símbolo que está leyendo la cabeza en el momento.
        '''
        self.simbolo = self.cinta[self.indice_cabeza]

    def escribe_simbolo(self, reemplazo):
        '''
        Recibe el símbolo a reemplazar en la cinta y lo escribe.
        '''
        s = self.cinta[self.indice_cabeza]
        s.actualiza_atomos(reemplazo)
        self.cinta = self.cinta[:self.indice_cabeza] + \
            [s] + self.cinta[self.indice_cabeza+1:]

    def mueve_cabeza(self, direccion):
        '''
        Mueve la cabeza de la Máquina de Turing haciendo uso
        de los métodos de direccionamiento según la dirección recibida.
        '''
        self.indice_cabeza = {
            'L': self.L(),
            'R': self.R(),
            'N': self.N()
        }[direccion]

    def N(self):
        '''
        Corresponde al movimiento Neutro de la cabeza.
        '''
        return self.indice_cabeza

    def L(self):
        '''
        Corresponde al movimiento a la izquierda de la cabeza.
        '''
        return self.indice_cabeza - 1

    def R(self):
        '''
        Corresponde al movimiento a la derecha de la cabeza.
        '''
        return self.indice_cabeza + 1

    def transita(self):
        '''
        De acuerdo al estado y símbolo que se está leyendo, este método
        busca la correspondiente transición, escribe el símbolo de reemplazo
        y mueve la cabeza en la dirección obtenida.

        Regresa True si la máquina debe seguir transitando.
        Regresa False si no existe transición para el estado y el símbolo.

        '''
        self.contador_transiciones += 1
        self.lee_simbolo()
        if (self.estado, repr(self.simbolo.atomos)) not in self.transiciones:
            return False

        self.estado, s_reemplazo, direccion = self.transiciones.get(
            (self.estado, repr(self.simbolo.atomos))
        )
        self.escribe_simbolo(s_reemplazo)
        self.mueve_cabeza(direccion)
        return True

    def escribe_cinta(self, cadena):
        '''
        Toma la cadena que procesará la Máquina y la escribe en la cinta.
        '''
        nueva_cinta = []
        for c in cadena:
            nueva_cinta.append(
                Simbolo(self.num_pistas, blanco=self.blanco, cabeza=c))
        self.cinta = nueva_cinta + self.cinta

    def procesa_cadena(self):
        '''
        Ejecuta la Máquina de Turing con la cadena recibida al inicio.

        Regresa True si la cadena es aceptada. Regresa False cuando no hay
        transición para el par(estado, símbolo) que se está leyendo.
        '''
        cadena_entrada = self.cadena
        self.escribe_cinta(cadena_entrada)
        while self.estado not in self.estados_finales:
            seguir = self.transita()
            if not seguir:
                return False
        return True

    def procesa_cadena_verbose(self):
        '''
        Ejecuta la Máquina de Turing con la cadena recibida al inicio y
        muestra configuraciones en cada transición.

        Regresa True si la cadena es aceptada. Regresa False cuando no hay
        transición para el par(estado, símbolo) que se está leyendo.
        '''
        cadena_entrada = self.cadena
        print("  Cadena a procesar: {}\n\n".format(cadena_entrada))
        self.escribe_cinta(cadena_entrada)
        self.muestra_instantanea()
        print("\n\n  Presionar ENTER para mostrar configuraciones\n\n")
        while self.estado not in self.estados_finales:
            input()
            seguir = self.transita()
            if not seguir:
                print("\n\n Cadena \"{}\" no aceptada.".format(cadena_entrada))
                print(" No hay transición para ({}, {})\n\n".format(
                    self.estado, self.simbolo.atomos_representacion_cadena()))
                return False
            self.muestra_instantanea()

        print("\n\n\n  Cadena \"{}\" aceptada.".format(cadena_entrada))
        print("  {} transiciones\n\n".format(self.contador_transiciones))
        return True
