class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos: list[Nodo] = []

    def agregarHijo(self, hijo):
        self.hijos.append(hijo)
    
    def __str__(self):
        return str(self.valor)
    
    def imprimir_arbol(self, nivel=0):
        salida = "  " * nivel + str(self.valor) + "\n"
        for hijo in self.hijos:
            salida += hijo.imprimir_arbol(nivel + 1)
        return salida