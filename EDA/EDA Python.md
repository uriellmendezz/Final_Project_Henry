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

### 4. Variables con gran cantidad de ceros

> **Calcular la cantidad de ceros en cada columna**  
> zero_counts = (df == 0).sum()  
> total_records = len(df)  
> zero_percentages = (zero_counts / total_records) * 100  
> print (zero_counts)

> **Filtrar columnas con un porcentaje de ceros superior al 20%, lo puedes cambiar para ajustar el porcentaje**  
> columns_with_high_zeros = zero_percentages[zero_percentages > 20]  
> print("Columnas con un porcentaje alto de ceros:")  
> print(columns_with_high_zeros)

### 5. Variables desbalanceadas
> **Calcular la frecuencia de cada valor en cada columna**  
> value_counts = df.apply(pd.value_counts)  

> **Calcular el porcentaje del valor más común en cada columna**  
> max_value_percentages = value_counts.max() / len(df) * 100  

> **Filtrar columnas con un valor muy común en más del 50% de los registros**  
> unbalanced_columns = max_value_percentages[max_value_percentages > 50]  
> print("Columnas desbalanceadas:")  
> print(unbalanced_columns)  

### 6. Detectar outliers
> **Calcular la frecuencia de cada valor en cada columna**

### 7. Sesgo
> **Filtrar las columnas que no son datetime**  
> numeric_columns = df.select_dtypes(include=['int', 'float']).columns  

> **Calcular el sesgo de las columnas numéricas**
> skewness = df[numeric_columns].skew()  
> print("Sesgo de las columnas numéricas:")  
> print(skewness)  

### 8. 
