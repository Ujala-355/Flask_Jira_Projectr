import requests
import json
url="https://ujalasaini.atlassian.net//rest/api/3/issue/TIC-27/transitions"
headers={
    "Accept":"application/json",
    "Content-Type":"application/json"
}
payload=json.dumps({
    
    "transition": {
        "id": "11"
    }
}

)
respons=requests.post(url,headers=headers,data=payload ,auth=("ujala21@navgurukul.org","av6Ysbkio57PNrawc1Em89B7"))
print(respons.text)