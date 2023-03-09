palavra = str(input("Escreva uma palavra: "))
palavra = palavra.upper()
linha = ""

for l in palavra:
    if str(l) == "A":
        continue
    elif str(l) == "E":
        continue
    elif str(l) == "I":
        continue
    elif str(l) == "O":
        continue
    elif str(l) == "U":
        continue
    else:
        linha += l
print(linha)