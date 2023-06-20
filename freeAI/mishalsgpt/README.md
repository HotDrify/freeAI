# freeAI
Example usage:
```python
from freeAI import mishalsgpt
import asyncio

async def main():
    result = mishalsgpt.Running.main("Hello! what language model are you?")
    print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

result(OK):
```json
{
  'status': ['OK']
  'created': 1687115742.184269,
  'model': 'GPT-3.5-turbo',
  'result': [
    {
      'prompt': 'Hello! what language model are you?',
      'content': 'Hello! what language model are you?', 'content': 'I am an AI language model created by OpenAI called GPT-3. I have been trained on a diverse range of internet text in order to be able to generate human-like responses to various prompts and questions.'
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
  'model': 'GPT-3.5-turbo',
  'result': [
    {}
  ]
}
```
Function's
* Running.main(q = **str**, proxies = json: **None**)