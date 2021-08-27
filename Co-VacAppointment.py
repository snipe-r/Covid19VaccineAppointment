import requests
import time
from playsound import playsound
pin = 273014
date = '16-06-2021'
URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(
    pin, date)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}


def findAvailability():
    counter = 0
    result = requests.get(URL, headers=header)
    response_json = result.json()
    data = response_json["sessions"]
    for each in data:
        if((each["available_capacity"] > 0) & (each["min_age_limit"] == 18)):
            counter += 1
            print(each["name"])
            print(each["pincode"])
            print(each["vaccine"])
            print(each["available_capacity"])
            for i in range(10):
                playsound(r"C:\Users\Shivam Shukla\Downloads\ding-sound.mp3")
            return True
    if(counter == 0):
        return False


while(findAvailability() != True):
    time.sleep(30)
    findAvailability()
