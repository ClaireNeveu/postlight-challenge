FROM debian:buster-slim

ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8

RUN apt-get update

RUN apt-get install -y locales
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && locale-gen

RUN apt-get -y install python3 pipenv

# Application building
COPY Pipfile postlight-api/
COPY Pipfile.lock postlight-api/
COPY start.py postlight-api/

WORKDIR postlight-api/

RUN pipenv sync --python /usr/bin/python3

CMD python3 start.py
