FROM python:3.7-alpine

RUN pip3 install flask~=1.0.0
WORKDIR /app
COPY app.py /app/

CMD ["python3", "app.py"]

