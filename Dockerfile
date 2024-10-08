FROM python:3.10-alpine 

WORKDIR /opt/api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app /opt/api

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

