import boto3

aws_management_console = boto3.session.Session(profile_name="Devanshu")
ec2_console = aws_management_console.client('ec2')

#Listing already running EC2 instance
response = ec2_console.describe_instance_status()
print(response)