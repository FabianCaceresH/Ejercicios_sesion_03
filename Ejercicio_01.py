# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos
numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))
if numero_1 > numero_2  :
    print(f"el numero {numero_1} es mayor")
elif numero_1 < numero_2 :
    print(f"el numero {numero_2} es mayor")
if numero_1 > 0:
        print("numero1 es positivo")
if numero_1 <0:
        print("numero1 es negativo")
elif numero_1 == 0:
    print("numero1 es 0")
if numero_1 < 100 and numero_1 > 0 :
    print("numero1 es menor a 100 y mayor a 0")
if numero_1 < 10 or numero_1 < numero_2:
    print("numero1 es menor a 10 o menor a numero2")