FROM python:slim

RUN adduser shayblog

WORKDIR /home/shayblog

COPY requirements.txt requirements.txt
RUN python -m venv sbvenv
RUN sbvenv/bin/pip install -r requirements.txt
RUN sbvenv/bin/pip install gunicorn pymysql cryptography

COPY myapp myapp
COPY migrations migrations
COPY shayblog.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP shayblog.py

RUN chown -R shayblog:shayblog ./
USER shayblog

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]