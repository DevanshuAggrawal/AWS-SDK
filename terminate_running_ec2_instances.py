import boto3
import json

aws_management_console = boto3.session.Session(profile_name="Devanshu")
ec2_console = aws_management_console.client('ec2')

response = ec2_console.describe_instance_status()
print(response)

print(type(response))

newlist=[]

for i in response['InstanceStatuses']:
    newlist.append(i['InstanceId'])
    print("Instance ID Created is :{}".format(i['InstanceId']))

response = ec2_console.terminate_instances(
    InstanceIds=(newlist)
)

print(response)
print(response)
