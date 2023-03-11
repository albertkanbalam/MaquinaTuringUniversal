# -*- coding: utf-8 -*-
"""
Implementación del Algoritmo universal. Lee la descripción
de una Máquina de Turing y la ejecuta.
"""
import os
import sys
import importlib.util

from turing import MaquinaTuringUniversal


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\n  - INGRESAR COMO PARÁMETROS EL NOMBRE DEL ARCHIVO")
        print("  QUE CONTIENE LA DESCRIPCION DE LA MAQUINA DE TURING\n")
        sys.exit()

    if not os.path.isfile('descripciones/' + sys.argv[1]):
        print(f"\n  - NO EXISTE EL ARCHIVO {sys.argv[1]} \n")
        sys.exit()
    try:
        # archivo_mt = json.load(open('descripciones/' + sys.argv[1], 'r'))
        spec = importlib.util.spec_from_file_location('descripcion',
                                                      'descripciones/' +
                                                      sys.argv[1])
        archivo_mt = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(archivo_mt)

    except Exception as ex:
        print(f"\n EL ARCHIVO {sys.argv[1]} ESTA MAL FORMADON \n")
        print(ex)
        sys.exit()

    cadena = input("  Insertar cadena de entrada: ")
    M = MaquinaTuringUniversal(archivo_mt.descripcion, cadena)
    M.muestra_maquina()
    M.procesa_cadena_verbose()
