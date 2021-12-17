import os
import boto3
import argparse

bucket = 'volt-models'
key = 'yolov4-tiny/'

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--source", required=True,
                    help="please specify source dir for training result")

args = vars(parser.parse_args())


s3 = boto3.client(
    's3',
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
)

key += args["source"]

try:
    s3.upload_file(filename=args["source"], bucket=bucket, key=key)
    print("== upload file completed ==")

except Exception as e:
    print("FAILED: ", e)
