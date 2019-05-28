from flask import request
from .app import app

# Useful debugging interceptor to log all values posted to the endpoint
@app.before_request
def before():
    app.logger.debug("Headers: %s", request.headers)
    app.logger.debug("Body: %s", request.get_data())


# Useful debugging interceptor to log all endpoint responses
@app.after_request
def after(response):
    return response


# Default handler for uncaught exceptions in the app
@app.errorhandler(500)
def internal_error(exception):
    app.logger.error(exception)
    return flask.make_response("server error", 500)


# Default handler for all bad requests sent to the app
@app.errorhandler(400)
def handle_bad_request(e):
    app.logger.info("Bad request", e)
    return flask.make_response("bad request", 400)
