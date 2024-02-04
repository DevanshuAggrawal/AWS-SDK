import boto3
 
def get_lambda_functions():
    client = boto3.client('lambda')
    response = client.list_functions()
    return response['Functions']
 
def lambda_handler(event, context):
    lambda_functions = get_lambda_functions()
 
    for function in lambda_functions:
        function_name = function['FunctionName']
        last_modified_timestamp = function['LastModified']
        version = function['Version']
 
        print(f"Function Name: {function_name}")
        print(f"Last Modified Timestamp: {last_modified_timestamp}")
        print(f"Version: {version}")
        print("-" * 30)
 
    return {
        'statusCode': 200,
        'body': 'Lambda information retrieved successfully!'
    }