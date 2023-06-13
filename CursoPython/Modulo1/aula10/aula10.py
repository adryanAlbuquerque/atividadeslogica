senha = input("Digite sua senha: ")
qtd_caracter = len(senha)

if qtd_caracter >= 6:
    print("Usuário cadastrado!")
else:
    print("Por favor, digite uma senha com mais de 6 caracteres!")