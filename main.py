import math

class Ponto:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def adicionar_pontos(self, x, y):
        self.__x = x
        self.__y = y
         
    def remover_pontos(self):
        self.__x = None
        self.__y = None
    
    def calcular_distancia(self, Ponto1, Ponto2):
        distancia = math.sqrt((Ponto2.__x - Ponto1.__x)**2 + (Ponto2.__y - Ponto1.__y)**2)
        return distancia

Ponto1 = Ponto(0, 0)  # Inicializa o Ponto1 em (0, 0)
Ponto2 = Ponto(0, 0)  # Inicializa o Ponto2 em (0, 0)

continuar = True
while continuar:
    escolha = int(input("O que deseja fazer: 1- adicionar pontos, 2- remover pontos, 3- calcular distância, 4- sair: "))

    if escolha == 1:
        ponto = int(input("Qual dos pontos deseja adicionar: 1 ou 2? "))
        if ponto == 1:
            x = int(input("Digite x do ponto: "))
            y = int(input("Digite y do ponto: "))
            Ponto1.adicionar_pontos(x, y)
        elif ponto == 2:
            x = int(input("Digite x do ponto: "))
            y = int(input("Digite y do ponto: "))
            Ponto2.adicionar_pontos(x, y)
    elif escolha == 2:
        ponto = int(input("Qual dos pontos deseja remover: 1 ou 2 "))
        if ponto == 1:
            Ponto1.remover_pontos()
        elif ponto == 2:
            Ponto2.remover_pontos()
    elif escolha == 3:
        distancia = Ponto1.calcular_distancia(Ponto2)
        print("Distância entre os pontos:", distancia)
    elif escolha == 4:
        continuar = False
    else:
        print("Opção inválida. Por favor, escolha novamente.")
