FROM node:lts-alpine

RUN apk update && apk add git python3 py3-pip
RUN pip install pyyaml && \
    npm install -g codefresh

COPY codefresh_components.py /

CMD ["./codefresh_components.py"]
