# freeAI
Example usage:
```python
from freeAI import pocketgpt

response = pocketgpt.Running.main("Hello! what language model are you?")
print(response)
```

result(OK):
```json
{
  'status': ['OK']
  'created': 1687115742.184269,
  'model': 'GPT-4',
  'result': [
    {
      'prompt': 'Hello! what language model are you?',
      'content': 'Hello! I am GPT-4, a language model created by OpenAI. If you have questions or need information, I'm happy to help.'
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
  'model': 'GPT-4',
  'result': [
    {}
  ]
}
```
Function's
* Running.main(q = **str**, proxies = json: **None**, model = str: **gpt-4**, plugin = str: **vanilla**, temperature = int: **1**)