import pandas
import numpy
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
bandera=0
salir= 0
while True:
    print("1.- Cargar y limpiar base de datos Galaxia\n2.- Aplicar algoritmo base 10 a raefcorkpg\n3.- Medidas de tencia central\n4.- Aplicar regrecion lineal\n5.-Salir")
    try:
        opc = int(input("Ingresa una opción: "))
        if opc < 1 or opc > 5:
            print("Opción no válida. Por favor ingresa un número entre 1 y 5.")
            continue
    except ValueError:
        print("Entrada inválida. Por favor ingresa un número válido.")
        continue

    match opc:
        case 1:
            print("Cargando y limpiando la base de datos esto puede tardar unos minutos, porfavor espere\n")
            archivo = '/Users/juansanchez/Desktop/CUGDL/2º semestre/Programacion/RLgalaxias/galaxias_data.xlsx' 
            df= pandas.read_excel(archivo)
            df_limpio = df[['raefcorkpg', 'errreckg', 'raefcorkpr', 'errreckr', 'muecorg']]
            archivo_salida = '/Users/juansanchez/Desktop/CUGDL/2º semestre/Programacion/RLgalaxias/archivo_limpio.xlsx'  
            df_limpio.to_excel(archivo_salida, index=False)
            print("Base de datos limpia creada en: ",archivo_salida )
            bandera=1
        case 2:
            if (bandera==1):
                print("Cargando y aplicando Log base 10 a la columna reafcorkpg, porfavor espere\n")
                archivo_limpio = '/Users/juansanchez/Desktop/CUGDL/2º semestre/Programacion/RLgalaxias/archivo_limpio.xlsx' 
                df= pandas.read_excel(archivo_limpio)
                df['raefcorkpg']= numpy.log10(df['raefcorkpg'])
                df_limpio = df[['raefcorkpg', 'errreckg', 'raefcorkpr', 'errreckr', 'muecorg']]
                archivo_salida = '/Users/juansanchez/Desktop/CUGDL/2º semestre/Programacion/RLgalaxias/archivo_limpio_log10.xlsx'  
                df_limpio.to_excel(archivo_salida, index=False)
                print("Se a creado exitosamente archivo_limpio_log10 en:",archivo_salida )
            else: 
                print("Es necesario primero limpiar la base de datos, porfavor ejecute la opcion 1 primero\n")
        case 3:
            if (bandera==1):
                print("Calculando medidas de tendencia central\n")
                archivo_limpio = '/Users/juansanchez/Desktop/CUGDL/2º semestre/Programacion/RLgalaxias/archivo_limpio.xlsx' 
                df = pandas.read_excel(archivo_limpio)
                # Crear un diccionario para almacenar los resultados
                estadisticas = {}

                for columna in df.columns:
                    datos = df[columna].dropna()  # Eliminar valores nulos
    
                    # Cálculo de medidas de tendencia central y dispersión
                    media = numpy.mean(datos)
                    mediana = numpy.median(datos)
                    moda = datos.mode().tolist()  # Puede haber más de una moda
                    varianza = numpy.var(datos, ddof=1)  # ddof=1 para varianza muestral
                    desviacion_estandar = numpy.std(datos, ddof=1)
    
                    estadisticas[columna] = {
                    "Media": media,
                    "Mediana": mediana,
                    "Moda": moda,
                    "Varianza": varianza,
                    "Desviación estándar": desviacion_estandar,
                    }

                # Convertir resultados a DataFrame y guardarlo en un archivo Excel
                resultado_df = pandas.DataFrame.from_dict(estadisticas, orient='index')
                archivo_salida = '/Users/juansanchez/Desktop/CUGDL/2º semestre/Programacion/RLgalaxias/Medidas_centrales.xlsx'  
                resultado_df.to_excel(archivo_salida)
        
            else: 
                print("Es necesario primero limpiar la base de datos, porfavor ejecute la opcion 1 primero\n")
        case 4:
            # Graficar el conjunto de datos en un diagrama de dispersión
            archivo = '/Users/juansanchez/Desktop/CUGDL/2º semestre/Programacion/RLgalaxias/archivo_limpio_log10.xlsx' 
            df = pandas.read_excel(archivo)
            plt.scatter(df.iloc[:, 0], df.iloc[:, 4], alpha=0.5)
            plt.xlabel(df.columns[0])
            plt.ylabel(df.columns[4])
            plt.title("Diagrama de dispersión")

            # Aplicar regresión lineal
            X = df.iloc[:, [0]].dropna()  # Variable independiente
            y = df.iloc[:, 4].dropna()  # Variable dependiente
            modelo = LinearRegression()
            modelo.fit(X, y)
            y_pred = modelo.predict(X)

            # Graficar la línea de regresión
            plt.plot(X, y_pred, color='red', linewidth=2, label='Regresión Lineal')
            plt.legend()
            plt.show()
        case 5:
            break
