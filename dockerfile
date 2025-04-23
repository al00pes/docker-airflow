FROM apache/airflow:2.10.5-python3.10

USER root

# Copia o requirements.txt com bibliotecas Python
COPY requirements.txt /requirements.txt

# Agora volta a ser o usuário airflow
USER airflow

# Instala os pacotes Python como usuário airflow (sem aviso)
RUN pip install --no-cache-dir -r /requirements.txt