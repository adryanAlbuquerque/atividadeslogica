"""
Condições   IF - ELIF - ELSE
"""

nome = input("Qual seu nome? ")
idade = int(input("Quantos anos você tem? "))

if idade >= 20 and idade <= 30:
    print(f"{nome} pode fazer emprestimo!")
else:
    print(f"{nome} não pode fazer emprestimo")