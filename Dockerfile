FROM python:3.9-alpine3.12
ADD rest_app.py db_connector.py /
RUN pip install flask requests pymysql
EXPOSE 5000:5000
CMD ["python", "./rest_app.py"]
