from min_heap import HeapBinaria
from max_heap import MaxHeapBinaria

if __name__ == "__main__":

    valores = [10, 5, 20, 3, 8, 15]

    print("====== MIN HEAP ======")
    min_heap = HeapBinaria()

    for v in valores:
        min_heap.inserir(v)
        min_heap.imprimir()

    print("\nExtraindo (crescente):")
    while True:
        val = min_heap.extrair_min()
        if val is None:
            break
        print(val)
        min_heap.imprimir()

    print("\n====== MAX HEAP ======")
    max_heap = MaxHeapBinaria()

    for v in valores:
        max_heap.inserir(v)
        max_heap.imprimir()

    print("\nExtraindo (decrescente):")
    while True:
        val = max_heap.extrair_max()
        if val is None:
            break
        print(val)
        max_heap.imprimir()