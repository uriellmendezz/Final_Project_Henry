# Importa las librerías necesarias
from google.cloud import bigquery
import json
import os
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
import pandas as pd
#from fastapi.templating import Jinja2Templates
#from fastapi.staticfiles import StaticFiles

# Configura las credenciales de Google Cloud
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'google_credentials.json'
client = bigquery.Client()
project_name = 'nyc-taxis-project'
dataset_name = 'new_york_transport_project'

# Crea una instancia de FastAPI
app = FastAPI()

# Define la ruta de inicio que servirá la página HTML
@app.get("/")
def read_root():
    message = '''
        Welcome to the New York Taxi Project API!

        You can request for the following endpoints:
        - /zones
        - Obtener la cantidad de viajes realizados en una zona en especifico durante el ultimo mes
        - Obtener las zonas con mayor circulaciones de taxis por tipos de transporte
            - Top 5 barrios con mas viajes en los ultimos 10 dias (ordenado de mayor a menor)
            - Top 5 barrios con menos viajes en los ultimos 10 dias (ordenado de mayor a menor)
            - Predicción de concentraciones de CO para la ciudad de Manhattan en una determinada fecha futura
            - Prediccion de cantidad de viajes para un tipo de transporte en especifico
            - Promedio de concentraciones de CO por barrio
    '''
    functions = {
        '/zones': 'Get info about zones',
        '/taxis':'Get info about taxis'
    }
    json_str = json.dumps(functions, indent=4, default=str)
    return Response(content=json_str, media_type='application/json')

@app.get('/zones')
def zones():
    manhattan_zones = {'Alphabet City': '4',
 'Battery Park': '12',
 'Battery Park City': '13',
 'Bloomingdale': '24',
 'Central Harlem': '41',
 'Central Harlem North': '42',
 'Central Park': '43',
 'Chinatown': '45',
 'Clinton East': '48',
 'Clinton West': '50',
 'East Chelsea': '68',
 'East Harlem North': '74',
 'East Harlem South': '75',
 'East Village': '79',
 'Financial District North': '87',
 'Financial District South': '88',
 'Flatiron': '90',
 'Garment District': '100',
 "Governor's Island/Ellis Island/Liberty Island": '105',
 'Gramercy': '107',
 'Greenwich Village North': '113',
 'Greenwich Village South': '114',
 'Hamilton Heights': '116',
 'Highbridge Park': '120',
 'Hudson Sq': '125',
 'Inwood': '127',
 'Inwood Hill Park': '128',
 'Kips Bay': '137',
 'Lenox Hill East': '140',
 'Lenox Hill West': '141',
 'Lincoln Square East': '142',
 'Lincoln Square West': '143',
 'Little Italy/NoLiTa': '144',
 'Lower East Side': '148',
 'Manhattan Valley': '151',
 'Manhattanville': '152',
 'Marble Hill': '153',
 'Meatpacking/West Village West': '158',
 'Midtown Center': '161',
 'Midtown East': '162',
 'Midtown North': '163',
 'Midtown South': '164',
 'Morningside Heights': '166',
 'Murray Hill': '170',
 'Penn Station/Madison Sq West': '186',
 'Randalls Island': '194',
 'Roosevelt Island': '202',
 'Seaport': '209',
 'SoHo': '211',
 'Stuy Town/Peter Cooper Village': '224',
 'Sutton Place/Turtle Bay North': '229',
 'Times Sq/Theatre District': '230',
 'TriBeCa/Civic Center': '231',
 'Two Bridges/Seward Park': '232',
 'UN/Turtle Bay South': '233',
 'Union Sq': '234',
 'Upper East Side North': '236',
 'Upper East Side South': '237',
 'Upper West Side North': '238',
 'Upper West Side South': '239',
 'Washington Heights North': '243',
 'Washington Heights South': '244',
 'West Chelsea/Hudson Yards': '246',
 'West Village': '249',
 'World Trade Center': '261',
 'Yorkville East': '262',
 'Yorkville West': '263'}
    
    json_str = json.dumps(manhattan_zones, indent=4, default=str)
    return Response(content=json_str, media_type='application/json')


