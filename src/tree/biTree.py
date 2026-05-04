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
    
    return raiz is not None
      
  def minArvore(self,):
    raiz = self.__raiz
    while raiz is not None and raiz.getFilhoEsq() is not None:
      raiz = raiz.getFilhoEsq()
    return raiz
  
  def maxArvore(self):
    raiz = self.__raiz
    while raiz is not None and raiz.getFilhoDir() is not None:
      raiz = raiz.getFilhoDir()
    return raiz 
  
  def sucesArvore(self):
    raiz = self.__raiz
    if raiz.getFilhoDir() is not None and self.percorreArvore(percurso=percursos.IN_ORDEM):
      return self.minArvore()

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':
  
  
  arvore = cArvoreBinaria()

  print("Inserindo valores:")
  for valor in [10, 5, 15, 3, 12, 1]:
    arvore.inserir(valor)
  
  print(f"Total de nós: {arvore.getNumNos()}\n")

  # Testando busca
  print("Testando buscas:")
  print(f"Busca 7: {arvore.buscaDado(7)}")
  print(f"Busca 12: {arvore.buscaDado(12)}")
  print(f"Busca 100: {arvore.buscaDado(100)}\n")
  print(f"Busca mínimo: {arvore.minArvore().getDado()}\n")
  print(f"Busca máximo: {arvore.maxArvore().getDado()}\n") 

  # Percursos
  print("Percurso em In-Ordem (valores em ordem ):")
  arvore.percorreArvore(percursos.PRE_ORDEM)
