import logging
import boto3
from botocore.exceptions import ClientError
import os

# Prerequisites:
# pip install boto3
# Export the below environment variables with coreect value
# export AWS_ACCESS_KEY_ID=XXXXXXXXXXX
# export AWS_SECRET_ACCESS_KEY=XXXXXXXXXXX
# If do not have creds then follow the steps here - https://docs.aws.amazon.com/keyspaces/latest/devguide/access.credentials.html

def uploadFile(fileName, bucket, objectName=None):
    """Upload a file to an S3 bucket

    :param fileName: File to upload
    :param bucket: Bucket to upload to
    :param objectName: S3 object name. If not specified then fileName is used
    :return: True if file was uploaded, else False
    """

    # If S3 objectName was not specified, use fileName
    if objectName is None:
        objectName = os.path.basename(fileName)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(fileName, bucket, objectName)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def downloadFile(objectName, bucket, fileName=None):
    """Download a file from S3 bucket

    :param fileName: fileName to save as. If not specified then objectName is used
    :param bucket: Bucket to download from
    :param objectName: S3 object name
    :return: True if file was uploaded, else False
    """

    # If S3 objectName was not specified, use fileName
    if fileName is None:
        fileName = os.path.basename(objectName)
    
    # Download the file
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket, objectName, fileName)
    except ClientError as e:
        logging.error(e)
        return False
    return True

if __name__ == "__main__":
    uploadFile("local/path/to/file", "your-bucket-name", "s3-object-name")
    downloadFile("s3-object-name", "your-bucket-name", "local/path/to/file")