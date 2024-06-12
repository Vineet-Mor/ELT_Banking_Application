import os
from google.cloud import storage
import requests

def extract_data():
    # Example API call to fetch banking data
    response = requests.get("https://api.bankingdata.com/data")
    data = response.text
    
    # Upload data to GCS
    bucket_name = 'bankingvm'
    file_name = 'extracted_data.json'
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    blob.upload_from_string(data)
    
    print('Data extracted and uploaded to GCS')

if __name__ == "__main__":
    extract_data()
