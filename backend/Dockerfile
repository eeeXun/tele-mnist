FROM python

WORKDIR /app

COPY index.py /app
COPY model.h5 /app
COPY requirements.txt /app

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3", "index.py"]
