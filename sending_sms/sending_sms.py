import requests
import json
def send_sms(number,message):
    url="https://www.fast2sms.com/dev/bulkV2"
    params={
        "authorization":"dFMKneWBkqDOUroNas0FUkAq4cRprDIr9hxrcTkenVG54DrRRTTdVRsNiz1Z",
        "sender_id":"TXTIND",
        "message":"Hello Good Morning",
        "route":"v3",
        "numbers":number
    }
    response=requests.get(url, params=params)
    dic=response.json()
    print(dic)
send_sms("9819051025","hello good morning")
print("testing")