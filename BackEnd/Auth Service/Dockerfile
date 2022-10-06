FROM python:3.9.6

RUN mkdir /app
ADD . /app
WORKDIR /app

ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run"]


#docker build -t api .
#docker run -p 5000:5000 -it api