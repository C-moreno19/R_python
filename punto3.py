sueldo = int(input("Ingrese su sueldo actual: "));

if (sueldo < 300000):
    nuevo_sueldo = sueldo + (sueldo * 0.15);
    print("Usted recibio un aumento 15% ");
    print(f"Su sueldo es de: {nuevo_sueldo}");
elif (sueldo > 300000):
    print("Su sueldo es mayor a 300000 por lo tanto no tiene aumento ");
