def aceptar_o_rechazar_pieza(longitud, diametro):
    densidad = 3.5  # g/cm³
    
    # Verificar la longitud
    if longitud > 7.5 and longitud <= 9:
        # Verificar el diámetro
        if diametro >= 0.5 and diametro <= 1.3:
            # Calcular la masa
            masa = (diametro * longitud) / densidad
            # Verificar la masa
            if masa <= 5.8:
                print("Pieza aceptada")
            else:
                print("Pieza rechazada por exceso de masa")
        else:
            print("Pieza rechazada por diámetro fuera de rango")
    else:
        print("Pieza rechazada por longitud fuera de rango")

# Ejemplo de uso
longitud = float(input("Ingrese la longitud de la pieza (en cm): "))
diametro = float(input("Ingrese el diámetro de la pieza (en cm): "))
aceptar_o_rechazar_pieza(longitud, diametro)
