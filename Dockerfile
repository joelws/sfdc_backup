FROM python:3.9.13-slim

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

WORKDIR /app

COPY ./sfdc_backup /sfdc_backup

ENTRYPOINT [ "python" ]
CMD ["-m", "sfdc_backup.main"]