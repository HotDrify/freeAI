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
    "Accept": "*/*",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Content-Type": "application/json",
    "Authorization": "Bearer ninomae1001",
    "referrer": "http://124.222.157.84:8012/",
}
class Running:
    @staticmethod
    async def main(messages, proxies = None, temperature = 1, model = "gpt-4"):
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(
                    "http://124.222.157.84:3700/v1/chat/completions",
                    data = {
                      "messages": messages,
                      "model": model,
                      "temperature": temperature,
                      "presence_penalty": 0,
                      "top_p": 1,
                      "frequency_penalty": 0,
                      "stream": True,
                      "key": "bilibili"
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