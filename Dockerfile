FROM ubuntu:20.04

WORKDIR /app
RUN apt update -y

RUN apt install python3-dev python3-pip nano curl iputils-ping -y

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
