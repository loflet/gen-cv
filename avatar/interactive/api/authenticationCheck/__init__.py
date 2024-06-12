import logging
import requests
import json
import os

import azure.functions as func

loginUser = os.getenv("LOGIN_USER")
loginPass = os.getenv("LOGIN_PASS")

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        # Parse request body
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            "Invalid input",
            status_code=400
        )

    username = req_body.get('username')
    password = req_body.get('password')

    logging.info(f"Username entered: {username}; Password: {password} ; loginUser is: {loginUser}; loginPass is: {loginPass}")

    if not username or not password:
        return func.HttpResponse(
            "Please pass both username and password in the request body",
            status_code=400
        )

    if username == loginUser and password == loginPass:
        return func.HttpResponse(
            json.dumps({"status": "success"}),
            status_code=200,
            mimetype="application/json"
        )
    else:
        return func.HttpResponse(
            json.dumps({"status": "failure"}),
            status_code=401,
            mimetype="application/json"
        )