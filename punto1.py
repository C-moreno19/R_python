#imprimir un numero negativo junto con su positivo
  
numero = float(input("Ingrese un número: "))  

  
if numero < 0:  
      
    print("El número negativo es:",numero)
    print("Su equivalente positivo es: ",abs(numero))    
   
else:  
    # Indicar que el número no es negativo  
    print("El número ingresado no es negativo.")  