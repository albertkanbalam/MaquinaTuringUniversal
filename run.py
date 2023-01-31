# -*- coding: utf-8 -*-
"""
Implementación del Algoritmo universal. Lee la descripción
de una Máquina de Turing y la ejecuta.
"""
import os
import sys
import json

from turing import MaquinaTuringUniversal


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\n  - INGRESAR COMO PARÁMETROS EL NOMBRE DEL ARCHIVO")
        print("  QUE CONTIENE LA DESCRIPCION DE LA MAQUINA DE TURING\n")
        sys.exit()

    if not os.path.isfile('descripciones/' + sys.argv[1]):
        print("\n  - NO EXISTE EL ARCHIVO {}\n".format(sys.argv[1]))
        sys.exit()
    try:
        archivo_mt = json.load(open('descripciones/' + sys.argv[1], 'r'))
    except Exception as ex:
        print("  - EL ARCHIVO {} ESTA MAL FORMADO".format(sys.argv[1]))
        print(ex)
        sys.exit()

    cadena = input("  Insertar cadena de entrada: ")
    M = MaquinaTuringUniversal(archivo_mt, cadena)
    M.muestra_maquina()
    M.procesa_cadena_verbose()
