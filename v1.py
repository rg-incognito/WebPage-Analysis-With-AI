from openai import OpenAI

client = OpenAI(
    base_url="https://paid-ddc.xiolabs.xyz/v1",
    api_key="Contact DevsDoCode for API Key 👉 Telegram - https://t.me/devsdocode || Instagram - https://www.instagram.com/sree.shades_/"
)

# completion = client.chat.completions.create(
#   model="llama-3.1-70b",
#   messages=[
#     {"role": "developer", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "How many letters ‘r’ are in the word ‘strawberry’?"}
#   ]
# )

# print("Normal Chat Completions:")
# print(completion.choices[0].message)

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant."},
        {"role": "user", "content": "A farmer stands with the sheep on one side of the river. A boat can carry only a single person and an animal. How can the farmer get himself and the sheep to the other side of the river with minimum trips?"}
    ],
    stream=True
)

print("\nStream Chat Completions:")
for chunk in completion:
    print(chunk.choices[0].delta.content, end="", flush=True)

# models = client.models.list()
# print("\nModels:")
# for model in models:
#     print(model)

