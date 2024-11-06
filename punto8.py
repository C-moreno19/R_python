# imprimir el número medio de un conjunto de tres números únicos. El número medio es aquel que no es el menor ni el mayor.
Num1 = float(input("Ingrese el primer número: "))  
Num2 = float(input("Ingrese el segundo número: "))  
Num3 = float(input("Ingrese el tercer número: "))  


if Num1 > Num2:  
    if Num1 < Num3:  
        medio = Num1  
    elif Num2 > Num3:  
        medio = Num2  
    else:  
        medio = Num3  
else: 
    if Num2 < Num3:  
        medio = Num2  
    elif Num1 > Num3:  
        medio = Num1  
    else:  
        medio = Num3  

 
print(f"El número medio es: {medio:,.0f}")  
