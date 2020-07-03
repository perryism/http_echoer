from flask import Flask, request

import logging, sys
import argparse

parser = argparse.ArgumentParser(description="Echo")
parser.add_argument("--log", choices=["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], default="INFO",
                    help="Log level")
parser.add_argument("--port", type=int, default=5555, help="Port")

args = parser.parse_args()

app = Flask(__name__)

def dump_result():
    print(request.method)
    print(request.headers)
    print(request.get_data())
    print(request.url)

@app.route('/', methods=["GET", "POST", "DELETE", "OPTION", "PUT"])
def echo():
    dump_result()
    return 'Hello, World!'

app.run(host='0.0.0.0',port=args.port)
