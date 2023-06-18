# freeAI
Example usage:
```python
from freeAI import alpaca7b

response = alpaca7b.Running.main("Hello! what language model are you?")
print(response)
```

result(OK):
```json
{
  'status': ['OK']
  'created': 1687115742.184269,
  'model': 'alpaca-7B',
  'result': [
    {
      'prompt': 'Hello! what language model are you?',
      'content': 'I am language model!'
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
* Running.main(q = **str**, proxies = json: **None**)