from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
from datetime import timedelta
import pandas as pd

default_args = {
    'start_date': days_ago(1),
}

@dag(
    schedule_interval='@daily', default_args=default_args, catchup=False,
    description="A simple example DAG", tags=['EDX', 'IBM'])
def edx_ibm_ETL_Server_Access_Log_Processing():

    @task
    def download():
        import requests
        url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/web-server-access-log.txt'
        response = requests.get(url)
        open("web-server-access-log.txt", "wb").write(response.content)
    
    @task
    def extract():
        df = pd.read_csv("web-server-access-log.txt", header='infer', delimiter="#")
        df = df[['timestamp','visitorid']]
        df.to_csv("extract.csv", index=False)

    @task
    def transform():
        df = pd.read_csv("extract.csv", header='infer')
        df['visitorid'] = df['visitorid'].str.upper()
        df.to_csv("transform.csv", index=False)

    @task
    def load():
        df = pd.read_csv("transform.csv", header='infer')
        df.to_csv("web-server-access-log.csv.zip", 
           index=False, 
           compression="zip")

    download()>>extract()>>transform()>>load()
dag = edx_ibm_ETL_Server_Access_Log_Processing()