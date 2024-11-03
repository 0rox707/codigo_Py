# ------------ receber numero e adicionar na lista -----------
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

    r =str(input("Quer adicionar outro numero: \ns/n: "))
    if r == "N" or r == "n":
        j=False
print(lista)


# Dada uma lista de números inteiros fornecida pelo usuário, escreva um programa 
# que calcule e exiba a média dos valores que estão em índices ímpares. Imprima 
# cada valor encontrado e, ao final, a média desses valores. 
# Se não houver valores em índices ímpares, exiba uma mensagem adequada.


media =0 
h = 0
c=0
print("media de |", end="")
while True:
    
    if h%2 == 0:
        print(lista[h],end=" ")
        media+=lista[h]
        c+=1
        
    h+=1
    
    if h >= len(lista):
        media=(media/c)
        print("| e ",media)
        break
    
