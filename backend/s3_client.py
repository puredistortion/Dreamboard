import os
import boto3
from dotenv import load_dotenv

load_dotenv()  # Only needed locally, harmless on Railway

s3 = boto3.client(
    "s3",
    region_name=os.environ.get("AWS_REGION"),
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
)

BUCKET = os.environ.get("S3_BUCKET")

def upload_file(file_path, key):
    s3.upload_file(file_path, BUCKET, key, ExtraArgs={'ACL':'public-read'})
    url = f"https://{BUCKET}.s3.amazonaws.com/{key}"
    return url
