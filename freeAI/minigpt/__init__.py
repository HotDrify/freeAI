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
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Content-Type": "application/json",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "123",
    "Sec-Fetch-Site": "same-origin"
}
class Running:
    @staticmethod
    async def main(q, proxies = None, temperature = 1):
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(
                    "https://mflsf.aitianhu.fun/api/chat-process",
                    json = {
                      "prompt": q,
                      "options": {},
                      "systemMessage": "You are heplful gpt-3 assistant.",
                      "temperature": temperature,
                      "top_p": 1
                    },
                    proxy = proxies
            ) as response:
                text = await response.text()
                lines = text.splitlines()
                out = ""
                for line in lines:
                    data = json.loads(line)
                    try:
                        out = data['choices'][0]['delta']['content']
                    except Exception as err:
                        pass
                if response.ok:
                    output = {
                        "status": ["OK"],
                        "created": time.time(),
                        "model": "GPT-3.5-turbo",
                        "result": [
                            {
                                "prompt": q,
                                "content": out
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
                        "model": "GPT-3.5-turbo",
                        "result": [
                            {}
                        ]
                    }
        return output