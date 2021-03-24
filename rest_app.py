import os
import signal
from flask import Flask, request
from db_connector import get_user_name_from_db, add_user_name_to_db, delete_user_name_from_db, update_user_name_in_db

app = Flask(__name__)

@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(),signal.SIGTERM)
    return 'Server Stopped'

@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def get_user(user_id):
    if request.method == 'GET':
        try:
            #check user name per id from DB
            user_name = get_user_name_from_db(user_id)
            if user_name is not None:
                return {"status": "ok", "user_name": user_name}, 200
            else:
                return {"status": "error", "reason": "failed to get user"}, 500
        except Exception as e:
            return {"status:": "error", "reason": "failed to get user"}, 500
    elif request.method == 'POST':
        try:
            # getting the json data payload from request
            request_data = request.json
            # treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get('user_name')
            result = add_user_name_to_db(user_id, user_name)
            if result is True:
                return {"status": "ok", "user added": user_name}, 200
            else:
                return {"status": "error", "reason": "id already exist"}, 500  # status code
        except Exception as e:
            return {"status": "error", "reason": "id is not the issue, something else is wrong"}, 500  # status code
    elif request.method == 'PUT':
        try:
            # getting the json data payload from request
            request_data = request.json
            # treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get('user_name')
            result = update_user_name_in_db(user_id, user_name)
            if result is True:
                return {"status": "ok", "user updated": user_name}, 200
            else:
                return {"status": "error", "reason": "there was nothing to update"}, 500  # status code
        except Exception as e:
            return {"status": "error", "reason": "user exist, must be something else that is wrong"}, 500  # status code
    elif request.method == 'DELETE':
        try:
            # getting the json data payload from request
            request_data = request.json
            # treating request_data as a dictionary to get a specific value from key
            # user_name = request_data.get('user_name')
            # user_id = request_data.get(user_id)
            result = delete_user_name_from_db(user_id)
            if result is True:
                return {"status": "ok", "user deleted": user_id}, 200
            else:
                return {"status": "error", "reason": "the requested id does not exist"}, 500  # status code
        except Exception as e:
            return {"status": "error", "reason": "no such id"}, 500  # status code


app.run(host='127.0.0.1', debug=True, port=5000)
