import requests
from flask import Flask
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

@app.route('/createJira', methods=['POST'])

def createJira():

    url = ""

    API_TOKEN = ""

    auth = HTTPBasicAuth("", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
            "fields": {
            "description": {
                "content": [
                    {
                        "content": [
                            {
                                "text": "Order entry fails when selecting supplier.",
                                "type": "text"
                            }
                        ],
                        "type": "paragraph"
                        }
                    ],
                "type": "doc",
                "version": 1
            },
            "project": {
            "key": "KAN"
            },
            "issuetype": {
                "id": "10005"
            },
            "summary": "Feature request: Slider required",
        },
        "update": {}
        } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)
