from bson import json_util
import json
import pymongo
from ..bootstrap import db, cache

from bson.objectid import ObjectId


def fetch_latest_jobs(page=1, per_page=10):
    jobs = (
        db.jobs.find()
        .sort("date", pymongo.DESCENDING)
        .skip((page - 1) * per_page)
        .limit(per_page)
    )
    jobs = list(jobs)
    jobs = json.dumps({"result": jobs}, indent=4, default=json_util.default)

    return json.loads(jobs)


def get_total_jobs_count():
    rv = cache.get("total-jobs-count")
    if rv is None:
        count = db.jobs.find().count()
        response = json.dumps({"result": count})
        cache.set("total-jobs-count", response, timeout=60 * 60 * 24)
        return json.loads(response)

    return json.loads(rv)


def search_jobs(search, page=1, per_page=10):
    jobs = (
        db.jobs.find({"$text": {"$search": search}})
        .sort("date", pymongo.DESCENDING)
        .skip((page - 1) * per_page)
        .limit(per_page)
    )
    jobs = list(jobs)
    jobs = json.dumps({"result": jobs}, indent=4, default=json_util.default)

    return json.loads(jobs)


def get_job_details(jobId):
    jobs = db.jobs.find({"_id": ObjectId(jobId)})
    jobs = list(jobs)
    jobs = json.dumps({"result": jobs}, indent=4, default=json_util.default)

    return json.loads(jobs)
