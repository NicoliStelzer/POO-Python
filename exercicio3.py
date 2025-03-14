class Pessoas:
    def __init__(self, nome, telefone, idade):
        self.nome = nome
        self.telefone = telefone
        self.idade = idade

class ListaSequencial:
    def __init__(self, capacidade):
        self.capacidade = capacidade 
        self.tamanho = 0  
        self.elementos = [None]*capacidade  

    def inserir(self, elemento):
        if self.tamanho < self.capacidade:
            self.elementos[self.tamanho] = elemento
            self.tamanho += 1
    
    def remover(self, index):
        if index < 0 or (index >= self.tamanho - 1):
            print("Erro: Índice fora dos limites válidos da lista.")
            return  
        for i in range(index, self.tamanho - 1):
            self.elementos[i] = self.elementos[i + 1]
        self.elementos[self.tamanho - 1] = None
        self.tamanho -= 1
    
    def imprimir(self):
        elementos = [str(self.elementos[i]) for i in range(self.tamanho)]
        lista_formatada = "[" + ", ".join(elementos) + "]"
        print(lista_formatada)

    def inserir_em(self, index, pessoa):
        if self.tamanho >= self.capacidade:
            print("erro: a lista esta cheia")
            return
        if index < 0 or index > self.tamanho:
            print("erro: indice fora do intervalo")
            return
        i = self.tamanho
        while i > index:
            self.elementos[i] = self.elementos[i - 1]
            i -= 1
        self.elementos[index] = pessoa
        self.tamanho += 1

lista = ListaSequencial(7)

lista.inserir(Pessoas("Alice", "483773940", "18"))
lista.inserir(Pessoas("Joao", "003826253", "20"))
lista.inserir(Pessoas("tiago", "00234266", "24"))
lista.inserir(Pessoas("Joao", "034203823", "26"))
lista.inserir(Pessoas("Joao", "062533423", "22"))
lista.remover(2)
lista.imprimir()