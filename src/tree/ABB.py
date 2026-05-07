# ##################################################
# Classe cArvoreBinária
# ##################################################

import cNo

# *******************************************************
#
# *******************************************************
class percursos:
  PRE_ORDEM   = 0
  IN_ORDEM    = 1
  POST_ORDEM  = 2
  NIVEL       = 3

# *******************************************************
#
# *******************************************************
class cArvoreBinaria:
  
  chave = 0

# *******************************************************
  def __init__(self):
    self.__raiz   = None  #cabeça da árvore (pai)
    self.__numNos = 0 #quantidade de nós, vetor posição árvore
    
    
# *******************************************************
  def getNumNos(self):
    return self.__numNos  #perguntando quantos nos eu tenho

# *******************************************************
  def getRaiz(self):
    return self.__raiz #obter raiz 

# *******************************************************
  def __getPai(self, no):
      if no == self.__raiz:
        return None
      
      atual = self.__raiz
      while atual is not None:
        if no.getDado() < atual.getDado():
          if atual.getFilhoEsq() == no:
            return atual
          atual = atual.getFilhoEsq()
        else:
          if atual.getFilhoDir() == no:
            return atual
          atual = atual.getFilhoDir()
      
      return None
# *******************************************************

  def percorreArvore(self, percurso=percursos.POST_ORDEM):

    if percurso == percursos.PRE_ORDEM:
      self.__preOrdem(self.__raiz)

    elif percurso == percursos.IN_ORDEM:
      self.__inOrdem(self.__raiz)

    elif percurso == percursos.POST_ORDEM:
      self.__postOrdem(self.__raiz)
 
# *******************************************************
  def inserir(self, n):
    
    novoNo = cNo.cNo(n)

    if self.__raiz == None:
      self.__raiz = novoNo
      self.__numNos += 1
    else: 
      novaArvore = self.__raiz
      while True: 
        arvore = novaArvore
        if n <= novaArvore.getDado():
          novaArvore = novaArvore.getFilhoEsq()
          if novaArvore is None:
            arvore.setFilhoEsq(novoNo)
            self.__numNos +=1 
            return 
        else: 
          novaArvore = novaArvore.getFilhoDir()
          if novaArvore == None: 
            arvore.setFilhoDir(novoNo)
            self.__numNos += 1
            return
       
    
# *******************************************************
  def __preOrdem(self, raiz):
    if raiz != None :
      print(raiz.getDado())

      self.__preOrdem(raiz.getFilhoEsq())
      self.__preOrdem(raiz.getFilhoDir())
# *******************************************************
  def __inOrdem(self, raiz):
    if raiz != None :
      self.__inOrdem(raiz.getFilhoEsq())
      print(raiz.getDado())
      self.__inOrdem(raiz.getFilhoDir())
    
 
# *******************************************************
  def __postOrdem(self, raiz):
    if raiz != None :
      self.__postOrdem(raiz.getFilhoEsq())
      self.__postOrdem(raiz.getFilhoDir())
      print(raiz.getDado())

# *******************************************************
# Consultas em uma árvore de busca binária 

  def buscaDado(self, dado):
    raiz = self.__raiz
    while raiz != None and dado != raiz.getDado(): 
      if dado < raiz.getDado(): 
        raiz = raiz.getFilhoEsq()
      else: 
        raiz = raiz.getFilhoDir()
    
    return raiz 
      
  def minArvore(self, raiz=None):
    if raiz is None:
      raiz = self.__raiz
    while raiz is not None and raiz.getFilhoEsq() is not None:
      raiz = raiz.getFilhoEsq()
    return raiz
  
  
  def maxArvore(self, raiz = None):
    if raiz is None: 
      raiz = self.__raiz
    while raiz is not None and raiz.getFilhoDir() is not None:
      raiz = raiz.getFilhoDir()
    return raiz 

  
  
  def sucessArvore(self, dado):
  # se tem filho direito, o sucessor é o mínimo da subárvore direita
    no = self.buscaDado(dado)
    if no is None: 
      return None
    
    if no.getFilhoDir() is not None:
      return self.minArvore(no.getFilhoDir())
    
    
    # Se não existe filho direito, procura o primeiro ancestral
    # para o qual 'no' está na subárvore esquerda
    pai = None
    atual = self.__raiz
    
    while atual is not None:
      if dado < atual.getDado():
        pai = atual
        atual = atual.getFilhoEsq()
      
      elif dado > atual.getDado():

        atual = atual.getFilhoDir()
      else: 
        break

    return pai

     
  def antecesArvore(self, dado):
    
    no = self.buscaDado(dado)
    
    if no is None:
        return None

    # Se tem filho esquerdo == máximo da subárvore esquerda
    if no.getFilhoEsq() is not None:
        return self.maxArvore(no.getFilhoEsq())

    
    pai = None
    atual = self.__raiz

    while atual is not None:
        if dado > atual.getDado():
            pai = atual        # candidato a antecessor
            atual = atual.getFilhoDir()
        elif dado < atual.getDado():
            atual = atual.getFilhoEsq()
        else:
            break

    return pai
  

