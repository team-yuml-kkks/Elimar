FROM openjdk:21-slim

ENV PUPPETEER_SKIP_DOWNLOAD 1

RUN apt update -y \
    && apt -y install curl \
    && curl -L https://deb.nodesource.com/setup_18.x | bash \
    && apt update -y \
    && apt install -y \
        nodejs graphviz

RUN npm install -g c4builder@0.2.16

EXPOSE 3000

ENTRYPOINT ["c4builder"]
