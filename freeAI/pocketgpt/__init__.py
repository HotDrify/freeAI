"""
@ Author : HotDrify
@ Type : GPT-4
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
    def main(q, proxies = None):
      json = {
        "prompt": q,
        "model": "gpt-4",
        "plugin": "vanilla"
      }
      r = requests.post(
        "http://pocketgpt.000webhostapp.com/api/chat/completions/",
        headers = headers,
        data = json,
        proxies = proxies
      )
      if r.ok:
          output = {
            "status": ["OK"],
            "created": time.time(),
            "model": "pocketGPT-4",
            "result": [
              {
                "prompt": q,
                "content": r.json()['completion']
              }
            ]
          }
      else:
          output = {
            "status": [
              {
                "code": r.status_code
              }
            ],
            "created": time.time(),
            "model": "pocketGPT-4",
            "result": [
              {}
            ]
          }
      return output