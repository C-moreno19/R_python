def verificar_par_impar(numero):
    # Verificamos si el número es par o impar usando el operador módulo (%)
    if numero % 2 == 0:
        return "El número es par."
    else:
        return "El número es impar."

# Solicitamos al usuario el número a evaluar
numero = int(input("Ingresa un número entero: "))

# Evaluamos y mostramos si es par o impar
resultado = verificar_par_impar(numero)
print(resultado)
