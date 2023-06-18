"""
@ Author : HotDrify
@ Type : pocketGPT-4
@ GiT : https://github.com/HotDrify/freeAI
"""
import requests
import time
from fake_useragent import UserAgent

headers = {
  "User-Agent": UserAgent().random,
  "Accept": "*/*",
  "Accept-Language": "ru-RU,ru;q==0.8,en-US;q=0.5,en;q=0.3",
  "Content-Type": "application/json",
  "Sec-Fetch-Deskt": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "same-origin"
}
class Running:
    @staticmethod
    def main(q, proxies = None, model = "gpt-4", plugin = "vanilla", temperature = 1):
        r = requests.post(
          "http://pocketgpt.000webhostapp.com/api/chat/completions/",
          proxies = proxies,
          headers = headers, 
          data = {
            "prompt": q,
            "model": model,
            "plugin": plugin,
            "temperature": temperature
          }
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