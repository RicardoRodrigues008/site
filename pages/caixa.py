saldo= int (input("quanto vai ser guardado?"))
tempo= int(input("quanto tempo?"))
taxa=5/100
juros=round(saldo*(1+taxa)**tempo)-saldo
montante=saldo+juros
print("seu dinheiro rendeu "+str(juros)+" Reais ")
print("saldo atual "+str(montante)+" Reais ")