numeroSecreto = 21
tentativa  = 1

while tentativa <=3:
    palpite = int(input("Adivinhe o número secreto: "))
    if palpite == numeroSecreto:
        print("Parabéns, você acertou!")
        break
    else:
        if palpite < numeroSecreto:
            print("O número secreto é maior do que",palpite)
        else:
            print("O número secreto é menor do que",palpite)
    tentativa +=1
if tentativa > 3:
    print("Acabaram as sua chances, vai morrer de curiosidade agora HAHAHA!")
    
        