@app.get('/zones/{zone}')
def get_zone(zone):
    zone = zone.replace('%20',' ')

    tabla = 'green_taxis'
    abr = 'vt'
    column = 'TotalGreen'

    query = f'''
    WITH UltimoMes AS (
    SELECT
        DATE_SUB(MAX(DATE({abr}.pickup_datetime)), INTERVAL 1 MONTH) AS MesUltimoMes
    FROM `new_york_transport_project.{tabla}` {abr}
    )

    SELECT
    mz.Zone AS Zone,
    mz.LocationID AS IdZone,
    (COUNT({abr}.PULocationID) + COUNT({abr}.DOLocationID)) as {column},
    EXTRACT(MONTH FROM UltimoMes.MesUltimoMes) AS month,
    EXTRACT(YEAR FROM UltimoMes.MesUltimoMes) AS year
    FROM `new_york_transport_project.manhattan_zones` mz
    JOIN `new_york_transport_project.{tabla}` {abr}
    ON mz.LocationID = {abr}.PULocationID
    JOIN UltimoMes
    ON DATE({abr}.pickup_datetime) >= UltimoMes.MesUltimoMes
    WHERE mz.Zone = '{zone}'
    GROUP BY Zone, year, month, IdZone;
    '''
    df1= client.query(query).to_dataframe()

    tabla = 'yellow_taxis'
    abr = 'yt'
    column = 'TotalYellow'

    query = f'''
    WITH UltimoMes AS (
    SELECT
        DATE_SUB(MAX(DATE({abr}.pickup_datetime)), INTERVAL 1 MONTH) AS MesUltimoMes
    FROM `new_york_transport_project.{tabla}` {abr}
    )

    SELECT
    mz.Zone AS Zone,
    mz.LocationID AS IdZone,
    (COUNT({abr}.PULocationID) + COUNT({abr}.DOLocationID)) as {column},
    EXTRACT(MONTH FROM UltimoMes.MesUltimoMes) AS month,
    EXTRACT(YEAR FROM UltimoMes.MesUltimoMes) AS year
    FROM `new_york_transport_project.manhattan_zones` mz
    JOIN `new_york_transport_project.{tabla}` {abr}
    ON mz.LocationID = {abr}.PULocationID
    JOIN UltimoMes
    ON DATE({abr}.pickup_datetime) >= UltimoMes.MesUltimoMes
    WHERE mz.Zone = '{zone}'
    GROUP BY Zone, year, month, IdZone;
    '''
    df2= client.query(query).to_dataframe()

    tabla = 'black_taxis'
    abr = 'bt'
    column = 'TotalBlack'

    query = f'''
    WITH UltimoMes AS (
    SELECT
        DATE_SUB(MAX(DATE({abr}.pickup_datetime)), INTERVAL 1 MONTH) AS MesUltimoMes
    FROM `new_york_transport_project.{tabla}` {abr}
    )

    SELECT
    mz.Zone AS Zone,
    mz.LocationID AS IdZone,
    (COUNT({abr}.PULocationID) + COUNT({abr}.DOLocationID)) as {column},
    EXTRACT(MONTH FROM UltimoMes.MesUltimoMes) AS month,
    EXTRACT(YEAR FROM UltimoMes.MesUltimoMes) AS year
    FROM `new_york_transport_project.manhattan_zones` mz
    JOIN `new_york_transport_project.{tabla}` {abr}
    ON mz.LocationID = {abr}.PULocationID
    JOIN UltimoMes
    ON DATE({abr}.pickup_datetime) >= UltimoMes.MesUltimoMes
    WHERE mz.Zone = '{zone}'
    GROUP BY Zone, year, month, IdZone;
    '''
    df3= client.query(query).to_dataframe()

    tabla = 'grey_taxis'
    abr = 'gt'
    column = 'TotalGrey'

    query = f'''
    WITH UltimoMes AS (
    SELECT
        DATE_SUB(MAX(DATE({abr}.pickup_datetime)), INTERVAL 1 MONTH) AS MesUltimoMes
    FROM `new_york_transport_project.{tabla}` {abr}
    )

    SELECT
    mz.Zone AS Zone,
    mz.LocationID AS IdZone,
    (COUNT({abr}.PULocationID) + COUNT({abr}.DOLocationID)) as {column},
    EXTRACT(MONTH FROM UltimoMes.MesUltimoMes) AS month,
    EXTRACT(YEAR FROM UltimoMes.MesUltimoMes) AS year
    FROM `new_york_transport_project.manhattan_zones` mz
    JOIN `new_york_transport_project.{tabla}` {abr}
    ON mz.LocationID = {abr}.PULocationID
    JOIN UltimoMes
    ON DATE({abr}.pickup_datetime) >= UltimoMes.MesUltimoMes
    WHERE mz.Zone = '{zone}'
    GROUP BY Zone, year, month, IdZone;
    '''
    df4= client.query(query).to_dataframe()

    # Realiza los merges de dos en dos.
    merged_df1 = pd.merge(df1, df2, on=['Zone','IdZone','month','year'])
    merged_df2 = pd.merge(df3, df4, on=['Zone','IdZone','month','year'])

    # Luego, combina los resultados anteriores en uno solo.
    df = pd.merge(merged_df1, merged_df2, on=['Zone','IdZone','month','year'])
    if len(df) < 1:
        message = 'No data for this zone in the last month'
        return message
    else:
        df['TotalTrips'] = df.TotalGreen + df.TotalYellow + df.TotalBlack + df.TotalGrey
        df = df[["Zone",'IdZone','year',"month", "TotalTrips", "TotalGreen", "TotalYellow", "TotalBlack", "TotalGrey"]]

        df['%_Green'] = round((df['TotalGreen'] * 100) / df['TotalTrips'],3)
        df['%_Yellow'] = round((df['TotalYellow'] * 100) / df['TotalTrips'],3)
        df['%_Black'] = round((df['TotalBlack'] * 100) / df['TotalTrips'],3)
        df['%_Grey'] = round((df['TotalGrey'] * 100) / df['TotalTrips'],3)

        data_json = df.to_dict(orient='records')[0]
        json_str = json.dumps(data_json, indent=4, default=str)

        return Response(content=json_str, media_type='application/json')


