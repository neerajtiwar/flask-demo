from flask import Flask, request
import structlog
import json

app = Flask(__name__)
LOGGER = structlog.get_logger()


@app.route("/sum", methods=["POST"])
def webhook():
    LOGGER.info("request received")
    operand1 = request.args.get('num1')
    operand2 = request.args.get('num2')
    addition = int(operand1) + int(operand2)
    return {
        "sum": addition
    }


if __name__ == "__main__":
    app.run(port=5000)






