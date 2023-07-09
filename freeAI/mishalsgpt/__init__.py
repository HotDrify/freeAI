"""
@ Author : HotDrify
@ Type : gpt-3.5-turbo-0301
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
                    "https://mishalsgpt.vercel.app/api/openai/v1/chat/completions",
                    json = {
                      "messages": messages,
                      "stream": True,
                      "model": "gpt-3.5-turbo",
                      "temperature": temperature,
                      "presence_penalty": 2,
                      "frequency_penalty": 0
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
                        "model": "gpt-3.5-turbo-0301",
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
                        "status": ["ERR", {"code": response.status}],
                        "object": "chat.completion",
                        "created": time.time(),
                        "model": "gpt-3.5-turbo-0301",
                        "choices": []
                    }
        return output