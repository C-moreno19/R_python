def verificar_divisibilidad(a, b, c):
    # Verificar si uno es divisible por otro
    if a % b == 0:
        print(f"{a} es divisible por {b}")
    if a % c == 0:
        print(f"{a} es divisible por {c}")
    if b % a == 0:
        print(f"{b} es divisible por {a}")
    if b % c == 0:
        print(f"{b} es divisible por {c}")
    if c % a == 0:
        print(f"{c} es divisible por {a}")
    if c % b == 0:
        print(f"{c} es divisible por {b}")
        
# Solicitar al usuario que ingrese tres números
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))

# Llamar a la función para verificar divisibilidad
verificar_divisibilidad(a, b, c)
