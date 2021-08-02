FROM python:3.2
ENV PYTHONUNBUFFERED 0.1.0
RUN lmss
WORKDIR /lmss
COPY requirements.txt /lmss
RUN pip install -r requirements.txt
COPY . /lmss/

