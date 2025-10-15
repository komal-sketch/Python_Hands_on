'''
Script to take bacup from local to AWS S3
boto3 : used to do AWS tasks using Python
'''
# show all buckets
import boto3

s3 = boto3.resource("s3")
def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)


show_buckets(s3)

# Create bucket

import boto3
from botocore.exceptions import ClientError

def create_bucket(s3_client, bucket_name: str, region: str) -> None:
    """
    Create an S3 bucket. For us-east-1, omit CreateBucketConfiguration.
    """
    try:
        if region == "us-east-1":
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={"LocationConstraint": region},
            )
        print(f"[OK] Bucket created: {bucket_name} in {region}")
    except ClientError as e:
        print(f"[ERR] create_bucket failed: {e}")
        raise

def upload_backup(s3_client, file_path: str, bucket_name: str, key_name: str) -> None:
    """
    Upload a local file to S3 as a specific key.
    """
    try:
        # upload_file handles streaming and multipart for large files
        s3_client.upload_file(file_path, bucket_name, key_name)
        print(f"[OK] Uploaded {file_path} -> s3://{bucket_name}/{key_name}")
    except ClientError as e:
        print(f"[ERR] upload_backup failed: {e}")
        raise
    except FileNotFoundError:
        print(f"[ERR] Local file not found: {file_path}")
        raise

def show_buckets(s3_client) -> None:
    """
    Print all buckets in the account.
    """
    try:
        resp = s3_client.list_buckets()
        names = [b["Name"] for b in resp.get("Buckets", [])]
        if not names:
            print("[i] No buckets found.")
        else:
            print("[i] Buckets:")
            for name in names:
                print(f"  - {name}")
    except ClientError as e:
        print(f"[ERR] list_buckets failed: {e}")
        raise

if __name__ == "__main__":
    # Initialize once; relies on your AWS credentials (env vars, shared creds, or role)
    region = "us-east-1"   # change as needed
    bucket_name = "your-unique-bucket-name-here-12345"
    s3 = boto3.client("s3", region_name=region)

    create_bucket(s3, bucket_name, region)
    show_buckets(s3)

    # Example upload
    # upload_backup(s3, "backup.sql.gz", bucket_name, "db/backups/backup-2025-10-15.sql.gz")


