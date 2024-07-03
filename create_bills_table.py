from google.cloud import bigquery

client = bigquery.Client()

table_id = "mlabs-incubator.skills_gong.bills"

schema = [
    bigquery.SchemaField("congress", "INT64"),
    bigquery.SchemaField("latest_action_date", "DATE"),
    bigquery.SchemaField("latest_action_text", "STRING"),
    bigquery.SchemaField("number", "INT64"),
    bigquery.SchemaField("origin_chamber", "STRING"),
    bigquery.SchemaField("origin_chamber_code", "STRING"),
    bigquery.SchemaField("title", "STRING"),
    bigquery.SchemaField("type", "STRING"),
    bigquery.SchemaField("update_date", "DATE"),
    bigquery.SchemaField("update_date_including_text", "DATETIME"),
    bigquery.SchemaField("url", "STRING")
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)
print(
    f"Created table {table.project}.{table.dataset_id}.{table.table_id}"
)