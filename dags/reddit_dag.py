from pipelines import reddit_pipeline, upload_s3_pipeline
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

default_args = {
    "owner": "Vadym Urupa",
    "start_date": datetime(2023, 12, 6)
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id="etl_data_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
    tags=["reddit", "etl", "pipeline"]
)

# Extraction from Reddit.

extract = PythonOperator(
        task_id = "reddit_extractor",
        python_callable=reddit_pipeline,
        op_kwargs = {
            "file_name": f"reddit_{file_postfix}",
            "subreddit": "data_engineering",
            "time_filter": "day",
            "limit": 100
        },
        dag=dag
)

upload_s3 = PythonOperator(
    task_id = "s3_upload",
    python_callable= upload_s3_pipeline,
    dag=dag
)