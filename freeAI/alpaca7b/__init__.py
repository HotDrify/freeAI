"""
@ Author : HotDrify
@ Type : alpaca 7B
@ GiT : https://github.com/HotDrify/freeAI
"""
import requests
import time
from fake_useragent import UserAgent

headers = {
  "User-Agent": UserAgent().random
}
class Running:
    @staticmethod
    def main(q, proxies = None):
        r = requests.post(
          "https://us-central1-arched-keyword-306918.cloudfunctions.net/run-inference-1",
          proxies = proxies,
          json = {
            "prompt": q
          }
        )
        if r.ok:
            output = {
              "status": ["OK"],
              "created": time.time(),
              "model": "alpaca-7B",
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
              "model": "alpaca-7B",
              "result": [
                {}
              ]
            }
        return output