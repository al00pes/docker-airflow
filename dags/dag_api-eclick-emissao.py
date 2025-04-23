from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
#from azure.storage.blob import BlobServiceClient
import credenciais_eclick
from airflow.utils.trigger_rule import TriggerRule
from datetime import datetime, timedelta
import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
from openpyxl import Workbook


    
#inicio das função (TASK)

def acesso_url():
    
    # URL do endpoint OData
    odata_url = "https://rpeotta.e-clic.net/bi/Emissoes"

    # Fazendo a requisição com autenticação
    response = requests.get(odata_url, auth=HTTPBasicAuth(credenciais_eclick.login, credenciais_eclick.senha))

    # Verifica se deu certo
    if response.status_code == 200:
        dados_json = response.json()
    
        # Caso os dados estejam no formato OData padrão
        resultados = dados_json.get("value", [])

        # Transforma em DataFrame para facilitar o tratamento
        df_documentos = pd.DataFrame(resultados)
    else:
        print(f"Erro {response.status_code}: {response.text}")

    #Salvando o relatório na rede 
    df_documentos.to_excel(r'/opt/airflow/dados/01. LD e CR/0000 - BASE DE DADOS/relatorio_emissao_airflow.xlsx',index=False)

   

# Definindo os argumentos da DAG

default_args = {
    'owner':'arthur.lopes',
    'depends_on_past': False,
    'retris':1,
    'retry_delay': timedelta(minutes=0.5),
    'email_on_failure': False,
    'email_on_retry': False,
}

with DAG(
    'api-eclick-ETL-emissao',
    default_args=default_args,
    description='Dag - ELT do relatorio de emissoes dos documentos eclick',
    schedule_interval='0 17 * * *', #Executa todos os dias
    start_date=datetime(2025, 1, 1),
    catchup=False
) as dag:
    
    acesso_api = PythonOperator(
        task_id='api-eclick',
        python_callable=acesso_url,
        trigger_rule='all_done'
    )

   

acesso_api