import cNo

#--------------------------------------------------------#
####### Balanceamento de Árvore Binárias de Busca #######
#-------------------------------------------------------#

class percurso:
    PRE_ORDEM  = 0
    IN_ORDEM   = 1
    POST_ORDEM = 2


class AVL:
    def __init__(self):
        self.__raiz   = None
        self.__numNos = 0

    def getNumNos(self):
        return self.__numNos

    def getRaiz(self):
        return self.__raiz

    def __obterAltura(self, no):
        if no is None:
            return 0
        return no.getAltura()

    def __obterFatorBalanceamento(self, no):
        if no is None:
            return 0
        return self.__obterAltura(no.getFilhoEsq()) - self.__obterAltura(no.getFilhoDir())

    def __atualizarAltura(self, no):
        if no is None:
            return
        no.setAltura(1 + max(self.__obterAltura(no.getFilhoEsq()),
                             self.__obterAltura(no.getFilhoDir())))

    def __rotacaoEsquerda(self, no):
        novoRaiz = no.getFilhoDir()
        no.setFilhoDir(novoRaiz.getFilhoEsq())
        novoRaiz.setFilhoEsq(no)
        self.__atualizarAltura(no)
        self.__atualizarAltura(novoRaiz)
        return novoRaiz

    def __rotacaoDireita(self, no):
        novoRaiz = no.getFilhoEsq()
        no.setFilhoEsq(novoRaiz.getFilhoDir())
        novoRaiz.setFilhoDir(no)
        self.__atualizarAltura(no)
        self.__atualizarAltura(novoRaiz)
        return novoRaiz

    def inserir(self, dado):
        self.__raiz = self.__inserirRec(self.__raiz, dado)

    def __inserirRec(self, no, dado):
        if no is None:
            self.__numNos += 1
            return cNo.cNo(dado)

        if dado <= no.getDado():
            no.setFilhoEsq(self.__inserirRec(no.getFilhoEsq(), dado))
        else:
            no.setFilhoDir(self.__inserirRec(no.getFilhoDir(), dado))

        self.__atualizarAltura(no)
        fator = self.__obterFatorBalanceamento(no)

        if fator > 1:
            if self.__obterFatorBalanceamento(no.getFilhoEsq()) < 0:
                no.setFilhoEsq(self.__rotacaoEsquerda(no.getFilhoEsq()))
            return self.__rotacaoDireita(no)

        if fator < -1:
            if self.__obterFatorBalanceamento(no.getFilhoDir()) > 0:
                no.setFilhoDir(self.__rotacaoDireita(no.getFilhoDir()))
            return self.__rotacaoEsquerda(no)

        return no

    def buscar(self, dado):
        return self.__buscarRec(self.__raiz, dado)

    def __buscarRec(self, no, dado):
        if no is None:
            return None
        if dado == no.getDado():
            return no
        elif dado < no.getDado():
            return self.__buscarRec(no.getFilhoEsq(), dado)
        else:
            return self.__buscarRec(no.getFilhoDir(), dado)

    def percorreArvore(self, tipo=percurso.IN_ORDEM):
        if tipo == percurso.PRE_ORDEM:
            self.__preOrdem(self.__raiz)
        elif tipo == percurso.IN_ORDEM:
            self.__inOrdem(self.__raiz)
        elif tipo == percurso.POST_ORDEM:
            self.__postOrdem(self.__raiz)

    def __preOrdem(self, no):
        if no is not None:
            print(no.getDado(), end=' ')
            self.__preOrdem(no.getFilhoEsq())
            self.__preOrdem(no.getFilhoDir())

    def __inOrdem(self, no):
        if no is not None:
            self.__inOrdem(no.getFilhoEsq())
            print(no.getDado(), end=' ')
            self.__inOrdem(no.getFilhoDir())

    def __postOrdem(self, no):
        if no is not None:
            self.__postOrdem(no.getFilhoEsq())
            self.__postOrdem(no.getFilhoDir())
            print(no.getDado(), end=' ')


if __name__ == '__main__':
    avl = AVL()

    valores = [1, 2, 3, 4, 5, 6, 7, 10, 9, 8]
    print("Inserindo:", valores)
    for v in valores:
        avl.inserir(v)

    print(f"\nTotal de nós : {avl.getNumNos()}")
    print(f"Altura da raiz: {avl.getRaiz().getAltura()}")

    print("\n-- Percursos --")
    print("In-Ordem   :", end=' '); avl.percorreArvore(percurso.IN_ORDEM);   print()
    print("Pré-Ordem  :", end=' '); avl.percorreArvore(percurso.PRE_ORDEM);  print()
    print("Pós-Ordem  :", end=' '); avl.percorreArvore(percurso.POST_ORDEM); print()

    print("\n-- Buscas --")
    for alvo in [5, 8, 100]:
        resultado = avl.buscar(alvo)
        print(f"  buscar({alvo:>3}): {'encontrado' if resultado else 'não encontrado'}")