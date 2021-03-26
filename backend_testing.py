import requests
import pymysql
from db_connector import get_user_name_from_db


def post_user(user_id, user_name):
    res = requests.post("http://127.0.0.1:5000/users/%s" % user_id, json={'user_name': user_name})
    if res.status_code == 200:
    # print('POST RESPONSE: %s' % res)
        print("POST Success %s" % res)
    else:
        print("POST failure %s" % res, "id already exist")


def get_user(user_id, user_name):
    response = requests.get("http://127.0.0.1:5000/users/%s" % user_id)
    response_data = response.json()
    response_name = response_data.get('user_name')
    success = response.status_code == 200 and response_name == user_name
    print("GET Response Successfull.", "The user name is:", user_name)






if __name__ == "__main__":
    post_user(1, 'lihi ofir')
    get_user(1, 'lihi ofir')
    get_user_name_from_db(1)


