Implementación de una Máquina de Turing Universal.

Esta MT recibe como entrada una descripción de una Máquina de Turing y
una cadena a procesar.
La MTU determina si la cadena es aceptada por la Máquina de Turing.

------------------------------------------------------------------------------------

Ejemplo de ejecución con la descripción de la máquina que reconoce el leguaje {ww}:

	python run.py Mww.json

------------------------------------------------------------------------------------

Consideraciónes:

	- Una vez ejecutado 'python run.py Mww.json' el programa pedirá la cadena
	  a procesar.
  
	- En los archivos de descipción de la Máquina de Turing, los símbolos
	  deberán estar conformados por arreglos. Esto es porque el simulador
	  acepta varias pistas. Si se desea la máquina corra sobre una pista,
	  el arreglo deberá ser de longitud 1.

	  Ejemplo para una pista:
	
	    ...
	    "Cinta" :[["_"], ["0"], ["*"], ["1"], ...],
	    "Transiciones" :[
	    		   ["q0",  ["0"], "q4",  ["0"], "R"],
		           ["q0",  ["1"], "q4",  ["1"], "R"],
			   ...
			   ]
	     ...
	     
	  Ejemplo para dos pistas:
	
	    ...
	    "Cinta" :[["_", "_"], ["0", "_"], ["1", "_"], ...],
	    "Transiciones" :[
	    		   ["q0",  ["0", "_"], "q4",  ["0", "+"], "R"],
		           ["q0",  ["1", "_"], "q4",  ["1", "+"], "R"],
			   ...
			   ]
	     ...

	- Los archivos JSON con la descripción deben colocarse en la carpeta
	  'descripciones'. Se incluye como ejemplo:
	  
	      - 'M.json' (con una pista), el ejemplo de la práctica.
	      - 'Mww.json' (con 2 pistas), que reconoce el lenguaje {ww}.
	      - 'M0n1n.json' (con 6 pistas), que reconoce el lenguaje {0^n1^n}.
