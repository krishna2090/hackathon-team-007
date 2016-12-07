"""Main Entrypoint for the Application"""

import logging
import json
import base64

from flask import Flask, request
from flask import jsonify

import notebook
import utility


app = Flask(__name__)


@app.route('/api/status')
def status():
    """hello world"""
    {
  "insert": true,
  "fetch": true,
  "delete": true,
  "list": true
}
    return 'Hello World!'

@app.route('/api/capitals')
def capitals():
    capitals = [
        {
            "id": 0,
            "country": "string",
            "name": "string",
            "location": {
            "latitude": 0,
            "longitude": 0
            },
            "countryCode": "string",
            "continent": "string"
        }]

    return json.dumps(capitals)

@app.route('/api/capitals/<id>', methods=['GET', 'PUT', 'DELETE'])
def capitalsid(id):
    if request.method == 'GET':
        return id
    if request.method == 'POST':
        return id

@app.errorhandler(500)
def server_error(err):
    """Error handler"""
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(err), 500


if __name__ == '__main__':
    # Used for running locally
    app.run(host='127.0.0.1', port=8080, debug=True)
