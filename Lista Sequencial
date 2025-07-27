class ListaSequencial:
    __slots__ = ('dados', 'tamanho', 'capacidade')
    def __init__(lista, capacidade):
        lista.dados = [None] * capacidade
        lista.tamanho = 0
        lista.capacidade = capacidade
    def __len__(lista):
        return lista.tamanho
    def __bool__(lista):
        return lista.tamanho > 0
    def __getitem__(lista, indice):
        if not 0 <= indice < lista.tamanho: raise IndexError
        return lista.dados[indice]
    def __setitem__(lista, indice, valor):
        if not 0 <= indice < lista.tamanho: raise IndexError
        lista.dados[indice] = valor
    def inserir(lista, indice, valor):
        if lista.tamanho == lista.capacidade: raise OverflowError
        if not 0 <= indice <= lista.tamanho: raise IndexError
        lista.dados[indice+1:lista.tamanho+1] = lista.dados[indice:lista.tamanho]
        lista.dados[indice] = valor
        lista.tamanho += 1
    def remover(lista, indice=-1):
        if lista.tamanho == 0: raise IndexError
        indice = lista.tamanho - 1 if indice < 0 else indice
        if not 0 <= indice < lista.tamanho: raise IndexError
        valor = lista.dados[indice]
        lista.dados[indice:lista.tamanho-1] = lista.dados[indice+1:lista.tamanho]
        lista.tamanho -= 1
        return valor
