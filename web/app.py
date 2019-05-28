from flask import Flask
from flask_cors import CORS

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from flask_restplus import Api

sentry_sdk.init(
    dsn="https://5f0531268d3c4920a7b6ba11fa69d43f@sentry.io/1452832",
    integrations=[FlaskIntegration()],
)

app = Flask(__name__)
api = Api(app)

CORS(app)

## Manage Logging
from .log_manager import *

from .jobs import *

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
