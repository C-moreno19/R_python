def verificar_signo(numero):
    # Verificamos si el número es positivo, negativo o cero
    if numero > 0:
        return "El número es positivo."
    elif numero < 0:
        return "El número es negativo."
    else:
        return "El número es cero."

# Solicitar al usuario el número a evaluar
numero = float(input("Ingresa un número: "))

# Evaluar y mostrar el resultado
resultado = verificar_signo(numero)
print(resultado)
