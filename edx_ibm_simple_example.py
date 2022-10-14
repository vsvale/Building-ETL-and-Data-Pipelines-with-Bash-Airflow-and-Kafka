from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args = {
#    'owner':'me',
    'start_date': days_ago(1),
 #   'retries':1,
 #   'retry_delay': timedelta(minutes=5)
}

@dag(
    schedule_interval='@daily', default_args=default_args, catchup=False,
    description="A simple example DAG", tags=['EDX', 'IBM'])
def edx_ibm_simple_example():

    @task
    def print_hello():
        print('Greetings.')

    @task
    def print_date():
        print("{{ ds }}")

    print_hello() >> print_date()
dag = edx_ibm_simple_example()