import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "pifrwg",
        "typeId": "Extern_Assignment",
        "deviceId":"1106"
    },
    "auth": {
        "token": "18BLC1106_Externship_Assignment"
    }
}


client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    inten=random.randint(0,125)
    level=random.randint(0,100)
    myData={'Light Intensity':inten, 'Water Level':level}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    time.sleep(2)
client.disconnect()
