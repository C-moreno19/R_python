# Solicitar al usuario que ingrese tres números
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

mayor = max(num1, num2, num3);
menor = min(num1, num2, num3);

iguales = []
if num1 == num2:
    iguales.append(num1)
if num1 == num3:
    iguales.append(num1)
if num2 == num3:
    iguales.append(num2)

print(f"El numero mayor es: {mayor}");
print(f"El numero menor es: {menor}");

if len(iguales) == 0:
    print("Los tres números son diferentes.")
elif len(set(iguales)) == 1:
    print(f"Los números iguales son estos: {iguales[0]}.")
