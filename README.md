Este proyecto en Python permite realizar un análisis exploratorio de datos. Incluye funcionalidades para limpieza de datos, transformaciones matemáticas, cálculos estadísticos y regresión lineal, con visualizaciones gráficas.

## Características

- Carga y limpieza de bases de datos en formato Excel.
- Aplicación de logaritmo base 10 a columnas numéricas.
- Cálculo de medidas de tendencia central (media, mediana, moda, varianza, desviación estándar).
- Modelo de regresión lineal y visualización con `matplotlib`.
- Interfaz por consola basada en menú.

## Requisitos

- Python 3.x
- pandas
- numpy
- matplotlib
- scikit-learn
- openpyxl (para leer/escribir archivos Excel)

## Cómo usar
Ejecuta el archivo Python.

Selecciona las opciones del menú según el análisis que desees realizar:

1: Cargar y limpiar base de datos

2: Aplicar logaritmo base 10

3: Calcular estadísticas

4: Aplicar regresión lineal

5: Salir del programa

Nota: Algunas opciones requieren que primero se ejecute la opción 1 para generar los archivos necesarios.

## Estructura del Proyecto
📁 RLgalaxias/
├── galaxias_data.xlsx
├── archivo_limpio.xlsx
├── archivo_limpio_log10.xlsx
├── Medidas_centrales.xlsx
├── analisis_galaxias.py

## 📊 Archivos Excel del Proyecto
1. galaxias_data.xlsx
Ubicación: Se espera que esté en tu escritorio dentro de la ruta del proyecto.

Propósito: Es la base de datos original que contiene información astronómica cruda sobre galaxias.

Uso: Este archivo se carga en la opción 1 del menú para ser limpiado y transformado.

2. archivo_limpio.xlsx
Generado por: Opción 1 del menú.

Propósito: Es la versión limpia del archivo original, conservando solo las columnas relevantes (raefcorkpg, errreckg, raefcorkpr, errreckr, muecorg).

Uso: Sirve como base para los siguientes análisis. Este archivo asegura que se trabaja con datos consistentes y depurados.

3. archivo_limpio_log10.xlsx
Generado por: Opción 2 del menú.

Propósito: Contiene los mismos datos que archivo_limpio.xlsx, pero con la columna raefcorkpg transformada mediante logaritmo base 10.

Uso: Este archivo es necesario para realizar la regresión lineal (opción 4), donde se busca una relación lineal más clara entre variables.

4. Medidas_centrales.xlsx
Generado por: Opción 3 del menú.

Propósito: Almacena las medidas de tendencia central y dispersión (media, mediana, moda, varianza, desviación estándar) de cada columna numérica del archivo limpio.

Uso: Permite entender mejor la distribución y características estadísticas de los datos de galaxias.

Autor
Juan Emmanuel Sánchez Castañon — Estudiante de programación, CUGDL

