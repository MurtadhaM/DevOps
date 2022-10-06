# HTTP FLASK SERVER
from ast import arg
from flask import Flask, request, jsonify

app = Flask(__name__)

# set the environment variable
import os
import sys

os.environ['FLASK_APP'] = 'flask_server'
os.environ['FLASK_ENV'] = 'development'
@app.route("/")
def hello():
    return "Hello World!"



if __name__ == "__main__":
    # get the parameters from the command line
    args = sys.argv[1:]
    if len(args) > 0:
        port = int(args[0])
        app.run(port=port, debug=True)
    else:
        port = 8080
        app.run(port=port, debug=True)
        print("docker run -p 8080:8080 mmarzouq/flask_server:latest 8080")
    print("server is shutting down")
    
