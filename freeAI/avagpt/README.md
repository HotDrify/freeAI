# freeAI
Example usage:
```python
from freeAI import avagpt
import asyncio

async def main():
    result = await avagpt.Completion.acreate("Hello! what language model are you?")
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
        "content": "Hello! I am an AI language model developed by OpenAI, known as GPT-3 (Generative Pre-trained Transformer 3). I have been trained on a wide range of internet text to assist with various tasks and provide information on different topics. How can I assist you today?"
       }
     }
   ]
}
{
  'status': ['OK']
  'created': 1687115742.184269,
  'model': 'GPT-3.5-turbo',
  'result': [
    {
      'messages': [{"role": "user", "content": "Hello! what language model are you?"}],
      'content': 'Hello! what language model are you?', 'content': 'I am an AI language model created by OpenAI called GPT-3. I have been trained on a diverse range of internet text in order to be able to generate human-like responses to various prompts and questions.'
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