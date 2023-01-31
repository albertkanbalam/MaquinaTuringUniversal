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
        print("\n  - Ingresar como parámetro el nombre del archivo")
        print("    que contiene la descripción de la Máquina de Turing\n")
        sys.exit()

    if not os.path.isfile('descripciones/' + sys.argv[1]):
        print("\n  - No existe archivo {}\n".format(sys.argv[1]))
        sys.exit()
    try:
        archivo_mt = json.load(open('descripciones/' + sys.argv[1], 'r'))
    except Exception as ex:
        print("  - El archivo {} está mal formado".format(sys.argv[1]))
        print(ex)
        sys.exit()

    cadena = input("  Insertar cadena de entrada: ")
    M = MaquinaTuringUniversal(archivo_mt, cadena)
    M.muestra_maquina()
    M.procesa_cadena_verbose()
