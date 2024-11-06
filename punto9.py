#imprimir los numeros  de mayor a menor
num_a = int(input("Digite numero a: "))
num_b = int(input("Digite numero b: "))
num_c = int(input("Digite numero c: "))

numeros = [num_a,num_b,num_c]
numeros.sort(reverse=True)


print("Los números ordenados de mayor a menor son:", numeros)