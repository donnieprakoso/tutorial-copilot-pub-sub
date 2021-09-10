from flask import Flask, request
import boto3
import os
import json
import random, string

def generate_random(char_length):
   characters = string.ascii_lowercase
   return ''.join(random.choice(characters) for i in range(char_length))

AWS_REGION='ap-southeast-1'
TOPIC_ARNS = json.loads(os.getenv("COPILOT_SNS_TOPIC_ARNS"))
client = boto3.client('sns', region_name=AWS_REGION)
app = Flask(__name__)

@app.route('/')
def hello_world():
    ping_message = "Pong {}".format(generate_random(5))
    response = client.publish(
        TopicArn=TOPIC_ARNS["ping"],
        Message=ping_message
            )
    return "Message sent: {}\n".format(ping_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
