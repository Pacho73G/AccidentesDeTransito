# Librerias importadas para el desarrollo del proyecto
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Se lee el archivo CSV desde la ruta local
df = pd.read_csv("")#Aca poner la ruta del archivo csv 

# Se Limpia los nombres de las columnas (sin espacios y en minúsculas)
df.columns = df.columns.str.strip().str.lower()

# Se realiza una exploracion basica con DataFrame
print("Primeras filas del dataset:")
print(df.head())
print("\nForma del dataset:", df.shape)
print("\nColumnas disponibles:", df.columns)
print("\nResumen de tipos de datos:")
print(df.info())
print("\nResumen estadístico:")
print(df.describe())

# Se hace una Revisión de valores nulos por columna
print("\nValores nulos por columna:")
print(df.isnull().sum())

# Se convierte la columna 'fecha del hecho' a formato datetime
df['fecha del hecho'] = pd.to_datetime(df['fecha del hecho'], errors='coerce')

# Eliminamos filas con datos faltantes en 'edad' o 'fecha del hecho'
df = df.dropna(subset=['edad', 'fecha del hecho'])

# Se crea columnas nuevas con información útil
df['año'] = df['fecha del hecho'].dt.year           # Año del accidente
df['mes'] = df['fecha del hecho'].dt.month          # Mes del accidente
df['dia_semana'] = df['fecha del hecho'].dt.day_name()  # Día de la semana

# Se convierte la hora a formato numérico (hora en número)
df['hora'] = pd.to_datetime(df['hora del hecho (hh:mm)'], errors='coerce').dt.hour

# Estadísticas útiles
print("\nAccidentes por año:\n", df['año'].value_counts().sort_index())
print("\nAccidentes por mes:\n", df['mes'].value_counts().sort_index())
print("\nAccidentes por hora:\n", df['hora'].value_counts().sort_index())
print("\nAccidentes por día de la semana:\n", df['dia_semana'].value_counts())

# Visualización: Accidentes por mes
plt.figure(figsize=(10, 5))  # Tamaño del gráfico
df['mes'].value_counts().sort_index().plot(kind='bar')

plt.title("Accidentes por Mes en Colombia (2012–2022)")
plt.xlabel("Mes")
plt.ylabel("Cantidad de Accidentes")
plt.xticks(rotation=0)
plt.tight_layout()  # Asegura que no se corten los ejes
plt.show(block=True)  # Para VS Code: mantiene la ventana abierta
