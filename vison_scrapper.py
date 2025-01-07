from openai import OpenAI
import subprocess
import base64
import json
import os
from groq import Groq

from dotenv import load_dotenv

load_dotenv()

client = Groq()
model = OpenAI()
model.timeout = 10

def image_b64(image):
    with open(image, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')
def url2screenshot(url):
    print(f"Crawling {url}")
    
    if os.path.exists("screenshot.jpg"):
        os.remove("screenshot.jpg")
    
    result = subprocess.run(
        ["node", "screenshot.js", url],
        capture_output=True,
        text=True
    )
    
    exitcode = result.returncode
    output = result.stdout
    
    if not os.path.exists("screenshot.jpg"):
        print("ERROR")
        return "Failed to scrape the website"
    
    b64_image = image_b64("screenshot.jpg")
    return b64_image

def visionExtractWithGroq(b64_image, prompt):
    response = client.chat.completions.create(
        model="llama-3.2-90b-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{b64_image}"
                        }
                    }
                ]
            }
        ],
        # temperature=1,
        # max_tokens=1024,
        # top_p=1,
        # stream=False,
        # stop=None,
    )

    # Extract the message content
    message = response.choices[0].message
    message_text = message.content if hasattr(message, 'content') else ""

    # Handle cases where the model doesn't provide an answer
    if "ANSWER_NOT_FOUND" in message_text:
        print("ERROR: Answer not found")
        return "I was unable to find the answer on that website. Please pick another one"
    else:
        print(f"GPT: {message_text}")
        return message_text

def visionExtract(b64_image, prompt):
    response = model.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "system",
                "content": "You are a web crawler, your job is to extract information based on a screenshot of a webpage and a users instruction."
            }
        ] + [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": f"data:image/jpeg;base64,{b64_image}",
                    },
                    {
                        "type": "text",
                        "text": prompt,
                    }
                ]
            }
        ],
        max_tokens=1024,
    )
    message = response.choices[0].message
    message_text = message.content

    if "ANSWER_NOT_FOUND" in message_text:
        print("ERROR: Answer not found")
        return "I was unable to find the answer on that website. Please pick another one"
    else:
        print(f"GPT: {message_text}")
        return message_text

def visionCrawl (url, prompt): 
    b64_image = url2screenshot(url)
    print("Image captured")
    if b64_image == "Failed to scrape the website":
            return "I was unable to crawl that site. Please pick a different one."
    else:
            return visionExtractWithGroq(b64_image, prompt)
response = visionCrawl("https://job-boards.greenhouse.io/particle41llc/jobs/4473297008?gh_src=c3589fd48us", prompt = """
Please examine the image of the form and list each field, along with the following details for each one:
1. **Field Name**: The name of the field (e.g., 'Name', 'Email', etc.).
2. **Field Type**: The type of the field (e.g., 'text', 'email', 'number', 'checkbox', etc.).
3. **Required/Optional**: Whether the field is required or optional. If not explicitly stated, make an assumption based on common form practices.
4. **Placeholder Text**: If any, provide the placeholder text in the field.
5. **Field Description**: If any, describe what information is expected in the field.

If the form has sections or multiple steps, make sure to mention the section for each field. If a field is part of a group (like radio buttons or checkboxes), list all possible options for that group.
"""
)