@app.get('/taxis')
def home_taxis():
    data_json = {
        '/greens':'Get a ranking of zones with the highest circulation of green taxis',
        '/yellows':'Get a ranking of zones with the highest circulation of yellow taxis',
        '/blacks':'Get a ranking of zones with the highest circulation of black taxis',
        '/greys':'Get a ranking of zones with the highest circulation of grey taxis'

    }

    json_str = json.dumps(data_json, indent=4, default=str)
    return Response(content=json_str, media_type='application/json')

@app.get('/taxis/{color}')
def home_taxis(color):
    if color not in ['greens','yellows','blacks','greys']:
        data_json = {
        'taxis/greens':'Get a ranking of zones with the highest circulation of green taxis in the last month',
        'taxis/yellows':'Get a ranking of zones with the highest circulation of yellow taxis in the last month',
        'taxis/blacks':'Get a ranking of zones with the highest circulation of black taxis in the last month',
        'taxis/greys':'Get a ranking of zones with the highest circulation of grey taxis in the last month'

        }
        json_str = json.dumps(data_json, indent=4, default=str)

        return Response(content=json_str, media_type='application/json')
    else:
        color = color[:-1]
        query = f'''
        WITH UltimoMes AS (
        SELECT
            DATE_SUB(MAX(DATE(bt.pickup_datetime)), INTERVAL 1 MONTH) AS FechaUltimoMes
        FROM `nyc-taxis-project.new_york_transport_project.{color}_taxis` bt
        )

        SELECT
        mz.Zone AS Zone,
        mz.LocationID AS IdZone,
        EXTRACT(YEAR FROM UltimoMes.FechaUltimoMes) as year,
        EXTRACT(MONTH FROM UltimoMes.FechaUltimoMes) as month,
        (COUNT(bt.PULocationID) + COUNT(bt.DOLocationID)) AS TotalTrips
        FROM `nyc-taxis-project.new_york_transport_project.{color}_taxis` bt
        JOIN `new_york_transport_project.manhattan_zones` mz
        ON bt.PULocationID = mz.LocationID
        JOIN `new_york_transport_project.manhattan_zones` mz2
        ON bt.DOLocationID = mz2.LocationID
        JOIN UltimoMes
        ON DATE(bt.pickup_datetime) >= UltimoMes.FechaUltimoMes
        GROUP BY Zone, IdZone, year, month
        ORDER BY TotalTrips DESC;
        '''

        df = client.query(query).to_dataframe()
        df['Ranking'] = range(1, len(df) + 1)
        if color == 'green':
            df = df[['Ranking','Zone','IdZone','year','month','TotalTrips']].rename(columns={'TotalTrips':'TotalGreenTrips'})
        elif color == 'yellow':
            df = df[['Ranking','Zone','IdZone','year','month','TotalTrips']].rename(columns={'TotalTrips':'TotalYellowTrips'})
        elif color == 'black':
            df = df[['Ranking','Zone','IdZone','year','month','TotalTrips']].rename(columns={'TotalTrips':'TotalBlackTrips'})
        elif color == 'grey':
            df = df[['Ranking','Zone','IdZone','year','month','TotalTrips']].rename(columns={'TotalTrips':'TotalGreyTrips'})
        
        data_json = df.to_dict(orient='records')
        json_str = json.dumps(data_json, indent=4, default=str)

        return Response(content=json_str, media_type='application/json')


