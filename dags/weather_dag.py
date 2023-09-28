import json
from datetime import datetime
from airflow.models import DAG
from airflow.providers.http.sensors.http import HttpSensor
from airflow .providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator

with DAG( 
    dag_id='weather_dag', 
    schedule_interval='@daily', 
    start_date=datetime(2022, 3, 1),
    catchup=False
) as dag:
    
    task_is_api_active = HttpSensor (
        task_id='is_api_active',
        http_conn_id='weather_api',
        endpoint='posts/'
    )