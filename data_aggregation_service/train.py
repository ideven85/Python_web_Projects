from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

def train():
    import train_mlflow  # your script

with DAG("ml_pipeline", start_date=datetime(2026,7,8), schedule="@daily") as dag:
    train_task = PythonOperator(
        task_id="train_model",
        python_callable=train
    )