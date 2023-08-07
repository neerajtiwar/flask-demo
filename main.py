from flask import Flask, request
import structlog

app = Flask(__name__)
LOGGER = structlog.get_logger()


@app.route("/api/collector", methods=["POST"])
def webhook():
    LOGGER.info("request received")
    event = request.get_data()
    LOGGER.info(f"ArgoCD Notification received is:  {event}")


if __name__ == "__main__":
    app.run(port=5000)






