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
class Running:
    @staticmethod
    async def main(messages, proxies = None, temperature = 1):
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
                        "model": "GPT-4",
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
                        "model": "GPT-4",
                        "result": [
                            {}
                        ]
                    }
        return output