from AnalizadorSintactico import AnalizadorSintactico
from Gramatica import Gramatica
from Produccion import Produccion

def __main__():
    print("¡Estructuras de lenguajes!")

    gramatica = Gramatica(["a", "b"], ["A", "B", "S"], [
                          Produccion("S", ["aB", "bA"]), Produccion("A", ["a", "aS", "bAA"]), Produccion("B", ["b", "bS", "aBB"])], "S")

    gramatica.determinarRecursion()
    gramatica.mostrarProducciones()
    analizador = AnalizadorSintactico(gramatica)

    palabra = "ab"
    if analizador.analizar(palabra):
        print(f'La palabra "{palabra}" pertenece a la gramática.')
        # Mostrar árbol de derivación
        print("Árbol de derivación:")
        print(analizador.arbol_derivacion.imprimir_arbol())
    else:
        print(f'La palabra "{palabra}" no pertenece a la gramática.')

if __name__ == "__main__":
    __main__()
