FROM bash:alpine3.15


RUN apk add git git-lfs
COPY . /opt/download
RUN chmod +x /opt/download/download.sh

ENTRYPOINT ["/opt/download/download.sh"]
