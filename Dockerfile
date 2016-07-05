FROM dockercisco/acitoolkit
MAINTAINER Chad Peterson, chapeter@cisco.com

WORKDIR /opt
RUN git clone http://github.com/chapeter/acidash
WORKDIR acidash

EXPOSE 8000
CMD [ "python", "main.py" ]