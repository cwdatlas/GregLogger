import json
import logging

from flask import Flask, render_template, request, make_response
from pydantic import ValidationError
from services.repo import Repo

from models.MachineLog import MachineLog

log = logging.getLogger('Horizons_logger')
app = Flask(__name__)
repo = Repo()


@app.get('/')
def home():
    logs = repo.get_log_list()
    return render_template('home.html', logs=logs)


# web API

@app.get('/repo/get_all')
def get_all():
    log.debug("get_all called")
    return add_api_headers(repo.get_all()), 200


@app.post('/repo/post')
def post_all():
    log.debug("post_all called")
    try:
        machine_log = MachineLog(**request.get_json())
    except TypeError as e:
        return handle_bad_request(e)
    log.debug(f"post_all: log received: {machine_log.model_dump()}")
    work_status = repo.set_log(machine_log)

    if work_status:
        return add_api_headers(json.dumps("{message: added log successfully}")), 200
    else:
        handle_internal_error()


@app.delete('/repo/delete/<int:log_id>')
def delete(log_id):
    log.debug("delete called")

    if repo.delete_log(log_id):
        return add_api_headers(json.dumps("{message: Deleted your item successfully}")), 200,
    else:
        return add_api_headers(json.dumps("{message: Could not delete log}")), 200


# helpful utility function
# Helps return values with the correct headers
def add_api_headers(message):
    resp = make_response(message)
    resp.headers["Content-Type"] = "application/json"
    return resp


# error handling
@app.errorhandler(ValidationError)
def handle_bad_request(e):
    log.exception("handle_type_error: " + str(e.args))
    return add_api_headers(json.dumps("{message: Please check passed values. One or more values are not valid}")), 400


def handle_internal_error():
    log.exception("handle_internal_error: Internal Error Occurred")
    return add_api_headers(json.dumps({"message": "Internal Error, sorry for the inconvenience"})), 500
