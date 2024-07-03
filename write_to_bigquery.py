import json
from google.cloud import bigquery

client = bigquery.Client()

def write_bills_to_bigquery():
    """Read data from a json file called bills.json and writes to bigquery bills table."""
    with open("bills.json", "r") as file:
        data = json.load(file)
        result = client.load_table_from_json(json_rows=data, destination="mlabs-incubator.skills_gong.bills")
    
    return result

if __name__ == "__main__":
    write_bills_to_bigquery()
