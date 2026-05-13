import pandas as pd
import random

# Lista de nombres
nombres = [
    "Ana", "Carlos", "Marta", "David", "Laura", "Javier", "Sofia",
    "Pedro", "Elena", "Raul", "Nuria", "Alberto", "Lucia", "Hugo",
    "Claudia", "Daniel", "Irene", "Marcos", "Paula", "Sergio",
    "Beatriz", "Adrian", "Carmen", "Victor", "Patricia", "Oscar",
    "Silvia", "Manuel", "Teresa", "Ivan"
]

apellidos = [
    "Lopez", "Ruiz", "Garcia", "Perez", "Sanchez", "Martin",
    "Torres", "Gomez", "Diaz", "Moreno", "Vega", "Cano",
    "Romero", "Serrano", "Molina", "Ortega", "Castro",
    "Gil", "Navarro", "Ramos", "Leon", "Vidal", "Rubio",
    "Herrera", "Marin", "Fuentes", "Pastor", "Rios",
    "Nieto", "Aguilar"
]

datos = []

for i in range(1, 101):

    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)

    nombre_completo = f"{nombre} {apellido}"
    email = f"{nombre.lower()}.{apellido.lower()}@email.com"

    matematicas = round(random.uniform(2, 10), 1)
    criptografia = round(random.uniform(2, 10), 1)
    blockchain = round(random.uniform(2, 10), 1)
    mineria = round(random.uniform(2, 10), 1)
    learning = round(random.uniform(2, 10), 1)

    participacion = random.randint(20, 100)
    horas = random.randint(5, 50)
    tareas = random.randint(1, 10)
    asistencia = random.randint(30, 100)
    foros = random.randint(0, 10)

    media = (
        matematicas +
        criptografia +
        blockchain +
        mineria +
        learning
    ) / 5

    # Regla simple de riesgo
    riesgo = 1 if media < 5 or participacion < 50 else 0

    datos.append([
        i,
        nombre_completo,
        email,
        "Analisis de Datos II",
        matematicas,
        criptografia,
        blockchain,
        mineria,
        learning,
        participacion,
        horas,
        tareas,
        asistencia,
        foros,
        riesgo
    ])

# Crear DataFrame
df = pd.DataFrame(datos, columns=[
    "id",
    "nombre",
    "email",
    "curso",
    "matematicas",
    "criptografia",
    "blockchain",
    "mineria_datos",
    "learning_analytics",
    "participacion",
    "horas_plataforma",
    "tareas_entregadas",
    "asistencia",
    "foros",
    "riesgo_real"
])

# Guardar CSV
df.to_csv("datos_estudiantes.csv", index=False)

print("CSV generado correctamente con 100 registros")


# ==============================
# ANALISIS DE LEARNING ANALYTICS
# ==============================

print("\n--- ANALISIS DE DATOS EDUCATIVOS ---")

# Leer el CSV generado
df = pd.read_csv("datos_estudiantes.csv")

# Calcular nota media de las 5 asignaturas
df["nota_media"] = df[
    [
        "matematicas",
        "criptografia",
        "blockchain",
        "mineria_datos",
        "learning_analytics"
    ]
].mean(axis=1).round(2)

# Clasificar estudiantes
df["estado"] = df["riesgo_real"].apply(
    lambda x: "En riesgo" if x == 1 else "Estable"
)

# Mostrar primeras filas
print("\nPrimeros estudiantes analizados:")
print(df[["id", "nombre", "nota_media", "participacion", "estado"]].head(10))

# Resumen general
total_estudiantes = len(df)
estudiantes_riesgo = df[df["estado"] == "En riesgo"].shape[0]
estudiantes_estables = df[df["estado"] == "Estable"].shape[0]
media_general = round(df["nota_media"].mean(), 2)

print("\nResumen general:")
print(f"Total de estudiantes: {total_estudiantes}")
print(f"Estudiantes estables: {estudiantes_estables}")
print(f"Estudiantes en riesgo: {estudiantes_riesgo}")
print(f"Nota media general del curso: {media_general}")

