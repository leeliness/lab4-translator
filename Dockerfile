FROM python:3.12

WORKDIR /Tikhonova

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "gtrans3.py"]