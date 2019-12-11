# Send serial Modbus RTU data via MQTT to the Kinetic cloud on a Cisco IR829 Gateway
# Flo Pachinger / flopach, Cisco Systems, 2019
# Apache License 2.0
import paho.mqtt.client as mqtt
import serial
import minimalmodbus
import time

# MQTT
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


# disconnect message
def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected with result code " + str(rc))
    client.loop_stop()


# print the log
def on_log(client, userdata, level, buf):
    print("log: " + buf)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(str(msg))


# MQTT connection parameters
client = mqtt.Client("IR829_gateway")
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_log = on_log
client.on_message = on_message

# TLS certificate for the Kinetic Cloud
# You find the username and password of the MQTT broker on the Kinetic cloud
# URL depends on the cluster: eu.ciscokinetic.io or us.ciscokinetic.io
client.tls_set("cert.crt", tls_version=2)
client.username_pw_set("55555", "xxx_pwd")
client.connect("eu.ciscokinetic.io", 8883, 60)
client.loop_start()

# Modbus Parameters
i = minimalmodbus.Instrument('/dev/ttyS1', 1)
i.serial.baudrate = 9600
i.serial.bytesize = 8
i.serial.stopbits = 1
i.serial.timeout = 1
i.address = 1
i.mode = minimalmodbus.MODE_RTU

while True:
    time.sleep(1) #read and send sensor data every 1 second
    try:
        r = i.read_register(0x1100, 5)  # change here your modbus registers
        client.publish("/v1/55555/json/dev2app/modbussensor", "{ 'modbusdata': '" + str(r) + "' }") # find the MQTT topic URL on the Kinetic cloud
    except serial.SerialException:
        print("Serial connection error!")