# *******************************************************
# ***          Utilizando métodos de remoção          *** 
# *******************************************************
  
  def transplant(self, u, v):
    pai = self.__getPai(u) # sabendo se u é pai ou não
    
    # se u é raiz
    if pai is None:
      self.__raiz = v
    # se u é filho esquerdo do pai
    elif u == pai.getFilhoEsq():
      pai.setFilhoEsq(v)
    # se u é filho direito do pai
    else:
      pai.setFilhoDir(v)


  def eliminar(self, dado):

    no = self.buscaDado(dado)
    
    if no is None:
      return False  # nó não encontrado
    
    # nó não tem filho esquerdo
    if no.getFilhoEsq() is None:
      self.transplant(no, no.getFilhoDir())
      self.__numNos -= 1
      return True
    
    # nó não tem filho direito
    elif no.getFilhoDir() is None:
      self.transplant(no, no.getFilhoEsq())
      self.__numNos -= 1
      return True
    
    # nó tem dois filhos
    else:
      # Encontra o sucessor 
      sucessor = self.minArvore(no.getFilhoDir())
      
      # Se o sucessor não é filho direto de no
      if sucessor != no.getFilhoDir():
        # Substitui sucessor por seu filho direito
        self.transplant(sucessor, sucessor.getFilhoDir())
        # Coloca o filho direito de no em sucessor
        sucessor.setFilhoDir(no.getFilhoDir())
      
      # Substitui no por sucessor
      self.transplant(no, sucessor)
      # Coloca o filho esquerdo de no em sucessor
      sucessor.setFilhoEsq(no.getFilhoEsq())
      self.__numNos -= 1
      return True


# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':  # Arquivo de teste das funções 
    
    arvore = cArvoreBinaria()

    for valor in [10, 5, 15, 3, 12, 1]:
        arvore.inserir(valor)

    print(f"Total de nós: {arvore.getNumNos()}\n")

    no12 = arvore.buscaDado(12)
    print(f"Busca 12: {no12.getDado() if no12 else 'não encontrado'}")

    no100 = arvore.buscaDado(100)
    print(f"Busca 100: {no100.getDado() if no100 else 'não encontrado'}")

    suc5 = arvore.sucessArvore(5)
    print(f"Sucessor de 5: {suc5.getDado() if suc5 else 'nenhum'}")   

    suc12 = arvore.sucessArvore(12)
    print(f"Sucessor de 12: {suc12.getDado() if suc12 else 'nenhum'}") 

    suc15 = arvore.sucessArvore(15)
    print(f"Sucessor de 15: {suc15.getDado() if suc15 else 'nenhum'}") 

    ant15 = arvore.antecesArvore(15)
    print(f"Antecessor de 15: {ant15.getDado() if ant15 else 'nenhum'}")

    ant10 = arvore.antecesArvore(10)
    print(f"Antecessor 10: {ant10.getDado() if ant10 else 'nenhum'}")

    eli15 = arvore.eliminar(15) 
    print(f"Eliminei: {eli15}")

    print(f"\nMínimo: {arvore.minArvore().getDado()}")  
    print(f"Máximo: {arvore.maxArvore().getDado()}")    
    print("\nIn-Ordem antes da remoção:")
    arvore.percorreArvore(percursos.IN_ORDEM)
  
  
    
    print(f"Removendo 1 (sem filho esquerdo)...")
    arvore.eliminar(1)
    print(f"Total de nós: {arvore.getNumNos()}")
    print("In-Ordem:")
    arvore.percorreArvore(percursos.IN_ORDEM)
    
    