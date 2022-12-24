import boto3, os
from dotenv import load_dotenv
load_dotenv()

s3 = boto3.resource(
    's3',
    region_name=os.getenv("REGION_NAME"),
    aws_secret_access_key=os.getenv("SECRET_ACCESS_KEY"),
    aws_access_key_id=os.getenv("ACCESS_KEY_ID"),
    endpoint_url=os.getenv("ENDPOINT_URL")
)

for bucket in s3.buckets.all():
    print(bucket.name)

s3.meta.client.upload_file('index.html',os.getenv("BUCKET_NAME"), 'index.html')

#cdn access = https://cdn.comnetbe.my.id