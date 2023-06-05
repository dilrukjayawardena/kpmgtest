import requests
import google.auth.transport.requests
import google.oauth2.id_token
import json


def make_authorized_get_request(endpoint, audience,data):
    """
    make_authorized_get_request makes a GET request to the specified HTTP endpoint
    by authenticating with the ID token obtained from the google-auth client library
    using the specified audience value.
    """
    payload=json.dumps(data)
    
    auth_req = google.auth.transport.requests.Request()
    id_token = google.oauth2.id_token.fetch_id_token(auth_req, audience)

    headers={
        'authorization':f"bearer {id_token}",
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", endpoint, data=payload, headers=headers)
    return response.text