# freeAI
Example usage:
```python
from freeAI import pocketgpt

response = pocketgpt.Running.main("Hello! what language model are you?")
print(response)
```

result:
```json
{
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
Function's
* Running.main(q = str, proxies = json: None)