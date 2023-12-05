from airflow import DAG
from datetime import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

default_args = {
    "owner": "Vadym Urupa",
    "start_date": datetime(2023, 12, 5)
}