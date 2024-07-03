# m-labs skill assessment

## Setup
1. Create a virtual environment and activate it
2. `pip install -r requirements.txt`

## Usage

### Extract and Transform data
1. Get an API key from https://api.congress.gov/sign-up/ and set the `API_KEY` variable.
2. `python fetch_bills.py`
3. A file called `bills.json` will be created.

### Create table
1. Install (gcloud CLI)[https://cloud.google.com/sdk/docs/install] and set your application default credentials using gcloud auth application-default login. 
2. `python create_bills_table.py`
3. A table called `bills` with the appropriate schema should be created in bigquery

### Load data
1. `python load_to_bigquery.py`
2. The data from `bills.json` should be loaded to the `bills` table in bigquery. If it fails, check the `Job History` console in bigquery for errors.

## Improvements 
To productionalize this little ETL pipeline, I'd need to find more information about how often this API is updated, and figure out where within the dataset to stop ingesting to prevent duplicates. There doesn't seem to be a primary key right now, so we would possibly have to construct one based off of the bill type and the bill number, plus a third factor accounting for the fact that the bill numbers reset every several years. I'd like to containerize this and run it daily using github actions, or airflow. I'd pass the API_KEY in as a secret. I'd also define the data schema centrally somewhere, to avoid having it written out in two different locations.

One of my queries had a CTE that signified whether the bill was sent to committee or not. I'd like to add more columns about each bill based off of the title and action text, for easier semantic analysis. The CASE WHEN separator I used is likely a flawed way to segment the bills, so I'd want to do more experimenting to see what's an acceptable method of categorizing them. We could theoretically use some sort of text classification with sklearn or another NLP technique, but there are only so many congressional committees, so doing it by hand would probably ultimately be more accurate.