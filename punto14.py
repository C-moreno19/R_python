def evaluar_expresion(n):
    # Verificar si n es cero
    if n == 0:
        return "Error: No se puede dividir por cero."
    
    # Calcular la expresión 1/n
    resultado = 1 / n
    return resultado

# Solicitar al usuario el valor de n
n = float(input("Ingresa el valor de n: "))

# Evaluar la expresión y mostrar el resultado
resultado = evaluar_expresion(n)

# Mostrar el resultado o el mensaje de error
print(f"El resultado de 1/{n} es: {resultado}")
