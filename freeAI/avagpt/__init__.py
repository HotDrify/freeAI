"""
@ Author : HotDrify
@ Type : gpt-4
@ GiT : https://github.com/HotDrify/freeAI
"""

import asyncio
import json
import time
from fake_useragent import UserAgent
import aiohttp

headers = {
    "User-Agent": UserAgent().random,
    "accept": "application/json"

}
class Completion:
    @staticmethod
    async def acreate(messages, proxies = None, temperature = 1):
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(
                    "https://ava-alpha-api.codelink.io/api/chat",
                    json = {
                      "model": "gpt-4",
                      "temperature": temperature,
                      "stream": True,
                      "messages": messages
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
                        "model": "gpt-4",
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
                        "model": "gpt-4",
                        "choices": []
                    }
        return output