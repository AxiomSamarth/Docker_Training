FROM ubuntu

RUN apt-get update

ADD ./Flask_apps.tar.gz /root/

CMD if test -d "/root/Flask_apps"; then echo "The folder has been extracted to your container"; fi
