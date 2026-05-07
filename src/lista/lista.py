import cNo 
class lista:
    def __init__(self):
        self.cabeca = cNo.Node(None)  # nó sentinela

    def busca(self, x):
        vaga = self.cabeca.proximo
        while vaga is not None and vaga.arquivo != x:
            vaga = vaga.proximo
        return vaga

    def inserir(self, x, y):
        novo = cNo.Node(y)
        vagaOcupada = self.busca(x)
        if vagaOcupada is None:
            vagaOcupada = self.cabeca
        novo.proximo = vagaOcupada.proximo
        vagaOcupada.proximo = novo

    def remover(self, x):
        anterior = self.cabeca
        atual = self.cabeca.proximo

        while atual is not None and atual.arquivo != x:
            anterior = atual
            atual = atual.proximo

        if atual is None:
            return False

        anterior.proximo = atual.proximo
        return True
