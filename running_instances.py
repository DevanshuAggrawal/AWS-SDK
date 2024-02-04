import boto3
import webbrowser

aws_management_console = boto3.session.Session(profile_name="Devanshu")
ec2_console = aws_management_console.client('ec2')

response = ec2_console.describe_instance_status()
print(response)

newlist=[]
counter=0

f=open("sample.html","w")

for i in response['InstanceStatuses']:
    newlist.append(i['InstanceId'])
    
    print("Instance ID Created is :{}".format(i['InstanceId']))
    
    value=newlist[counter]
    
    print(value)
    
    counter=counter+1
    
    message=f'''
    <html>
    <head></head>
    <body><h1>{value}</h1></body>
    </html>
    '''
    print(message)

    f.write(message)

f.close()

webbrowser.open_new_tab("sample.html")

