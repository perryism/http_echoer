from flask import Flask, request, jsonify
import logging, sys
import argparse

parser = argparse.ArgumentParser(description="Echo")
parser.add_argument("--log", choices=["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], default="INFO",
                    help="Log level")
parser.add_argument("--port", type=int, default=5555, help="Port")

args = parser.parse_args()
app = Flask(__name__)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

fh = logging.FileHandler('echo.log')
fh.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter("%(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

def dump_result(result):
    logger.info(result["url"])
    logger.info(result["method"])
    for k, v in result["headers"].items():
        logger.info("%s: %s"%(k, v))
    logger.info("")
    logger.info(result["body"])

def capture_result():
    return {
            "url": request.url,
            "method": request.method,
            "headers": dict(request.headers),
            "body": request.get_data().decode("utf8")
            }

@app.route('/', methods=["GET", "POST", "DELETE", "OPTION", "PUT"])
def echo():
    result = capture_result()
    dump_result(result)
    return jsonify(result)

app.run(host='0.0.0.0',port=args.port)
