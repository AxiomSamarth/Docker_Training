FROM ubuntu

RUN apt-get update

HEALTHCHECK --interval=5s --timeout=3s --retries=2 CMD cd ./label_cd || exit 1
