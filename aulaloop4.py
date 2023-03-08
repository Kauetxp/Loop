tentativas = 1

while tentativas <=3:
    senha = "poipoi123"
    tentasenha = str(input("Digite a senha: "))
    
    if tentasenha == senha:
        print("Acesso concedido!")
        break
    else:
        print("Senha incorreta, tente novamente.")
        tentativas+=1
else:
    print("Núméro de tentativas excedido!")
    