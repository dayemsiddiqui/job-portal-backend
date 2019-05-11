from flask import Flask
from flask_cors import CORS
from flask import request, jsonify
from .jobs import fetch_latest_jobs, get_total_jobs_count, search_jobs, get_job_details
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://5f0531268d3c4920a7b6ba11fa69d43f@sentry.io/1452832",
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)

app.config.from_pyfile('config.py')

CORS(app)


@app.route('/')
def hello_world():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    return fetch_latest_jobs(page, per_page)


@app.route('/jobs/count')
def get_jobs_counts():
    return get_total_jobs_count()


@app.route('/jobs')
def search():
    search = request.args.get('search')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    return search_jobs(search, page, per_page)


@app.route('/ping')
def test():
    return jsonify({'status': 'success', 'payload':'pong'})



@app.route('/jobs/<job_id>')
def job_detail(job_id):
    return get_job_details(job_id)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
