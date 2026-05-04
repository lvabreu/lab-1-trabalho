class Node: 
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.proximo = None

class lista: 
    def __init__(self):
        self.cabeca = Node(None)
        
    
    def busca(self, x):
        vaga = self.cabeca.proximo
        while vaga is not None and vaga.arquivo != x:
            vaga = vaga.proximo
        return vaga

    
    def inserir(self, x, y): #busco o elemento x e insiro um y uma nova celula contendo y apos x
        novo = Node(y)
        vagaOcupada = self.busca(x)
        if vagaOcupada is None:
            vagaOcupada = self.cabeca 
        novo.proximo = vagaOcupada.proximo
        vagaOcupada.proximo = novo

    
    def remover(self,x): #o x 
        # Lista vazia
        if self.cabeca is None:
            return False

        atual = self.cabeca
        anterior = None

        # percorrer
        while atual and atual.arquivo != x:
            anterior = atual
            atual = atual.proximo

        # Não achou
        if atual is None:
            return False

        # Achou no primeiro nó
        if anterior is None:
            self.cabeca = atual.proximo
            del atual
            return True

        # Achou no meio ou fim
        anterior.proximo = atual.proximo
        del atual
        return True