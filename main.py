from flask import Flask, request
import structlog
import json
import sys
import logging
import os

app = Flask(__name__)
level = getattr(logging, os.environ.get('LOG_LEVEL', 'INFO').upper(), logging.INFO)

structlog.configure(
    cache_logger_on_first_use=True,
    wrapper_class=structlog.make_filtering_bound_logger(level),
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.format_exc_info,
        structlog.processors.TimeStamper(fmt="iso", utc=True),
        structlog.processors.JSONRenderer(),
    ]
)

LOGGER = structlog.get_logger(__name__)

def handle_exception(exctype, value, tb):
    logger = structlog.get_logger("sys.excepthook")
    logger.critical(event="unhandled exception", exc_info=(exctype, value, tb))


@app.route("/api/collector", methods=["POST"])
def webhook():
    LOGGER.info("request received")
    print(request.headers, file=sys.stderr)
    event = request.get_data()
    LOGGER.info(f"ArgoCD Notification received is:  {event}")
    data = json.loads(event)
    data["test"] = "Processed"
    return json.dumps(data)


if __name__ == "__main__":
    sys.excepthook = handle_exception
    app.run(port=6000)






