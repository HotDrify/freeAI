"""
@ Author : HotDrify
@ Type : gpt-3.5-turbo
@ GiT : https://github.com/HotDrify/freeAI
"""
import asyncio
import json
import time
from fake_useragent import UserAgent
import aiohttp

headers = {
    "User-Agent": UserAgent().random,
    "accept": "text/event-stream"
}

class Completion:
    @staticmethod
    async def acreate(messages, proxies = None, temperature = 1):
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(
                    "http://super.lockchat.app/v1/chat/completions?auth=FnMNPlwZEnGFqvEc9470Vw==",
                    json = {
                      "temperature": temperature,
                      "messages": messages,
                      "model": "gpt-3.5-turbo",
                      "stream": True
                    },
                    proxy = proxies
            ) as response:
                webText = await response.text()
                out = webText.replace("data: ", "").replace("\n\n", "\n").rstrip("\n[DONE]")
                lines = out.splitlines()
                text = ""
                for line in lines:
                    try:
                        data = json.loads(line)
                        text += data["choices"][0]['delta']['content']
                    except Exception:
                        pass
                if response.ok:
                    output = {
                        "status": ["OK"],
                        "object": "chat.completion",
                        "created": time.time(),
                        "model": "gpt-3.5-turbo",
                        "choices": [
                          {
                            "message": {
                              "content": text
                            }
                          }
                        ]
                    }
                else:
                    output = {
                        "status": ["ERR", {"code": response.code}],
                        "object": "chat.completion",
                        "created": time.time(),
                        "model": "gpt-3.5-turbo",
                        "choices": []
                    }
        return output