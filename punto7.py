
nombre = input("Ingrese su nombre: ");
edad = int(input("Ingrese su edad: "));
sexo = input("Ingrese su sexo: ");
estado_civil = input("Ingrese su estado_civil: ");

if (sexo == "masculino" and estado_civil == "casado" and edad > 40) or (sexo == "femenino"  and estado_civil == "soltera" and edad < 50):
    print(f"Su nombre es: {nombre}");


