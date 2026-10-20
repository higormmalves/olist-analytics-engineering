from pathlib import Path
from google.cloud import bigquery

PROJECT_ID = 'olist-analytics-engineering'
LOCATION = 'US'
TABLE_ID = f"{PROJECT_ID}.olist-raw.orders"

PROJECT_ROOT = Path(__file__).resolve().parent.parent

SOURCE_FILE = PROJECT_ROOT / "data" / "raw" / "olist_orders_dataset.csv"

def load_orders():
    client = bigquery.Client(
                project=PROJECT_ID,
                location=LOCATION)
    

    job_config = bigquery.LoadJobConfig(
                    source_format=bigquery.SourceFormat.CSV, 
                    skip_leading_rows=1, 
                    autodetect=False, 
                    schema=[
                            bigquery.SchemaField("order_id", "STRING"),
                            bigquery.SchemaField("customer_id", "STRING"),
                            bigquery.SchemaField("order_status", "STRING"),
                            bigquery.SchemaField("order_purchase_timestamp", "STRING"),
                            bigquery.SchemaField("order_approved_at", "STRING"),
                            bigquery.SchemaField("order_delivered_carrier_date", "STRING"),
                            bigquery.SchemaField("order_delivered_customer_date", "STRING"),
                            bigquery.SchemaField("order_estimated_delivery_date", "STRING")
                            ], 
                    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
                )
                