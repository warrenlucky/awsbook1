import boto3
def lambda_handler(event, context):
    s3 = boto3.resource('s3', region_name='ap-east-1')
    s3.create_bucket(Bucket='mys3bucket-123456789',CreateBucketConfiguration={
        'LocationConstraint': 'ap-east-1'
    })
    content="version 1"
    s3.Object('mys3bucket-123456789', 'version1.txt').put(Body=content)
    print("ok")