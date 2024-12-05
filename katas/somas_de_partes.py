"""
Vamos considerar este exemplo (matriz escrita em formato geral):

ls = [0, 1, 3, 6, 10]

Suas seguintes partes:

ls = [0, 1, 3, 6, 10]
ls = [1, 3, 6, 10]
ls = [3, 6, 10]
ls = [6, 10]
ls = [10]
ls = []
As somas correspondentes são (colocadas juntas em uma lista): [20, 20, 19, 16, 10, 0]

A função parts_sums(ou suas variantes em outras linguagens) receberá como parâmetro uma lista ls e retornará uma lista das somas de suas partes, conforme definido acima.

Outros exemplos:
ls = [1, 2, 3, 4, 5, 6]
parts_sums(ls) -> [21, 20, 18, 15, 11, 6, 0]

ls = [744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]
parts_sums(ls) -> [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0]
Notas
Dê uma olhada no desempenho: algumas listas têm milhares de elementos.
Por favor, pergunte antes de traduzir.
"""

#ls = [1, 2, 3, 4, 5, 6]
ls = [744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]


def parts_sums(ls):
    soma_total = sum(ls)
    resultado = [soma_total]
    for numero in ls:
        soma_total -= numero
        resultado.append(soma_total)
    return resultado


print(parts_sums(ls))
