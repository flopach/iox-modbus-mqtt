# Modbus-MQTT IOx App

Send serial Modbus RTU data via MQTT to the Kinetic cloud on a Cisco IR829 Gateway

## Installation

1. Put all files in one directory & edit them
2. docker build -t modbusmqtt:latest .
3. ioxclient docker package modbusmqtt:latest .
4. Install and run on IR8x9


## Documenation

IR829: https://www.cisco.com/c/en/us/products/collateral/routers/829-industrial-router/datasheet-c78-734981.html

IOx Documentation: https://developer.cisco.com/docs/iox/

Download ioxclient: https://developer.cisco.com/docs/iox/#!iox-resource-downloads

MinimalModbus: https://pypi.org/project/minimalmodbus/

Paho-MQTT: https://pypi.org/project/paho-mqtt/
