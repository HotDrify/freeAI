"""
@ Author : HotDrify
@ Type : GPT-3.5-turbo
@ GiT : https://github.com/HotDrify/freeAI
@ taken from gpt4free
"""
import asyncio
import time
from fake_useragent import UserAgent
import aiohttp

headers = {
    "User-Agent": UserAgent().random,
    "authority": "api.aichatos.cloud",
    "origin": "https://chat9.yqcloud.top",
    "referer": "https://chat9.yqcloud.top/"
}

class Running:
    @staticmethod
    async def main(q, proxies=None):
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(
                    "https://api.aichatos.cloud/api/generateStream",
                    json = {
                        "prompt": f"always reply in the user language | {q}",
                        "userId": f"#/chat/{int(time.time() * 1000)}",
                        "network": True,
                        "apikey": "",
                        "system": "",
                        "withoutContext": False
                    },
                    proxy = proxies
            ) as response:
                text = await response.text()
                if response.ok:
                    output = {
                        "status": ["OK"],
                        "created": time.time(),
                        "model": "GPT-3.5-turbo",
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
                        "model": "GPT-3.5-turbo",
                        "result": [
                            {}
                        ]
                    }
        return output