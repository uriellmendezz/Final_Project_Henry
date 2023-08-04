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

### 6. Sesgo
> **Filtrar las columnas que no son datetime**  
> numeric_columns = df.select_dtypes(include=['int', 'float']).columns  

> **Calcular el sesgo de las columnas numéricas**
> skewness = df[numeric_columns].skew()  
> print("Sesgo de las columnas numéricas:")  
> print(skewness)  

### 7. Valores estadisticos por columna numerica
> df.describe()

- Podemos revisar la normalidad de las distribuciones por columna a partir del informe de ydata_profiling y sweetviz, mirando los histograma que generan esas librerias y cruzandolos con datos de df.describe() para poder determinar outliers.

### 8. Outliers

- #### <ins>Metodo Z Score. Variables con distribucion Normal</ins>  
  El método del Z-score es una herramienta que se basa en la idea de usar desviaciones estándar para medir la distancia       entre los datos y la media, y puedes elegir el umbral que mejor se adapte a tus necesidades.  

>  **Calcular el Z-score para la variable**  
> z_scores = (df['extra'] - df['extra'].mean()) / df['extra'].std()  

> **Definir un umbral para considerar outliers (por ejemplo, 2 desviaciones estándar)**  
> z_threshold = 2  

> **Detectar outliers**  
> outliers = df[abs(z_scores) > z_threshold]  

> **Calcular valores límite superior e inferior**
> upper_limit = df['extra'].mean() + z_threshold * df['extra'].std()  
> lower_limit = df['extra'].mean() - z_threshold * df['extra'].std()  

> **Mostrar resultados**  
> print("Cantidad de outliers:", len(outliers))  
> print("Valor límite superior:", upper_limit)  
> print("Valor límite inferior:", lower_limit)  
> print("\nOutliers detectados:")  
> print(outliers)

- #### <ins>Metodo del IQR. Variables con distribucion No Normal y sesgo No alto o No Muy ALto </ins>  

> **Calcular el primer cuartil (Q1) y el tercer cuartil (Q3)**  
> Q1 = df['passenger_count'].quantile(0.25)  
> Q3 = df['passenger_count'].quantile(0.75)  

> **Calcular el IQR (Rango Intercuartílico)**  
> IQR = Q3 - Q1  

> **Definir los límites para detectar outliers**  
> lower_limit = Q1 - 1.5 * IQR  
> upper_limit = Q3 + 1.5 * IQR  

> **Detectar outliers**  
> outliers = df[(df['passenger_count'] < lower_limit) | (df['passenger_count'] > upper_limit)]  

> **Mostrar resultados**  
> print("Límite inferior:", lower_limit)  
> print("Límite superior:", upper_limit)  
> print("\nOutliers detectados:")  
> print("Cantidad de outliers:", len(outliers))  
> print(outliers)  
