FROM python:3.11-slim
ENV PYTHONPATH=/app
WORKDIR ${PYTHONPATH}
COPY requirement.txt .
RUN pip3 install -r requirement.txt
COPY main.py .
CMD gunicorn --workers 1 --timeout 300 --bind 0.0.0.0:8001 --log-file=-  main:app main.py
EXPOSE 8001
