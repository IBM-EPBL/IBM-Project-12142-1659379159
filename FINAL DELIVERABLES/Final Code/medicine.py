#IBM Watson IOT Platform
#pip install wiotp-sdk
import wiotp.sdk.device
import time
import random
from datetime import date
myConfig ={
 "identity":{
 "orgId": "smihrq",
 "typeId":"Medalarm",
 "deviceId":"555555"
 },
 "auth":{
 "token":"*xV*wjX4dK*NRQ*x6)"
 }
}

def MyCommandCallback(cmd):
    print ("Message received from IBM IOT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']
    if (m=="MEDICINE NAME"):
        print("*****/// MEDICINE NAME /////*****")
        
client = wiotp.sdk.device.DeviceClient(config=myConfig,logHandlers=None)
client.connect()

while True:
    medicinename=input('enter medicine name: ')
    time=input(time.time())
    date=input(date.today())
    name=medicinename
    time=time
    date=date
    myData={'medicine name':name, 'time':time, 'date': date}
    client.publishEvent(eventId="status", msgFormat="json",data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    #time.sleep(2)
    break

client.disconnect()
