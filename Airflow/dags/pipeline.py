from datetime import datetime

from airflow import DAG
from airflow.providers.dbt.cloud.operators.dbt import DbtCloudRunJobOperator


with DAG(
    dag_id="credit_risk_analysis_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["dbt", "databricks"],
) as dag:

    run_dbt_job = DbtCloudRunJobOperator(
        task_id="run_dbt_job",
        dbt_cloud_conn_id="credit_con",
        job_id=70506183139506,
        wait_for_termination=True,
    )