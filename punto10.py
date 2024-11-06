calificacion1 = float(input("Ingrese la calificación 1: "))  
calificacion2 = float(input("Ingrese la calificación 2: "))  
calificacion3 = float(input("Ingrese la calificación 3: "))  


if calificacion1 <= calificacion2 and calificacion1 <= calificacion3:  
    promedio = (calificacion2 + calificacion3) / 2  
elif calificacion2 <= calificacion1 and calificacion2 <= calificacion3:  
    promedio = (calificacion1 + calificacion3) / 2  
else:  
    promedio = (calificacion1 + calificacion2) / 2  


print("La calificación final es:", promedio)  