FROM python:3.7-alpine

RUN adduser -D flask

WORKDIR /home/flask

COPY isitpublic/requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install --no-cache-dir -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY isitpublic/app app
COPY isitpublic/isitpublic.py isitpublic/config.py isitpublic/forms.py isitpublic/functions.py isitpublic/boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP isitpublic.py

RUN chown -R flask:flask ./
USER flask

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]