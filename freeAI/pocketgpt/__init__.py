"""
@ Author : HotDrify
@ Type : pocketGPT-4
@ GiT : https://github.com/HotDrify/freeAI
"""
import requests
import json
import time
from fake_useragent import UserAgent

ua = UserAgent()

class Running:
    @staticmethod
    def main(q):
        headers = {
          "User-Agent": ua.random,
          "Accept": "*/*",
          "Accept-Language": "ru-RU,ru;q==0.8,en-US;q=0.5,en;q=0.3",
          "Content-Type": "application/json",
          "Sec-Fetch-Deskt": "empty",
          "Sec-Fetch-Mode": "cors",
          "Sec-Fetch-Site": "same-origin"
        }
        payload = {
          "prompt": q,
          "model": "gpt-4",
          "plugin": "vanilla"
        }
        
        r = requests.post(
          "http://pocketgpt.000webhostapp.com/api/chat/completions/",
          headers=headers, 
          data=json.dumps(payload)
        )
        
        output = {
          "created": time.time(),
          "model": "GPT-4",
          "result": [
            {
              "prompt": q,
              "content": r.text
            }
          ]
        }
        return output