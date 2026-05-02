from cNo import cNo

class HeapBinaria:

    def __init__(self):
        self.__raiz = None
        self.__nos = []

    def inserir(self, valor):
        novo = cNo(valor)
        self.__nos.append(novo)

        if len(self.__nos) == 1:
            self.__raiz = novo
            return

        pai_index = (len(self.__nos) - 2) // 2
        pai = self.__nos[pai_index]

        if pai.getFilhoEsq() is None:
            pai.setFilhoEsq(novo)
        else:
            pai.setFilhoDir(novo)

        self.__heapify_up(len(self.__nos) - 1)

    def __heapify_up(self, i):
        while i > 0:
            pai = (i - 1) // 2

            if self.__nos[pai].getDado() > self.__nos[i].getDado():
                self.__nos[pai].setDado(self.__nos[i].getDado()), self.__nos[i].setDado(self.__nos[pai].getDado())
                temp = self.__nos[pai].getDado()
                self.__nos[pai].setDado(self.__nos[i].getDado())
                self.__nos[i].setDado(temp)
                i = pai
            else:
                break

    def extrair_min(self):
        if not self.__nos:
            return None

        raiz = self.__nos[0].getDado()
        ultimo = self.__nos.pop()

        if len(self.__nos) == 0:
            return raiz

        self.__nos[0].setDado(ultimo.getDado())
        self.__heapify_down(0)

        return raiz

    def __heapify_down(self, i):
        n = len(self.__nos)

        while True:
            menor = i
            esq = 2*i + 1
            dir = 2*i + 2

            if esq < n and self.__nos[esq].getDado() < self.__nos[menor].getDado():
                menor = esq

            if dir < n and self.__nos[dir].getDado() < self.__nos[menor].getDado():
                menor = dir

            if menor != i:
                temp = self.__nos[i].getDado()
                self.__nos[i].setDado(self.__nos[menor].getDado())
                self.__nos[menor].setDado(temp)
                i = menor
            else:
                break

    def imprimir(self):
        print([no.getDado() for no in self.__nos])