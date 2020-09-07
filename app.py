from chalice import Chalice
import boto3
app = Chalice(app_name='control-ec2')


@app.authorizer(ttl_seconds=30)
def my_auth(auth_request):
        # Validate auth_request.token, and then:
            return AuthResponse(routes=['/'], principal_id='arn:aws:ec2:us-west-2:701203368262:root/*')

# Create route to start instance
@app.route('/start/{name}', authorizer=my_auth)
def instance(name):
    instances = [name]
    ec2 = boto3.client('ec2', region_name='us-west-2')
    ec2.start_instances(InstanceIds=instances)
    return {'InstanceId started': name}


# Create route to stop instance
@app.route('/stop/{name}', authorizer=my_auth)
def instance_stop(name):
    instances = [name]
    ec2 = boto3.client('ec2', region_name='us-west-2')
    ec2.stop_instances(InstanceIds=instances)
    return {'InstanceId stopped': name}
