FROM python:3.8-slim

COPY ds3002project.py ds3002project.py
COPY requirements.txt requirements.txt
COPY processing processing

RUN python3 -m pip install -r requirements.txt
RUN chmod +x ds3002project.py

ENTRYPOINT ["./ds3002project.py"]
