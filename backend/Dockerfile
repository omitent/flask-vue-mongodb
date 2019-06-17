FROM python:3.5

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /usr/src/app
WORKDIR /usr/src/app

CMD ["python", "main.py"]