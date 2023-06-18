# freeAI
Example usage:
```python
from freeAI import alpaca7b

response = alpaca7b.Running.main("Hello! what language model are you?")
print(response)
```

result:
```json
{
  'created': 1687115742.184269,
  'model': 'alpaca-7b',
  'result': [
    {
      'prompt': 'Hello! what language model are you?',
      'content': 'I am a language model!'
    }
  ]
}
```
Function's
* Running.main(q = str, proxies = json: None)