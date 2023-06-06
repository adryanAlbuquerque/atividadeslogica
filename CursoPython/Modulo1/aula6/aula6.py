"""
variaveis podem iniciar com letra, ter numeros, separar '_', letra minuscula

"""

nome = 'Adan'
idade = 19
altura = 1.70
e_maior = idade > 18
peso = 75

imc = peso / altura**2

print(f"O indice de massa corporal é: {imc:.2f}")
print('{} tem {} anos, sua altura é {}, e seu peso é {}Kg'.format(nome,idade,altura,peso))