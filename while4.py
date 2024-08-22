n=input("ingrese un numero para sumar sus digitos:")#"23"
lista=list(n)
suma=0
for digito in lista:
    suma=suma+int(digito)
print(suma)    
