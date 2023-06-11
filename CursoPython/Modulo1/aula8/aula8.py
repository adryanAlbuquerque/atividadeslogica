"""
Condições   IF - ELIF - ELSE
"""

nome = input("Qual seu nome? ")
idade = int(input("Quantos anos você tem? "))

quant_letras = len(nome)

if idade >= 20 and idade <= 30:
    print(f"{nome} pode fazer emprestimo!")
else:
    print(f"{nome} não está liberado pra fazer emprestimo")

if len(nome) > 0:
    print(f'{nome} tem {quant_letras}  letras')