FROM python:3.8-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD gunicorn --bind :${PORT:-5000} run:app
