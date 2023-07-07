"""
@ Author : HotDrify
@ Type : GPT-3.5-turbo
@ GiT : https://github.com/HotDrify/freeAI
"""
import asyncio
import time
from fake_useragent import UserAgent
import aiohttp

headers = {
    "User-Agent": UserAgent().random,
    "Content-Type": "application/json"
}

class Completion:
    @staticmethod
    async def acreate(messages, proxies=None):
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(
                    "https://fakell.raidghost.com/v1/chat/completions/",
                    data = {
                      "model": "gpt-3.5-turbo",
                      "messages": messages,
                      "stream": False
                    },
                    proxy = proxies
            ) as response:
                text = await response.json()
                if response.ok:
                    output = {
                        "status": ["OK"],
                        "object": "chat.completion",
                        "created": time.time(),
                        "model": "gpt-3.5-turbo",
                        "choices": [
                          {
                            "message": {
                              "content": text["choices"][0]["message"]["content"]
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