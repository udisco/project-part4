FROM python:3.9.2-buster
COPY getUser.py
CMD ['python3','getUser.py']