FROM python:3.9.2-buster
ADD ./rest_app.py /
CMD ['python3','./rest_app.py']
