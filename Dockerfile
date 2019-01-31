FROM python:3.6.5
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "run.py"]
