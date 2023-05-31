FROM python:alpine3.10
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 5000
CMD python service1.py

