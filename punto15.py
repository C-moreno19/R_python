import cmath  # Importar para manejar soluciones complejas si es necesario

def resolver_ecuacion_cuadratica(a, b, c):
    # Calcular el discriminante
    discriminante = b**2 - 4*a*c
    
    # Si el discriminante es positivo, tenemos dos soluciones reales
    if discriminante > 0:
        raiz1 = (-b + cmath.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - cmath.sqrt(discriminante)) / (2*a)
        return raiz1, raiz2
    
    # Si el discriminante es cero, hay una única solución real (raíz doble)
    elif discriminante == 0:
        raiz = -b / (2*a)
        return raiz,
    
    # Si el discriminante es negativo, las soluciones son complejas
    else:
        raiz1 = (-b + cmath.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - cmath.sqrt(discriminante)) / (2*a)
        return raiz1, raiz2

# Ejemplo de uso
a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))

# Resolver la ecuación cuadrática
soluciones = resolver_ecuacion_cuadratica(a, b, c)

# Mostrar las soluciones
if len(soluciones) == 2:
    print(f"Las soluciones son: {soluciones[0]} y {soluciones[1]}")
else:
    print(f"La solución es: {soluciones[0]}")
