"""
Crie uma função que responda à pergunta "Você está tocando banjo?".
Se seu nome começa com a letra "R" ou "r" minúsculo, você está tocando banjo!

A função recebe um nome como seu único argumento e retorna uma das seguintes strings:

name + " plays banjo"
name + " does not play banjo"
Os nomes fornecidos são sempre strings válidas.
"""
def are_you_playing_banjo(name):
    first_letter = name[:1]
    if first_letter == "R" or first_letter == "r":
        print(name + " plays banjo")
        return name + " plays banjo"
    else:
        print(name + " does not play banjo")
        return name + " does not play banjo"


are_you_playing_banjo("martin")
