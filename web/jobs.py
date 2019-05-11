from flask import request
from flask_restplus import Resource
from .app import api
from .services.jobs import fetch_latest_jobs, get_total_jobs_count, search_jobs, get_job_details

@api.route('/jobs')
class Job(Resource):
    def get(self):
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        return fetch_latest_jobs(page, per_page)

@api.route('/jobs/<string:job_id>')
class JobDetails(Resource):
    def get(self, job_id):
        return get_job_details(job_id)

@api.route('/jobs/count')
class JobCount(Resource):
    def get(self):
        return get_total_jobs_count()
    
@api.route('/jobs/search')
class JobSearch(Resource):
    def get(self):
        search = request.args.get('query')
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        return search_jobs(search, page, per_page)
    