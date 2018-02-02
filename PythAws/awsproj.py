import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIAJHW'
ACCESS_SECRET_KEY = 'k/FDSKIB'
BUCKET_NAME = 'vinitnewbucket'

data = open('/home/bridgeit/Desktop/forest.jpeg', 'rb')

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)
s3.Bucket(BUCKET_NAME).put_object(Key='html file/forest.jpeg', Body=data)

print ("Done")
