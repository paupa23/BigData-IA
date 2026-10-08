# Ejercicios de pandas
# Ejecutar el archivo completo, porque los ejercicios usan los datos anteriores.


# Ejercicio 1
# Enunciado:
# Crear una estructura de datos en Python con la información de los candidatos.
# Usar un diccionario con las columnas nombre, edad, puntos y
# estudios_superiores. Los estudios superiores deben ser True o False.


datos = {
    "nombre": ["Ana", "Paco", "Marta", "Luis", "Elena", "Carlos", "Sara", "Miguel", "Lucia", "Andres"],
    "edad": [23, 21, 19, 25, 22, 20, 18, 27, 21, 24],
    "puntos": [43, 38, 41, 35, 39, 36, 34, 45, 42, 37],
    "estudios_superiores": [True, False, True, False, True, True, False, False, True, False]
}


# Ejercicio 2
# Enunciado:
# Importar pandas con el alias pd, convertir los datos en un DataFrame
# y mostrar la tabla completa por pantalla.


import pandas as pd

df = pd.DataFrame(datos)
print(df.to_string(index=False))


# Ejercicio 3
# Enunciado:
# Explorar el DataFrame mostrando las primeras filas, el tamaño, las
# columnas, los tipos de datos, la información general y las estadísticas
# básicas. Usar head(), shape, columns, dtypes, info() y describe().


print("Primeras filas:")
print(df.head())
print("\nTamaño (filas, columnas):", df.shape)
print("\nColumnas:", df.columns.tolist())
print("\nTipos de datos:")
print(df.dtypes)
print("\nInformación general:")
df.info()
print("\nEstadísticas básicas:")
print(df.describe())


# Ejercicio 4
# Enunciado:
# Escribir con tus propias palabras la regla de selección:
# - Si tiene 22 años o más, será apto si tiene al menos 40 puntos.
# - Si tiene menos de 22 años, necesita estudios superiores y al menos 35 puntos.
# - En cualquier otro caso, no será apto.


# Respuesta:
# Primero miro la edad. Si tiene 22 años o más, necesita al menos 40 puntos.
# Si tiene menos de 22, debe tener estudios superiores y al menos 35 puntos.
# Si no cumple la regla que le corresponde, no es apto.


# Ejercicio 5
# Enunciado:
# Añadir una columna llamada apto con True si la persona es apta
# y False si no lo es. Mostrar el DataFrame con la nueva columna.


df["apto"] = (
    ((df["edad"] >= 22) & (df["puntos"] >= 40))
    | ((df["edad"] < 22) & df["estudios_superiores"] & (df["puntos"] >= 35))
)
print(df.to_string(index=False))


# Ejercicio 6
# Enunciado:
# Contar cuántas personas son aptas y cuántas no usando value_counts().


recuento = df["apto"].value_counts()
print(recuento)
print("Aptas:", recuento.get(True, 0))
print("No aptas:", recuento.get(False, 0))


# Ejercicio 7
# Enunciado:
# Crear un DataFrame llamado candidatos_aptos que contenga solo
# las personas aceptadas para el trabajo y mostrarlo por pantalla.


candidatos_aptos = df[df["apto"]].copy()
print(candidatos_aptos.to_string(index=False))


# Ejercicio 8
# Enunciado:
# Crear otro DataFrame con las personas que tienen estudios superiores.
# Mostrarlo y responder:
# - ¿Cuántas personas tienen estudios superiores?
# - ¿Cuántas de ellas son aptas?
# - ¿Hay alguna persona con estudios superiores que no sea apta?


candidatos_con_estudios = df[df["estudios_superiores"]].copy()
print(candidatos_con_estudios.to_string(index=False))
print("\nPersonas con estudios superiores:", len(candidatos_con_estudios))
print("Aptas con estudios superiores:", candidatos_con_estudios["apto"].sum())
con_estudios_no_aptos = candidatos_con_estudios[~candidatos_con_estudios["apto"]]
print("¿Hay personas con estudios superiores no aptas?", not con_estudios_no_aptos.empty)
print(con_estudios_no_aptos.to_string(index=False))


# Ejercicio 9
# Enunciado:
# Ordenar el DataFrame por puntos y mostrarlo de menor a mayor
# y de mayor a menor usando sort_values().


print("De menor a mayor puntuación:")
print(df.sort_values("puntos", ascending=True).to_string(index=False))
print("\nDe mayor a menor puntuación:")
print(df.sort_values("puntos", ascending=False).to_string(index=False))


# Ejercicio 10
# Enunciado:
# Calcular la edad media, la puntuación media, la puntuación máxima
# y mínima y las edades de la persona más joven y la más mayor.
# Usar mean(), max() y min().


print("Edad media:", df["edad"].mean())
print("Puntuación media:", df["puntos"].mean())
print("Puntuación máxima:", df["puntos"].max())
print("Puntuación mínima:", df["puntos"].min())
print("Edad de la persona más joven:", df["edad"].min())
print("Edad de la persona más mayor:", df["edad"].max())


# Ejercicio 11
# Enunciado:
# Añadir una columna llamada nivel según los puntos:
# - alto: 40 puntos o más.
# - medio: entre 35 y 39 puntos.
# - bajo: menos de 35 puntos.


def clasificar_nivel(puntos):
    if puntos >= 40:
        return "alto"
    elif puntos >= 35:
        return "medio"
    else:
        return "bajo"

df["nivel"] = df["puntos"].apply(clasificar_nivel)
print(df.to_string(index=False))


# Ejercicio 12
# Enunciado:
# Agrupar por nivel y calcular cuántas personas hay, la media de edad
# y la media de puntos de cada grupo usando groupby().


resumen_por_nivel = df.groupby("nivel").agg(
    personas=("nombre", "size"),
    edad_media=("edad", "mean"),
    puntos_medios=("puntos", "mean")
).reindex(["alto", "medio", "bajo"])
print(resumen_por_nivel)


# Ejercicio 13
# Enunciado:
# Crear un nuevo DataFrame solo con las columnas nombre, puntos y apto.


columnas_seleccionadas = df[["nombre", "puntos", "apto"]].copy()
print(columnas_seleccionadas.to_string(index=False))


# Ejercicio 14
# Enunciado:
# Renombrar las columnas para que tengan nombres más descriptivos
# usando rename(). Por ejemplo, nombre pasa a Nombre del candidato
# y puntos pasa a Puntuación.


df_renombrado = df.rename(columns={
    "nombre": "Nombre del candidato",
    "edad": "Edad",
    "puntos": "Puntuación",
    "estudios_superiores": "Estudios superiores",
    "apto": "Apto para el puesto",
    "nivel": "Nivel de puntuación"
})
print(df_renombrado.to_string(index=False))


# Ejercicio 15
# https://colab.research.google.com/drive/13QefOnrvBbPA4Kq0nu8AfYvX3Il5Dlwm?usp=sharing