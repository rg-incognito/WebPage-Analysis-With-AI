from openai import OpenAI

# Define the base URLs for accessing the API
BASE_URLS = [
    'https://api-handler-ddc-free-api.hf.space/v2',
    'https://devsdocode-ddc-free-api.hf.space/v2',
    'https://free-ddc.xiolabs.xyz/v1'
]

STATUS = "https://test-company-2.betteruptime.com/"

# Initialize the OpenAI client with a specific base URL and API key
client = OpenAI(
    base_url=BASE_URLS[-1],  # Using the third URL in the list
    api_key="DDC-Free-For-Subscribers-YT-@DevsDoCode"
)

# # List all available models
# models = client.models.list()
# print("\nModels:")
# for model in models:
#     print(model.id)


    

# # Create a normal chat completion
# completion = client.chat.completions.create(
#     model="gpt-4o",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Which is bigger - 9.11 or 9.9?"}
#     ],
#     temperature=0.7,
#     max_tokens=1000
# )

# # Print the response from the normal chat completion
# print("\nNormal Chat Completions:")
# print(completion.choices[0].message)

# Create a chat completion with an image
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
                    }
                }
            ]
        }
    ],
    max_tokens=300
)

# # Print the response from the image chat completion
print("\nImage Chat Completions:")
print(response.choices[0])
