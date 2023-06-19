"""
@ Author : HotDrify
@ Type : AI-assist
@ GiT : https://github.com/HotDrify/freeAI
"""
import urllib.request
import json
from fake_useragent import UserAgent

headers = {
  "User-Agent": UserAgent().random,
  "Content-type": "application/json"
}
class Running:
    @staticmethod
    def main(
        proxies = None,
        systemMessage: str = "You are a helpful assistant",
        q,
        parentMessageId: str = "",
        temperature: float = 0.8,
        top_p: float = 1,
    ):
        json_data = {
            "prompt": q,
            "options": {"parentMessageId": parentMessageId},
            "systemMessage": systemMessage,
            "temperature": temperature,
            "top_p": top_p,
        }
        req = urllib.request.Request(
          "http://43.153.7.56:8080/api/chat-process",
          data = {
            "prompt": q,
            "options": {
              "parentMessageId": parentMessageId
            },
            "systemMessage": systemMessage,
            "temperature": temperature,
            "top_p": top_p
          },
          headers = headers
          proxies = proxies
        )
        r = urllib.request.urlopen(req)
        content = r.read().decode()
        return Running.__get_json(content)

    @classmethod
    def __load_json(cls, content) -> dict:
        split = content.rsplit("\n", 1)[1]
        to_json = json.loads(split)
        return to_json