# Learning Analytics Tool with Cryptography and Blockchain

Proyecto académico desarrollado para la asignatura **Análisis de Datos II**.

La herramienta ha sido desarrollada en Python y combina conceptos básicos de:

- Learning Analytics
- análisis de datos educativos
- criptografía
- blockchain
- Machine Learning
- visualización de datos

## Funcionalidades principales

El sistema desarrollado permite:

- cargar y procesar datos educativos desde archivos CSV,
- analizar rendimiento académico y participación,
- clasificar estudiantes en riesgo,
- generar gráficas y visualizaciones,
- cifrar datos sensibles como nombres y correos electrónicos,
- simular una blockchain educativa mediante hashes SHA-256,
- realizar predicciones simples utilizando Machine Learning.

## Tecnologías utilizadas

- Python
- Pandas
- Matplotlib
- Scikit-learn
- Cryptography
- Hashlib

## Archivos principales

- `main.py` → código principal del proyecto
- `datos_estudiantes.csv` → dataset generado automáticamente
- `datos_estudiantes_analizados.csv` → dataset procesado
- `datos_estudiantes_cifrados.csv` → datos cifrados
- `grafico_riesgo.png` → gráfica de estudiantes en riesgo
- `grafico_notas.png` → gráfica de distribución de notas
- `blockchain_educativa.txt` → blockchain simulada generada por el sistema

## Ejecución del proyecto

Para ejecutar el proyecto:

```bash
python main.py