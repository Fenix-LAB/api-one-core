from google.cloud import bigquery
from config.config import config
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = config.BQ_JSON_CREDENTIALS

def get_db_session():
    """
    Get a session to the BigQuery database

    Returns:
    bigquery.client.Client: A session to the BigQuery database
    """
    client = bigquery.Client()
    try:
        yield client
    finally:
        client.close()
