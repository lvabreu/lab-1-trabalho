from lista import lista

def separador(titulo):
    print(f"\n{'='*40}")
    print(f"  {titulo}")
    print(f"{'='*40}")


def exibir(lst):
    atual = lst.cabeca.proximo
    if atual is None:
        print("  [lista vazia]")
        return
    while atual is not None:
        print(f"  {atual.arquivo}", end=" ->")
        atual = atual.proximo
    print(" None")


if __name__ == '__main__':

    lst = lista()

    separador("Inserção")
    lst.inserir(None, 10)
    lst.inserir(None, 20)
    lst.inserir(None, 30)
    lst.inserir(20, 25)   # insere 25 após o 20
    lst.inserir(99, 99)   # x não existe, insere no início
    exibir(lst)

    separador("Busca")
    for alvo in [25, 30, 99, 100]:
        resultado = lst.busca(alvo)
        print(f"  busca({alvo}): {'encontrado' if resultado else 'não encontrado'}")

    separador("Remoção")
    for alvo in [10, 25, 99, 100]:
        ok = lst.remover(alvo)
        print(f"  remover({alvo}): {'removido' if ok else 'não encontrado'}")
        exibir(lst)

    separador("Remoção em lista vazia")
    lst2 = lista()
    print(f"  remover(5): {'removido' if lst2.remover(5) else 'não encontrado'}")