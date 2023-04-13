import io
import json
import pandas as pd
from google.cloud import storage #pip3 install google-cloud-storage

# HOW TO GET JSON_CREDENTIALS: https://www.skytowner.com/explore/guide_on_creating_a_service_account_and_private_keys_in_google_cloud_platform

df = pd.DataFrame(
    {'name': ['Thanh', 'Ninh'], 'age': [16, 21]}
)

json_credentials_path = 'JSON_CREDENTIALS_PATH'
### WRITE ###
# create client
client = storage.Client.from_service_account_json(json_credentials_path=json_credentials_path)
# specify bucket
bucket = client.bucket('BUCKET_NAME')
# bucket = client.create_bucket('test-v2-bucket-skytowner')

# The name assigned to the CSV file on GCS. Upload file using blob
blob = bucket.blob('abc/xyz/<file_name>/file.csv')
blob.upload_from_string(df.to_csv(index=False), 'text/csv')

# blob = bucket.blob('abc/xyz/<file_name>.parquet')
# blob.upload_from_string(df.to_parquet(index=False), 'application/octet-stream')


### LOAD ###
b = blob.download_as_bytes()
load_file = io.BytesIO(b)
df_load = pd.read_parquet(load_file)
print(df_load)