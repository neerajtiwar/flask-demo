from flask import Flask, request
import structlog
import json

app = Flask(__name__)
LOGGER = structlog.get_logger()


@app.route("/api/collector", methods=["POST"])
def webhook():
    LOGGER.info("request received")
    event = request.get_data()
    LOGGER.info(f"ArgoCD Notification received is:  {event}")
    data = json.loads(event)
    data["test"] = "Processed"
    return json.dumps(data)


if __name__ == "__main__":
    app.run(port=5000)






