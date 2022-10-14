# import the libraries

from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

#defining DAG arguments
default_args = {
    'owner': 'Vinicius da Silva Vale',
    'start_date': days_ago(0),
    'email': ['viniciusdvale@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# define the DAG
dag = DAG(
    dag_id='ETL_tool_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval='@daily',
)

# define the tasks

# Task to unzip data
unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='tar zxvf /home/project/airflow/dags/finalassignment/tolldata.tgz -C /home/project/airflow/dags/finalassignment',
    dag=dag,
)

# Task to extract data from csv file
extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command='cut -d, -f1,2,3,4,6 /home/project/airflow/dags/finalassignment/vehicle-data.csv > /home/project/airflow/dags/finalassignment/csv_data.csv',
    dag=dag,
)

# Task to extract data from tsv file
extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command='cut -f 5,6,7 /home/project/airflow/dags/finalassignment/tollplaza-data.tsv > /home/project/airflow/dags/finalassignment/tsv_data.csv',
    dag=dag,
)

# Task to extract data from fixed width file
extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command='cut -c59-68 /home/project/airflow/dags/finalassignment/payment-data.txt > /home/project/airflow/dags/finalassignment/fixed_width_data.csv',
    dag=dag,
)

# Task to consolidate data
consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command='paste -d, <(cut -d, -f1,2,3,4 /home/project/airflow/dags/finalassignment/csv_data.csv) <(cut -f 1,2,3 /home/project/airflow/dags/finalassignment/tsv_data.csv | sed "s/\t/,/g" | tr -d "\t\r") <(cut -c1-10 /home/project/airflow/dags/finalassignment/fixed_width_data.csv | sed "s/ /,/") > /home/project/airflow/dags/finalassignment/extracted_data.csv',
    dag=dag,
)

# Task to transform data
transform_data = BashOperator(
    task_id='transform_data',
    bash_command='paste -d, <(cut -d, -f1,2,3 home/project/airflow/dags/finalassignment/extracted_data.csv) <(cut -d, -f4 home/project/airflow/dags/finalassignment/extracted_data.csv | tr "[a-z]" "[A-Z]") <(cut -d, -f5,6,7,8,9 home/project/airflow/dags/finalassignment/extracted_data.csv) > /home/project/airflow/dags/finalassignment/staging/transformed_data.csv',
    dag=dag,
)

# Task pipepline
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data
