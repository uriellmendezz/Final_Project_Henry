# Importa las librerías necesarias
from google.cloud import bigquery
import json
import os
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
'''from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles'''

# Configura las credenciales de Google Cloud
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'google_credentials.json'
client = bigquery.Client()
project_name = 'nyc-taxis-project'
dataset_name = 'new_york_transport_project'

# Crea una instancia de FastAPI
app = FastAPI()

'''
- Top 5 barrios con mas viajes en los ultimos 10 dias (ordenado de mayor a menor)
- Top 5 barrios con menos viajes en los ultimos 10 dias (ordenado de mayor a menor)
- Predicción de concentraciones de CO para la ciudad de Manhattan en una determinada fecha futura
- Consultar por un barrio en particular y ver que porcentaje de viajes le corresponde a cada tipo de transporte
- Prediccion de cantidad de viajes para un tipo de transporte en especifico

'''

# Define la ruta de inicio que servirá la página HTML
@app.get("/")
def read_root():
    message = '''
        Welcome to the New York Taxi Project API!

        You request for the following endpoints:
            - Top 5 barrios con mas viajes en los ultimos 10 dias (ordenado de mayor a menor)
            - Top 5 barrios con menos viajes en los ultimos 10 dias (ordenado de mayor a menor)
            - Predicción de concentraciones de CO para la ciudad de Manhattan en una determinada fecha futura
            - Consultar por un barrio en particular y ver que porcentaje de viajes le corresponde a cada tipo de transporte
            - Prediccion de cantidad de viajes para un tipo de transporte en especifico
            - Promedio de concentraciones de CO por barrio
    '''
    return message

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
    if isinstance(zone,int):

@app.get('/zones/top-{n}'):
def top5_zones(n):
    query = '''
        SELECT 
    '''




# Ruta para la consulta de la cantidad de viajes por categoría
@app.get('/cantidad_viajes/{categoria}')
def cantidad_taxis_fecha(categoria):

    table_name = f'{categoria}_taxis'

    # Especifica la referencia a la tabla que deseas visualizar
    table_ref = client.dataset(dataset_name).table(table_name)
    table = client.get_table(table_ref)

    query = f"""
        SELECT COUNT(pickup_datetime)
        FROM `{project_name}.{dataset_name}.{table_name}`
        LIMIT 1;
    """

    query_job = client.query(query)
    results = query_job.result()
    for row in results:
        resultado = row[0]

    data_json = {
        'mensaje': resultado
    }

    json_str = json.dumps(data_json, indent=4, default=str)
    return Response(content=json_str, media_type='application/json')

# Ruta para la página de inicio
@app.get('/')
def home():
    return {'mensaje': 'Bienvenido a la API para consultar información sobre los taxis de la ciudad de Nueva York.'}
