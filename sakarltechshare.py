import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_s3(local_file, bucket_name, s3_file):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(local_file, bucket_name, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

def download_from_s3(bucket_name, s3_file, local_file):
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket_name, s3_file, local_file)
        print("Download Successful")
        return True
    except FileNotFoundError:
        print("The file was not found on S3")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

