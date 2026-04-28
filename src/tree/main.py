import cNo
import biTree

import sys

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

  n = 20
  if (len(sys.argv) > 1):
      n = int(sys.argv[1])
      if n < 0:
          n = 20

  arvore = biTree.cArvoreBinaria(n)

  print("Percurso em Pré-Ordem:")
  print("======================")
  arvore.percorreArvore(biTree.percursos.PRE_ORDEM)
  print("======================")

  print("Percurso em In-Ordem:")
  print("======================")
  arvore.percorreArvore(biTree.percursos.IN_ORDEM)
  print("======================")

  print("Percurso em Post-Ordem:")
  print("======================")
  arvore.percorreArvore(biTree.percursos.POST_ORDEM)
  print("======================")