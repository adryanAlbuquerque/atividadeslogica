nome = input("Digite seu nome: ")
qtd_letra = (len(nome))

if qtd_letra <= 4:
    print("Seu nome é muito curto!")

else:
    if qtd_letra >= 5 and qtd_letra <=6:
        print("Seu nome é normal")

    else:
        print("Seu nome é muito grande!")