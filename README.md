# Modbus-MQTT IOx App

The main purpose is to send serial Modbus RTU data via MQTT to the Kinetic cloud on a Cisco IR829 gateway. On this gateway you can deploy a dockerized application where this python script can run.

## Getting Started

1. Clone the repo

2. Build the image
```
docker build -t modbusmqtt:latest .
```
3. Create the IOx tar with ioxclient
```
ioxclient docker package modbusmqtt:latest .
```
4. Install and run on the IR8x9. You troubleshoot with:
```
ioxclient application console <appid>
```

## Built With

* Cisco Kinetic Gateway Management Module
* MinimalModbus: https://pypi.org/project/minimalmodbus/
* PPaho-MQTT: https://pypi.org/project/paho-mqtt/

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE.md](LICENSE.md) file for details

## Further Links

Cisco DevNet Website: https://developer.cisco.com

IR829: https://www.cisco.com/c/en/us/products/collateral/routers/829-industrial-router/datasheet-c78-734981.html

IOx Documentation: https://developer.cisco.com/docs/iox/

Download ioxclient: https://developer.cisco.com/docs/iox/#!iox-resource-downloads

