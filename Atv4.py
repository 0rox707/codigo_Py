lista =[]
j=True
while j:

    i=True
    while i:
        nu =int(input("digite um numero:"))
        if type(nu) == int:
            i =False
            lista.append(nu)
        else:
            print("digite um numero inteiro!!!")

    r =str(input("- - - - - - - - - - - -\nQuer adicionar outro numero: \ns/n: "))
    if r == "N" or r == "n":
        j=False
# ------------ receber numero e adicionar na lista -----------




print(lista) 