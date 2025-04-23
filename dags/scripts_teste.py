'''from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from selenium import webdriver
import time
import pandas as pd
import credenciais_eclick
from bs4 import BeautifulSoup
import os
import shutil
import warnings
warnings.filterwarnings('ignore')
import aspose.tasks as tsk
 
 #Definindo os argumentos do da DAG

default_args={
    'owner': 'arthur.lopes', #criador da dag
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),

}

#Iniciando o selenium
def carregando_arquivo():
  
  path_file = '/opt/airflow/dados/04.BASE_DE_DADOS_AMBIENTE_TESTE_VALE/00005.csv'               
  df = pd.read_csv(path_file)
  df.to_csv('/opt/airflow/dags/00005.csv',index=False)
    

#Criação da DAG

with DAG(
    dag_id='extracao_tabela_project_teste',
    default_args=default_args,
    description='Extração_da_tabela_do_project',
    schedule_interval='0 17 * * *', #Executa todos os dias as 17h
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:


    task_carregando_dados = PythonOperator(
        task_id = 'Carregando_arquivo',
        python_callable= carregando_arquivo,
    )

   
task_carregando_dados '''

    




