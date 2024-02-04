import boto3

aws_management_console = boto3.session.Session(profile_name="Devanshu")
ec2_console = aws_management_console.client('ec2')

response = ec2_console.run_instances(
    ImageId='ami-0d63de463e6604d0a',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1
)

print(response)