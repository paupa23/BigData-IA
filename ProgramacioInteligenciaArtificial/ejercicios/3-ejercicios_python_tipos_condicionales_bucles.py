# Ejercicio 1. Control de notas
# Crea una lista llamada notas con al menos 10 calificaciones numéricas

# El programa debe:
# - Mostrar todas las notas
# - Calcular cuántas notas están aprobadas y cuántas suspendidas
# - Calcular la nota media
# - Mostrar la nota más alta y la nota más baja
# - Indicar si la media final está aprobada o suspendida
# Condición: Debe utilizar listas, bucle for, operadores de comparación y condicionales

notas = [5, 8, 7, 10, 5, 2, 8, 9, 10, 4]

print ("Todas las notas: ", notas)

suspendidas = 0
aprobadas = 0
for nota in notas:
    if nota > 5:
        aprobadas += 1
    else:
        suspendidas += 1

media = sum(notas) / len(notas)

print("La media de las notas es: ", media)

print("El numero mas alto es: ", max(notas), "Y el mas bajo es: ", min(notas))


if aprobadas > suspendidas:
    print("La media de notas son aprobadas")
else:
    print("La media de notas son suspendidas")



# Ejercicio 2. Carrito de la compra
# Crea dos listas: una con nombres de productos y otra con sus precios
# El programa debe:
# - Mostrar cada producto con su precio
# - Calcular el precio total de la compra
# - Aplicar un descuento del 10% si el total supera 20 euros
# - Mostrar el total final que debe pagarse
# Condición: Debe utilizar zip, un acumulador, if y operadores aritméticos

productos = ["pan", "leche", "arroz", "huevos"]
precios = [1.20, 0.95, 2.10, 2.80]
i = 1
total = sum(precios)

for producto, precio in zip(productos, precios):
    print("Producto", i)
    print(producto,"Cuesta", precio)

    i+= 1

print("Precio total de la compra: ", total)

total_con_descuento = total * 0,90
descuento = True

if total > 20:
    print("Tienes un 10" "%" "de descuento, la compra se te queda a: ", total_con_descuento)
    descuento = True
else:
    print("No tienes descuento ya que no supera 20 euros")
    descuento = False

if descuento is True:
    print("Tienes que pagar: ", total_con_descuento)
else:
    print("Tienes que pagar: ", total)


# Ejercicio 3. Registro de alumno
# Crea un diccionario llamado alumno con los siguientes datos

# El programa debe:
# - Mostrar todos los datos del alumno
# - Indicar si el alumno aprueba. Aprueba si su nota_media es mayor o igual que 5
# - Indicar si debe recibir un aviso. Recibe aviso si tiene más de 10 faltas
# - Mostrar un mensaje final combinando el resultado académico y el aviso
# Condición: Debe utilizar diccionarios, if, elif, else y operadores lógicos

alumno = {
    "nombre":"paupa",
    "edad": 22,
    "curso": "IaBigdata",
    "nota_media": 10,
    "faltas": 0
}
aviso_faltas = False
aprobado = False

for clave, valor in alumno.items():
    print(clave, ":", valor)

if alumno["nota_media"] > 5 :
    print("El alumno:", alumno["nombre"], "ha aprobado")
    aprobado = True
else:
    print("El alumno:", alumno["nombre"], "ha suspendido")
    aprobado = False

if alumno["faltas"] > 10:
    print("Cuidado, llevas mas de 10 faltas")
    aviso_faltas = True
else:
    print("vas bien de faltas")
    aviso_faltas = False

if aviso_faltas == True and aprobado == True:
    print("Cuidado, llevas mas de 10 faltas, pero has aprobado")
elif aviso_faltas == True and aprobado == False:
    print("Llevas mas de 10 faltas, y estas suspendido por nota")
elif aviso_faltas == False and aprobado == False:
    print("No has faltado casi, pero ya has suspendido")
elif aviso_faltas == False and aprobado == True:
    print("No tienes faltas, y has aprobado, muy bien")

# Ejercicio 4. Números pares, impares y múltiplos
# Usando range, recorre los números del 1 al 50
# El programa debe:
# - Contar cuántos números son pares
# - Contar cuántos números son impares
# - Contar cuántos números son múltiplos de 5
# - Mostrar los tres resultados finales
# Condición: Debe utilizar for, range, el operador módulo % y contadores

pares = 0
impares = 0
multiplos_5 = 0

for i in range(1, 51):
    if i % 2 == 0:
        pares += 1
    elif i % 2 != 0:
        impares += 1
    if i % 5 == 0:
        multiplos_5 += 1

print ("Hay", pares, "numeros pares")
print ("Hay", impares, "numeros impares")
print ("Hay", multiplos_5, "numeros multiplos de 5")


# Ejercicio 5. Validación de contraseña
# Crea una variable llamada password con una contraseña de prueba
# El programa debe:
# - Comprobar si la contraseña tiene al menos 8 caracteres
# - Comprobar si contiene el símbolo @
# - Comprobar que no sea igual a 12345678
# - Si cumple todas las condiciones, mostrar Contraseña válida
# - En caso contrario, mostrar Contraseña no válida
# Condición: Debe utilizar strings, len, operadores lógicos y condicionales. Para comprobar si aparece @ dentro
# del texto puede utilizarse "@" in password