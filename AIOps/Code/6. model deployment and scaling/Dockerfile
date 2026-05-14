FROM python:3.9

RUN groupadd -g 1000 sampleuser && \
    useradd -r -u 1000 -g sampleuser sampleuser

WORKDIR /home

RUN chown sampleuser:sampleuser /home

USER sampleuser

COPY . /home

RUN pip install -r /home/requirements.txt

CMD python3 /home/run.py