## EDA (Exploratory Dats Analysis) con Python

### 1. Tamaño de dataframe, columnas y tipo de dato, cantidad de registros, volumen en memoria

>df.info()

### 2. Detectar y contar filas duplicadas en el dataframe
>duplicated_rows = df[df.duplicated()]  
>duplicated_count = duplicated_rows.shape[0]  
>print("Filas duplicadas:")  
>print(duplicated_rows)
>print("Cantidad de filas duplicadas:", duplicated_count)

### 3. Detectar valores faltantes y el % sobre el valor de los datos

> **Detectar valores faltantes y calcular su porcentaje por columna**  
>missing_data = df.isna().sum()  
>missing_percentage = (missing_data / len(df)) * 100`

> **Crear un nuevo dataframe con los resultados**  
>missing_df = pd.DataFrame({'Missing Count': missing_data, 'Missing Percentage': missing_percentage})  
>print(missing_df)`
