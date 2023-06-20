"""
@ Author : HotDrify
@ Type : alpaca 7B
@ GiT : https://github.com/HotDrify/freeAI
"""
import asyncio
import time
from fake_useragent import UserAgent
import aiohttp

headers = {
    "User-Agent": UserAgent().random
}

class Running:
    @staticmethod
    async def main(q, proxies=None):
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(
                    "https://us-central1-arched-keyword-306918.cloudfunctions.net/run-inference-1",
                    json = {
                        "prompt": q
                    },
                    proxy = proxies
            ) as response:
                if response.ok:
                    output = {
                        "status": ["OK"],
                        "created": time.time(),
                        "model": "alpaca-7B",
                        "result": [
                            {
                                "prompt": q,
                                "content": await response.json()['completion']
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
                        "model": "alpaca-7B",
                        "result": [
                            {}
                        ]
                    }
        return output