figuraGeometrica=int(input("ingrese la cantidad de lados de las figura"))
if figuraGeometrica==4:
l1=int(input("ingrese el valor del primer lado:"))
l2=int(input("ingrese el valor del segundo lado:"))
l3=int(input("ingrese el valor del tercer  lado:"))
l4=int(input("ingrese el valor del cuarto lado:"))

if l1==l2 and l1==l3 and l1==l4:
    print("la figura podrá ser un cuadrado o un rombo")
elif l1!=l2 or l1!=3 or l1!=4:
    print("la figura podrá ser un rectangulo trapezoide escaleno")
elif l1==l3 and l3==l4:
    print ("la figura ingresada es un rectangulo o paralelogramo")
