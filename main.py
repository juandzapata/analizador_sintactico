from Gramatica import Gramatica
from Nodizador import Nodizador
from Produccion import Produccion

def __main__():
    print("¡Estructuras de lenguajes!")

    gramatica = Gramatica(["a", "b"], ["S","A", "B"], [
                          Produccion("S", ["aB", "bA"]), Produccion("A", ["a", "aS", "bAA"]), Produccion("B", ["b", "bS", "aBB"])], "S")

    gramatica.determinarRecursion()
    gramatica.mostrarProducciones()
    nodizador = Nodizador(gramatica)
    nodizador.crearArbol()
    nodizador.mostrarArbol()

    palabra = "ab"

if __name__ == "__main__":
    __main__()
