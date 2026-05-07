import random
import time
import sys
from ABB import cArvoreBinaria
from AVL import AVL

sys.setrecursionlimit(20000)


def testar(quantidade):
    print(f"\n{'='*50}")
    print(f"  Teste com {quantidade:,} nós")
    print(f"{'='*50}")

    valores = random.sample(range(quantidade * 10), quantidade)
    buscas  = random.sample(valores, 5) + [quantidade * 10 + 1]

    # ABB
    print("\n  [ABB]")
    abb = cArvoreBinaria()

    inicio = time.perf_counter()
    for v in valores:
        abb.inserir(v)
    fim = time.perf_counter()

    print(f"  Tempo de inserção : {fim - inicio:.4f}s")
    print(f"  Total de nós      : {abb.getNumNos():,}")

    print("  -- Buscas --")
    for alvo in buscas:
        inicio = time.perf_counter()
        resultado = abb.buscaDado(alvo)
        fim = time.perf_counter()
        status = "encontrado" if resultado else "não encontrado"
        print(f"    buscar({alvo:>8}): {status:<15} ({(fim - inicio) * 1_000_000:.2f} µs)")

    # AVL
    print("\n  [AVL]")
    avl = AVL()

    inicio = time.perf_counter()
    for v in valores:
        avl.inserir(v)
    fim = time.perf_counter()

    print(f"  Tempo de inserção : {fim - inicio:.4f}s")
    print(f"  Total de nós      : {avl.getNumNos():,}")
    print(f"  Altura da raiz    : {avl.getRaiz().getAltura()}")

    print("  -- Buscas --")
    for alvo in buscas:
        inicio = time.perf_counter()
        resultado = avl.buscar(alvo)
        fim = time.perf_counter()
        status = "encontrado" if resultado else "não encontrado"
        print(f"    buscar({alvo:>8}): {status:<15} ({(fim - inicio) * 1_000_000:.2f} µs)")


if __name__ == '__main__':
    testar(1_000)
    testar(10_000)