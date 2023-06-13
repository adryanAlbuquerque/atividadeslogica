senha = input("Digite sua senha: ")
qtd_caracter = len(senha)

if qtd_caracter >= 6:
    print("Usuário cadastrado!")
else:
    print("Por favor, digite uma senha com mais de 6 caracteres!")

str1 = input("digite uma coisa: ")
str2 = input("digite outra coisa: ")

print(f"A quantidade de letras é igual a {len(str1) + len(str2)}")