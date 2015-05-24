FROM python:2.7.9
COPY requirements.txt /src/
RUN cd /src && pip install ipython && pip install -r requirements.txt
COPY server.py /src/
WORKDIR /src
CMD ["gunicorn", "-b", "0.0.0.0:5000", "server:app"]
EXPOSE 5000
