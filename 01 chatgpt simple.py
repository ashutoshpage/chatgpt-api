import openai

openai.api_key = "api-key"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Tell me about Penguins "}])
print(completion.choices[0].message.content)
