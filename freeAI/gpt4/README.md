# freeAI
Example usage:
```python
from freeAI import gpt4
import asyncio

async def main():
    result = await gpt4.Running.main("Hello! what language model are you?")
    print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

result(OK):
```json
{
  'status': ['OK']
  'created': 1687115742.184269,
  'model': 'GPT 4',
  'result': [
    {
      'prompt': 'Hello! what language model are you?',
      'content': 'Hello! I am GPT-4, a large language model trained by OpenAI. I am designed to assist with answering questions, providing information, and engaging in conversation. How can I help you today?'
    }
  ]
}
```
result(error):
```json
{
  'status': [
    {
      "code": 500
    }
  ],
  'created': 1687115742.184269,
  'model': 'GPT 4',
  'result': [
    {}
  ]
}
```
Function's
* Running.main(q = **str**, proxies = json: **None**, model = str: **gpt-4**)