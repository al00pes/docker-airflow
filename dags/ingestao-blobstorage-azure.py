from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from azure.storage.blob import BlobServiceClient
import credenciais
from airflow.utils.trigger_rule import TriggerRule
from datetime import datetime, timedelta

# Função para fazer o upload no Azure Blob Storage
def upload_to_blob(account_name, account_key, container_name, local_file_path, blob_name):
    try:
        # Conexão com o Blob Storage
        connect_str = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net"
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        # Upload do arquivo
        with open(local_file_path, "rb") as data:
            blob_client.upload_blob(data=data, overwrite=True)

        print(f"Arquivo '{blob_name}' enviado com sucesso para o container '{container_name}'.")

    except Exception as e:
        print(f"Erro ao enviar o arquivo '{blob_name}': {e}")
        raise e

# TASKS para a DAG
def upload_files_brasfels():
    account_name = credenciais.account_name
    account_key = credenciais.account_key
    container_name = 'brasfels-2446'

    arquivos = [
        {"local_path": r"/opt/airflow/dados/01. LD e CR/2446 - BRASFELS/01. LISTA DE DOCUMENTOS/LD-2446-PE-CAR-PLN-GER-001-R0.xlsx", 
         "blob_name": "LD-2446-PE-CAR-PLN-GRC-001-R0.xlsx"},
        {"local_path": r"/opt/airflow/dados/01. LD e CR/2446 - BRASFELS/02. CRONOGRAMA/CS-2446-PE-CAR-PLN-GER-001-R0.xlsx", 
         "blob_name": "CS-2446-PE-CAR-PLN-GRC-001-R0.xlsx"},
        {"local_path": r"/opt/airflow/dados/03. PLN_Operacional/01 - PLANEJAMENTO E CONTROLE/COORDENACAO/CONTROLES (POWER BI)/240124/BRASFELLS/faturamento_2446.xlsx", 
        "blob_name": "faturamento_2446.xlsx"},
        {"local_path":r"/opt/airflow/dados//03. PLN_Operacional/01 - PLANEJAMENTO E CONTROLE/COORDENACAO/PAR/2446 - BRASFELS/PAR_2446_BRASFELS_R0.xlsx" , 
         "blob_name": "PAR_2446_BRASFELS_R0.xlsx"}
    ]

    for arquivo in arquivos:
        upload_to_blob(
            account_name,
            account_key,
            container_name,
            arquivo["local_path"],
            arquivo["blob_name"]
        )


# Configuração da DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=0.5),
    'email_on_failure': False,
    'email_on_retry': False,
    
    
}

with DAG(
    'ingestao-blobstorage-azure',
    default_args=default_args,
    description='DAG para fazer upload de arquivos para o Azure Blob Storage',
    schedule_interval='0 17 * * *',  # Executa todos os dias 
    start_date=datetime(2025, 1, 1),
    catchup=False, # Executar tarefas passadas 

) as dag:

    upload_task_brasfels = PythonOperator( # Operador que executar codigo python
        task_id='ingestao_azure-2446',
        python_callable=upload_files_brasfels,
        trigger_rule='all_done' # nome da função
    )

 
    upload_task_brasfels 
    