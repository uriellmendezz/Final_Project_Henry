# Importa las librerías necesarias
from google.cloud import bigquery
import json
import os
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Configura las credenciales de Google Cloud
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'google_credentials.json'
client = bigquery.Client()
project_name = 'nyc-taxis-project'
dataset_name = 'new_york_transport_project'

# Crea una instancia de FastAPI
app = FastAPI()

# Monta los archivos estáticos y configura las plantillas Jinja2
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Define la ruta de inicio que servirá la página HTML
@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

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
