import requests
import json
from datetime import datetime

API_KEY = ""


def transform_bill_data(bill):
    """Transform a single bill dict to underscore_case and flatten nested data."""
    transformed_data = {
        "congress": bill["congress"],
        "latest_action_date": bill["latestAction"]["actionDate"],
        "latest_action_text": bill["latestAction"]["text"],
        "number": bill["number"],
        "origin_chamber": bill["originChamber"],
        "origin_chamber_code": bill["originChamberCode"],
        "title": bill["title"],
        "type": bill["type"],
        "update_date": bill["updateDate"],
        "update_date_including_text": datetime.strftime(datetime.strptime(bill["updateDateIncludingText"],'%Y-%m-%dT%H:%M:%SZ'), '%Y-%m-%dT%H:%M:%S'),
        "url": bill["url"]
    }

    return transformed_data


def fetch_bills(api_key):
    """Return 1000 bills from Congress API in chunks of 250."""
    url = f"https://api.congress.gov/v3/bill?api_key={api_key}"
    offset = 0
    data = []

    while offset < 1000:
        response = requests.get(url, {"offset": offset, "limit": 250})

        [data.append(transform_bill_data(bill)) for bill in response.json()["bills"]]

        offset += 250

    return data

def write_to_file(data):
    """Write data to a json file called bills.json."""
    with open("bills.json", "w") as file:
        json_data = json.dumps(data, indent=4)

        file.write(json_data)


if __name__ == "__main__":
    api_key = API_KEY

    data = fetch_bills(api_key)
    write_to_file(data)




