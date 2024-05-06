import boto3
def lambda_handler(event, context):
    # Define EC2 Params
    instance_params = {
        'ImageId': ' ami-0f4dfdbd0b33c2e4c', # AL2023 AMI ID
        'InstanceType': 't3.micro',  # Instance Type
        'KeyName': 'your-key-pair',  # Instance KeyPair Name
        'MinCount': 1,  # Min Instance Count
        'MaxCount': 1,  # Max Instance Count
    }
    # Create EC2 Instance
    ec2_client = boto3.client('ec2', region_name='your-region')  #  AWS AZ
    response = ec2_client.run_instances(**instance_params)
    # Get EC2 Instance ID
    instance_id = response['Instances'][0]['InstanceId']
    return {
        'statusCode': 200,
        'body': f'EC2 instance {instance_id} has been successfully launched.'
    }