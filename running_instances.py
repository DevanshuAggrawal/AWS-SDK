import boto3
import webbrowser
from collections import _OrderedDictItemsView
from ipaddress import collapse_addresses

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
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML Table Example</title>
</head>
<body>

    <!-- Navigation with Hyperlinks -->
    <h2>Navigation</h2>
    <ul>
        <li><a href="#page1">Page 1</a></li>
        <li><a href="#page2">Page 2</a></li>
        <li><a href="#page3">Page 3</a></li>
        <!-- Add more pages as needed -->
    </ul>

    <!-- Table Format -->
    <h2>Table Format</h2>
    <table border="1" cellpadding="10">
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Age</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>{value}</td>
                <td>{value}</td>
                <td>{value}</td>
            </tr>
            <tr>
                <td>{value}</td>
                <td>{value}</td>
                <td>{value}</td>
            </tr>
            <!-- Add more rows as needed -->
        </tbody>
    </table>

</body>
</html>
    '''
    print(message)

    f.write(message)

f.close()

webbrowser.open_new_tab("sample.html")

