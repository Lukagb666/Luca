numerosEnteros=[]
while True:#se con la función break()
       numero=int(input("ingrese un numero entero:"))
       numerosEnteros.append(numero)
       if numero==0:
              break 
print(numerosEnteros)       
print("El valor mayor es: ")       
print(max(numerosEnteros))       