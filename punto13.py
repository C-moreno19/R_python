def calcular_nota_total():
    # Leer las notas de las diferentes evaluaciones
    nota_examen = float(input("Ingrese la nota del examen: "))
    nota_tareas = float(input("Ingrese la nota de las tareas: "))
    nota_practicas = float(input("Ingrese la nota de las prácticas: "))
    
    # Calcular la nota total
    nota_total = nota_examen + nota_tareas + nota_practicas
    
    # Determinar si aprobó o reprobó
    if nota_total >= 60:
        print("Felicitaciones, usted aprobo.")
    else:
        print("Lo siento, usted ha sido reprobado.")

# Llamada a la función para ejecutar el programa
calcular_nota_total()
