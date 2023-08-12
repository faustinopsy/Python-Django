""" Classe que implementa o algoritmo de ordenaçao QuickSort"""
class QuickSort:

    def __init__(self, numeros:'Lista de numeros')->None:
        self.__numeros = numeros
        self.__ordena()
        
    def __ordena(self)->None:
        self.__particiona(self.__numeros, 0, len(self.__numeros) - 1)
 
    def __particiona(self, numeros:'Lista de numeros', inicio: int, fim:int)->None:
        if fim - inicio > 0:
            pivo, esquerda, direita = self.__numeros[inicio], inicio, fim
            while esquerda <= direita:
                while self.__numeros[esquerda] < pivo:
                    esquerda += 1
                while self.__numeros[direita] > pivo:
                    direita -= 1
                if esquerda <= direita:
                    self.__numeros[esquerda], self.__numeros[direita] = self.__numeros[direita], self.__numeros[esquerda]
                    esquerda += 1
                    direita -= 1
            self.__particiona(self.__numeros, inicio, direita)
            self.__particiona(self.__numeros, esquerda, fim)

    @property
    def resultado(self)->'Lista de numeros':
        return self.__numeros
