FROM python:3.9-slim
WORKDIR /helloworld
COPY . .
RUN pip install -r requirements.txt
EXPOSE 7000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:7000" ]
