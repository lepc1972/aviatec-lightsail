
FROM python:3
ADD aviatec.py /
RUN pip install flask
RUN pip install flask_restful
RUN pip install boto3
EXPOSE 8080
CMD [ "python", "./aviatec.py"]
 
