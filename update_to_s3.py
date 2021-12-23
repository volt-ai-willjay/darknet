import os
import boto3
from datetime import datetime
import argparse
import requests

bucket = 'volt-models'
now = datetime.utcnow().strftime('%Y-%m-%d-%H:%M:%S')
key = f'{now}/'


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--source", required=True,
                    help="please specify source dir for training result dir")

args = vars(parser.parse_args())


def convert_darknet(bucket, key):
    url = 'https://https://data.api.volt.ai/convert-darknet/'
    body =  {
                'input_bucket': bucket,
                'input_dir': key
            }
    r = requests.post(url, data=body)
    print("== convert darknet api: ", r.status_code, " ==")



if not os.path.isdir(args["source"]):
    print("please specify source dir for training result dir")
else:
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
    )
    try:
        for root, dirs, files in os.walk(args["source"]):
            for file in files:
                file_path = os.path.join(root, file)
                s3_key = key+file
                s3.upload_file(file_path, bucket, s3_key)
        print(f"== finishing uploading files to {bucket}/{key} ==")
        convert_darknet(bucket=bucket, key=f'{now}')
    except Exception as e:
        print("FAILED: ", e)







