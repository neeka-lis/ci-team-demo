from airflow.sdk import dag
from datetime import datetime, timedelta

from packages.infra import tasks
from library.custom_logger import Logger


logger = Logger().get_logger()
