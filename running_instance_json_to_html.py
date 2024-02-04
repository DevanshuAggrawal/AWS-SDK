import boto3
import json
from json2html import *



aws_management_console = boto3.session.Session(profile_name="Devanshu")
ec2_console = aws_management_console.client('ec2')


#Creating new instance Id
response = ec2_console.run_instances(
    ImageId='ami-0d63de463e6604d0a',
    InstanceType='t2.micro',
    MaxCount=2,
    MinCount=2
)

print(response)

#Listing already running EC2 instance
response = ec2_console.describe_instance_status()
print(response)






