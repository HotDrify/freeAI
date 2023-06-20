"""
@ Author : HotDrify
@ Type : GPT-4
@ GiT : https://github.com/HotDrify/freeAI
"""
import aiohttp
import asyncio
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
    async def main(q, proxies=None):
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(
                    "http://pocketgpt.000webhostapp.com/api/chat/completions/",
                    data = {
                        "prompt": q,
                        "model": "gpt-4",
                        "plugin": "vanilla"
                    },
                    proxy = proxies
            ) as response:
                text = await response.text
                if response.ok:
                    output = {
                        "status": ["OK"],
                        "created": time.time(),
                        "model": "pocketGPT-4",
                        "result": [
                            {
                                "prompt": q,
                                "content": text
                            }
                        ]
                    }
                else:
                    output = {
                        "status": [
                            {
                                "code": response.status
                            }
                        ],
                        "created": time.time(),
                        "model": "pocketGPT-4",
                        "result": [
                            {}
                        ]
                    }
        return output