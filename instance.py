import boto3
from flask import Flask

app = Flask(__name__)

service = boto3.resource("ec2", region_name = "ap-south-1")

@app.route("/instance")
def launch_instance():
    instance = service.create_instances(ImageId = "ami-0f918f7e67a3323f0", InstanceType = "t2.micro", MaxCount = 1, MinCount = 1)
    return "os launched"

app.run()