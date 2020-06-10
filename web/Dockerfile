FROM debian:buster-slim

ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8

RUN apt-get update

RUN apt-get install -y locales
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && locale-gen

RUN apt-get -y install npm

COPY package.json postlight-web/
COPY public postlight-web/public
COPY src postlight-web/src
COPY tsconfig.json postlight-web/
COPY package-lock.json postlight-web/

WORKDIR postlight-web/

RUN npm install
RUN npm run-script build

CMD npx serve -l 4000 build