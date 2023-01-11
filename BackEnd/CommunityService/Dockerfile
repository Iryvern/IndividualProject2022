FROM python:3.9.6

RUN mkdir /app
ADD . /app
WORKDIR /app

ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#EXPOSE 8081

CMD ["python", "server.py"]

#docker build -t c-api .
#docker run -p 8081:8081 -it c-api