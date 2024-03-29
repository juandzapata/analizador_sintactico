from Gramatica import Gramatica
from Nodo import Nodo


class AnalizadorSintactico():
    def __init__(self, gramatica: Gramatica):
        self.gramatica = gramatica

    def analizar(self, palabra: str) -> bool:
        self.palabra = palabra
        self.posicion = 0
        self.arbol_derivacion = self.analizar_no_terminal(self.gramatica.inicial)
        return self.arbol_derivacion is not None and self.posicion == len(palabra)

    def analizar_no_terminal(self, no_terminal: str) -> Nodo:
        nodo = Nodo(no_terminal)
        producciones = self.gramatica.obtener_producciones(no_terminal)
        for produccion in producciones:
            for valor in produccion.valores:
                if self.analizar_valor(valor, nodo):
                    return nodo
        return None

    def analizar_valor(self, valor: str, nodo_padre: Nodo) -> bool:
        nodo = Nodo(valor)
        nodo_padre.agregarHijo(nodo)

        if valor == 'λ':
            return True

        for simbolo in valor:
            if self.posicion >= len(self.palabra):
                return False
            if self.gramatica.es_terminal(simbolo):
                if self.palabra[self.posicion] != simbolo:
                    return False
                self.posicion += 1
            elif self.gramatica.es_no_terminal(simbolo):
                if self.analizar_no_terminal(simbolo) is None:
                    return False
            else:
                return False

        return True