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
  def __init__(self, n):
    self.__raiz   = None #cabeça da árvore (pai)
    self.__numNos = 0 #quantidade de nós, vetor posição árvore
    self.__raiz   = self.__MontaAB(n)

# *******************************************************
  def getNumNos(self):
    return self.__numNos

# *******************************************************
  def percorreArvore(self, percurso=percursos.PRE_ORDEM):

    if percurso == percursos.PRE_ORDEM:
      self.__preOrdem(self.__raiz)

    elif percurso == percursos.IN_ORDEM:
      self.__inOrdem(self.__raiz)

    elif percurso == percursos.POST_ORDEM:
      self.__postOrdem(self.__raiz)
 
# *******************************************************
  def __MontaAB(self, n):
    
    if n <= 0: 
      return None
    
    novoNo = cNo.cNo(cArvoreBinaria.chave)
    cArvoreBinaria.chave += 1

    numDir = (n-1)//2
    numEsq = (n - 1) - numDir 

    novoNo.setFilhoEsq(self.__MontaAB(numEsq))
    novoNo.setFilhoDir(self.__MontaAB(numDir))
    
    return novoNo
    
# *******************************************************
  def __preOrdem(self, raiz):
    if raiz != None :
      print(raiz.getDado())

      self.__preOrdem(raiz.getFilhoEsq())
      self.__preOrdem(raiz.getFilhoDir())
# *******************************************************
  def __inOrdem(self, raiz):
    if raiz != None :
      self.__preOrdem(raiz.getFilhoEsq())
      print(raiz.getDado())
      self.__preOrdem(raiz.getFilhoDir())
    
 
# *******************************************************
  def __postOrdem(self, raiz):
    if raiz != None :
      self.__preOrdem(raiz.getFilhoEsq())
      self.__preOrdem(raiz.getFilhoDir())
      print(raiz.getDado())

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

  arvore = cArvoreBinaria(20)

  print("chave = ", arvore.chave)

  print("Percurso em Pré-Ordem:")
  print("======================")
  arvore.percorreArvore(percursos.PRE_ORDEM)
  print("======================")

  print("Percurso em In-Ordem:")
  print("======================")
  arvore.percorreArvore(percursos.IN_ORDEM)
  print("======================")

  print("Percurso em Post-Ordem:")
  print("======================")
  arvore.percorreArvore(percursos.POST_ORDEM)
  print("======================")
