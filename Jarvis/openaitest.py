import openai

from config import apikey

openai.api_key = apikey

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "Write a letter to my boss for resignation"
    },
    {
      "role": "assistant",
      "content": ""
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)
# response = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {
#       "role": "user",
#       "content": "write an email to my boss for resignation"
#     }
#   ],
#   temperature=1,
#   max_tokens=256,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )
'''
{
  "id": "chatcmpl-7n3RCzkK5dGaC5z9ooTBRqyZ2MhET",
  "object": "chat.completion",
  "created": 1691925642,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": ""
        },
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 275,
    "completion_tokens": 256,
    "total_tokens": 531
  }
}
'''
