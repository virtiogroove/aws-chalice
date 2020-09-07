import requests
from requests_aws_sign import AWSV4Sign
from boto3 import session

session = session.Session()
credentials = session.get_credentials()
region = session.region_name
service = 'execute-api'

url = "https://xxxxxxxxx.execute-api.us-west-2.amazonaws.com/api/[start/stop]/{name}"
auth = AWSV4Sign(credentials, region, service)
response = requests.get(url, auth=auth)

print(response.text)
