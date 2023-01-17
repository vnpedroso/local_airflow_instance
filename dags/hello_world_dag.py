from airflow import DAG
from airflow.operators.python import PythonOperator
import datetime
import pendulum 

def helloWorld():
	print("Hello World!")

with DAG(
	dag_id="hello_world_dag",
	start_date=pendulum.datetime(2023,1,1,tz="UTC"),
	catchup=False,
	dagrun_timeout=datetime.timedelta(minutes=30),
	tags=['example','hello_world']) as dag:

	task1 = PythonOperator(
		task_id="hello_world_task",
		python_callable=helloWorld)

task1