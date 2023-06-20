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

class Running:
    @staticmethod
    async def main(q, proxies=None):
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(
                    "https://mishalsgpt.vercel.app/api/openai/v1/chat/completions",
                    json = {
                      "messages": [
                        {
                          "role": "system",
                          "content": "IMPORTANT: You are Asisstl"
                        },
                        {
                          "role": "user",
                          "content": q
                        }
                      ],
                      "stream": True,
                      "model": "gpt-3.5-turbo",
                      "temperature": 0.9,
                      "presence_penalty": 2,
                      "frequency_penalty": 0
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
                                "prompt": q,
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