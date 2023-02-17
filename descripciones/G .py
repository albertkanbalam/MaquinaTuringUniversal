descripcionG={
    "Estados": ["q0", "qA", "qB", "qC"],
    "Entrada": [ "a", "b" ],
    "Cinta": [ ["a"] , ["b"], ["_"], ["X"]],
    "Inicial": "q0",
    "Blanco": "_",
    "Finales": ["qf"],
    "Transiciones": [
	["q0", ["_"] ,"q0", ["a"] ,"R"],
	["q0", ["_"] ,"q0", ["b"] ,"R"]
    ]
}
