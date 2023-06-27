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

class Running:
    @staticmethod
    async def main(messages, proxies = None, temperature = 1):
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
                rtext = await response.text()
                text = rtext.replace("data: ", "").replace("\n\n", "\n").rstrip("\n[DONE]")
                lines = text.splitlines()
                resout = ""
                for line in lines:
                    try:
                        data = json.loads(line)
                        resout += data["choices"][0]['delta']['content']
                    except Exception:
                        pass
                if response.ok:
                    output = {
                        "status": ["OK"],
                        "created": time.time(),
                        "model": "GPT-3.5-turbo",
                        "result": [
                            {
                                "messages": messages,
                                "content": resout
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