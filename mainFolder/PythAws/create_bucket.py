import sys
import boto3
from botocore.client import Config,ClientError
from boto3 import client
#b_name=input("enter name of bucket")


s3 = boto3.resource('s3',aws_access_key_id='AKIAJHWO2QI4BBQS6Q2A',
            aws_secret_access_key='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',
            config=Config(signature_version='s3v4'))

def bucket_create():                                             #1
        try:
            b_name = input("enter name of bucket")
            s3.create_bucket(Bucket=b_name, CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
            print("bucket created")
        except BaseException as e:
                print(e)

def push_file():
        try:
            b_name = input("enter name of bucket")
            local_files=input("enter file name you want to upload")
            data = open(local_files, 'rb')
            s3_filename=input("enter changed name file")
            s3.Bucket(b_name).put_object(Key=s3_filename, Body=data)
            print(s3_filename,"file uploaded")

        except BaseException as e:
                print(e)

def push_files():                                               #2
        n=int(input("enter no. of file you want to upload "))
        for i in range(n):
                push_file()

def delete_bucket():                                        #4
    try:
        nam=input("enter name of bucket u want to delete")
        bucket=s3.Bucket(nam)
        bucket.delete()
        print("bucket deleted")
    except BaseException as e:
        print(e)


def delete_Bucket_files():                                    #6
    try:
        nam = input("enter name of bucket u want to delete")
        #client=boto3.client('s3')
        #client.delete_object(Bucket=nam,Key="forets.jpeg")
        s3.get

        print("files deleted")
    except BaseException as e:
        print(e)


def list_Bucket_files():                               #5
    try:
        nam = input("enter name of bucket to show files")
        conn=client('s3')
        for key in conn.list_objects(Bucket=nam)['Contents']:
            print(key['Key'])
    except BaseException as e:
        print(e)



def list_bucket():                                 #3 list of bucket
    try:
        bucket_list = [bucket.name for bucket in s3.buckets.all()]
        print(len(bucket_list))
        print(bucket_list)
    except BaseException as e:
        print(e)

while True:
    try:
        print(" press 1 for  create bucket")
        print(" press 2 for push files")
        print(" press 3 for list of bucket")
        print("press 4 delete bucket")
        print("press 5 list of bucket files")
        print("press 6 delete bucket files")
        print("press 7 to exit")

        alpha = int(input("enter your choice"))

        opt={1:bucket_create,
             2:push_files,
             3: list_bucket,
             4:delete_bucket,
             5:list_Bucket_files,
             6:delete_Bucket_files,    #check it
             7:exit
             }
        opt[alpha]()
    except BaseException as e:
        print(e)