# Guardar CSV actualizado
df.to_csv("datos_estudiantes_analizados.csv", index=False)

print("\nArchivo datos_estudiantes_analizados.csv creado correctamente")



# ==============================
# VISUALIZACION DE DATOS
# ==============================

import matplotlib.pyplot as plt

# Grafico 1: estudiantes en riesgo vs estables

conteo_estado = df["estado"].value_counts()

plt.figure(figsize=(6, 6))

plt.pie(
    conteo_estado,
    labels=conteo_estado.index,
    autopct='%1.1f%%')

plt.title("Estudiantes estables vs en riesgo")
plt.savefig("grafico_riesgo.png")
print("\nGrafico grafico_riesgo.png generado correctamente")


# Grafico 2: distribucion de notas medias

plt.figure(figsize=(8, 5))

plt.hist(df["nota_media"], bins=10)

plt.title("Distribucion de notas medias")
plt.xlabel("Nota media")
plt.ylabel("Numero de estudiantes")
plt.savefig("grafico_notas.png")

print("Grafico grafico_notas.png generado correctamente")



# ==============================
# CRIPTOGRAFIA: CIFRADO DE DATOS SENSIBLES
# ==============================

from cryptography.fernet import Fernet

# Generar clave simetrica
clave = Fernet.generate_key()
cifrador = Fernet(clave)

# Cifrar nombre y email
df["nombre_cifrado"] = df["nombre"].apply(
    lambda x: cifrador.encrypt(x.encode()).decode()
)

df["email_cifrado"] = df["email"].apply(
    lambda x: cifrador.encrypt(x.encode()).decode()
)

# Ejemplo de descifrado del primer estudiante
nombre_descifrado = cifrador.decrypt(
    df.loc[0, "nombre_cifrado"].encode()
).decode()

print("\n--- CRIPTOGRAFIA ---")
print("Datos sensibles cifrados correctamente")
print("Ejemplo nombre original:", df.loc[0, "nombre"])
print("Ejemplo nombre cifrado:", df.loc[0, "nombre_cifrado"])
print("Ejemplo nombre descifrado:", nombre_descifrado)

# Guardar dataset cifrado
df.to_csv("datos_estudiantes_cifrados.csv", index=False)

# Guardar clave en archivo separado
with open("clave.key", "wb") as archivo_clave:
    archivo_clave.write(clave)

print("Archivo datos_estudiantes_cifrados.csv creado correctamente")
print("Clave guardada en clave.key")



# ==============================
# BLOCKCHAIN: VERIFICACION DE INTEGRIDAD CON HASH
# ==============================

import hashlib
import json
from datetime import datetime

class Bloque:
    def __init__(self, indice, datos, hash_anterior):
        self.indice = indice
        self.timestamp = str(datetime.now())
        self.datos = datos
        self.hash_anterior = hash_anterior
        self.hash_actual = self.calcular_hash()

    def calcular_hash(self):
        bloque_string = json.dumps({
            "indice": self.indice,
            "timestamp": self.timestamp,
            "datos": self.datos,
            "hash_anterior": self.hash_anterior
        }, sort_keys=True).encode()

        return hashlib.sha256(bloque_string).hexdigest()


def crear_blockchain(df):
    blockchain = []

    bloque_genesis = Bloque(
        0, {"mensaje": "Bloque inicial del sistema Learning Analytics"}, "0")

    blockchain.append(bloque_genesis)

    for i in range(5):
        estudiante = df.iloc[i]

        datos_bloque = {
            "id": int(estudiante["id"]),
            "nota_media": float(estudiante["nota_media"]),
            "estado": estudiante["estado"] }

        nuevo_bloque = Bloque(
            i + 1,
            datos_bloque,
            blockchain[-1].hash_actual )

        blockchain.append(nuevo_bloque)

    return blockchain


blockchain = crear_blockchain(df)

