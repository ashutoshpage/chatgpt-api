import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Tell me about Penguins "}])
print(completion.choices[0].message.content)