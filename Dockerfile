FROM python:3.11-alpine

WORKDIR /app

RUN apk update
RUN apk add bash git curl

# install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy sources
COPY . .

# create tmp directory
RUN mkdir .tmp

CMD ["python3", "/app/CommandLab.py"]