print("\n--- BLOCKCHAIN / HASH ---")
print("Blockchain educativa creada correctamente")

for bloque in blockchain:
    print("\nBloque:", bloque.indice)
    print("Datos:", bloque.datos)
    print("Hash anterior:", bloque.hash_anterior)
    print("Hash actual:", bloque.hash_actual)


# Guardar blockchain en archivo txt
with open("blockchain_educativa.txt", "w", encoding="utf-8") as archivo:
    for bloque in blockchain:
        archivo.write(f"Bloque: {bloque.indice}\n")
        archivo.write(f"Timestamp: {bloque.timestamp}\n")
        archivo.write(f"Datos: {bloque.datos}\n")
        archivo.write(f"Hash anterior: {bloque.hash_anterior}\n")
        archivo.write(f"Hash actual: {bloque.hash_actual}\n")
        archivo.write("-" * 50 + "\n")

print("\nArchivo blockchain_educativa.txt creado correctamente")



# ==============================
# MACHINE LEARNING: PREDICCION DE RIESGO
# ==============================

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

print("\n--- MACHINE LEARNING ---")

# Variables que usara el modelo
X = df[
    [
        "nota_media",
        "participacion",
        "horas_plataforma",
        "tareas_entregadas",
        "asistencia",
        "foros"
    ]
]

# Variable objetivo
y = df["riesgo_real"]

# Separar datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# Crear y entrenar modelo
modelo = LogisticRegression()
modelo.fit(X_train, y_train)

# Predicciones
predicciones = modelo.predict(X_test)

# Evaluacion
precision = accuracy_score(y_test, predicciones)

print("Modelo de regresion logistica entrenado correctamente")
print(f"Precision del modelo: {round(precision * 100, 2)}%")

print("\nInforme de clasificacion:")
print(classification_report(y_test, predicciones))

# Prediccion ejemplo de un estudiante nuevo
nuevo_estudiante = pd.DataFrame([{
    "nota_media": 4.8,
    "participacion": 42,
    "horas_plataforma": 12,
    "tareas_entregadas": 5,
    "asistencia": 55,
    "foros": 1
}])
prediccion_nuevo = modelo.predict(nuevo_estudiante)

resultado = "En riesgo" if prediccion_nuevo[0] == 1 else "Estable"

print("\nPrediccion para estudiante nuevo:")
print("Nota media: 4.8 | Participacion: 42 | Horas: 12 | Tareas: 5 | Asistencia: 55 | Foros: 1")
print("Resultado predicho:", resultado)



# ==============================
# VALIDACION Y PRUEBAS
# ==============================

print("\n--- VALIDACION Y PRUEBAS ---")

# Prueba 1: comprobar cifrado y descifrado
nombre_original = df.loc[0, "nombre"]
nombre_recuperado = cifrador.decrypt(
    df.loc[0, "nombre_cifrado"].encode()
).decode()

if nombre_original == nombre_recuperado:
    print("Prueba de cifrado: correcta")
else:
    print("Prueba de cifrado: error")


# Prueba 2: verificar integridad de la blockchain
def verificar_blockchain(blockchain):
    for i in range(1, len(blockchain)):
        bloque_actual = blockchain[i]
        bloque_anterior = blockchain[i - 1]

        if bloque_actual.hash_anterior != bloque_anterior.hash_actual:
            return False

        if bloque_actual.hash_actual != bloque_actual.calcular_hash():
            return False

    return True


if verificar_blockchain(blockchain):
    print("Prueba de integridad blockchain: correcta")
else:
    print("Prueba de integridad blockchain: error")


# Prueba 3: ejemplo de alteracion de datos
hash_original = blockchain[1].hash_actual
blockchain[1].datos["nota_media"] = 0.0
hash_modificado = blockchain[1].calcular_hash()

print("Hash original:", hash_original)
print("Hash tras modificar datos:", hash_modificado)

if hash_original != hash_modificado:
    print("La modificacion ha sido detectada correctamente")
else:
    print("No se ha detectado la modificacion")