
# freeAI
Example usage:
```python
from freeAI import minigpt
import asyncio

async def main():
    result = await minigpt.Completion.acreate("Hello! what language model are you?")
    print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

result(OK):
```json
{
  "status": ["OK"],
  "object": "chat.completion",
  "created": time.time(),
  "model": "gpt-3.5-turbo",
  "choices": [
    {
      "message": {
        "content": "Hello! I am GPT-4, a large language model trained by OpenAI. I am designed to assist with answering questions, providing information, and engaging in conversation. How can I help you today?"
       }
     }
   ]
}
```
result(error):
```json
{
  "status": ["ERR", {"code": 500}],
  "object": "chat.completion",
  "created": time.time(),
  "model": "gpt-3.5-turbo",
  "choices": []
}
```
Function's
* Completion.acreate(q = **str**, proxies = json: **None**)