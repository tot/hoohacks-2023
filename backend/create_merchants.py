#Create Merchants

from dotenv import load_dotenv
import os, requests, json, glob,time
import create_transactions 
import numpy as np
load_dotenv()
api_key = os.getenv("API_KEY")

def arrayMaker(folder, textfile):
  for filename in glob.glob(folder):
    name = ''.join(filename.rpartition('/')[2])
    name = name.split("\\")
    
    if ((name[1]) == textfile):
      with open(os.path.join(os.getcwd(), filename), "r") as text:
        lines = [line.split() for line in text]
        return lines
      
def rowSlice(array, index):
  newArr = np.array(array)
  slice = newArr[index, :]
  return slice

def createMerchants():
    url = 'http://api.nessieisreal.com/merchants?key={}'.format(api_key)
    data = arrayMaker("./backend/*", "merchantData.txt")

    for i in range(15):
        time.sleep(2)
        arr = rowSlice(data, i)


        payload = {
        "name": arr[0],
        "category": arr[1],
        "address": {
            "street_number": "123",
            "street_name": "University Street",
            "city": "Charlottesville",
            "state": "VA",
            "zip": "22308"
        },
        "geocode": {
            "lat": 15,
            "lng": 15
        }
        }

        response = requests.post(url,data=json.dumps(payload), 
                headers={'Content-Type': 'application/json', 'Accept': 'application/json'} )

        print(response.content)
