import json
import urllib
import requests

def check(username):
    url = "https://accounts.google.com/_/signup/webusernameavailability?hl=en&rt=j"

    payload = {
        "flowEntry": "SignUp",
        "flowName": "GlifWebSignIn",
        "f.req": json.dumps(["", "", "", username, True, "", 1])
    }
    payload = urllib.parse.urlencode(payload)
    headers = {
      'authority': 'accounts.google.com',
      'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
      'x-same-domain': '1',
      'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
      'google-accounts-xsrf': '1',
      'sec-ch-ua-mobile': '?0',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
      'sec-ch-ua-platform': '"Windows"',
      'accept': '*/*',
      'origin': 'https://accounts.google.com',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    res = json.loads(response.text.split("\n")[-1])[0][0]
    
    return res
