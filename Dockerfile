FROM alpine:latest

RUN apk add --update --no-cache python3 py3-setuptools
RUN pip3 install --upgrade pip
RUN pip3 install paho-mqtt minimalmodbus

COPY cert.crt /opt/modbus-mqtt/cert.crt
COPY iox-modbus-mqtt.py /opt/modbus-mqtt/iox-modbus-mqtt.py
