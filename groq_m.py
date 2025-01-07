from groq import Groq

client = Groq()
def visionExtractWithGroq(b64_image, prompt):
    response = client.chat.completions.create(
    model="llama-3.2-11b-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "You are a web crawler, your job is to extract information based on a screenshot of a webpage and a users instruction."
                },
                {
                    "type": "image_url",
                     "image_url": f"data:image/jpeg;base64,{b64_image}",
                }
            ]
        },
        {
            "role": "assistant",
            "content": "This image captures a stunning sunset, with the vibrant sky transitioning from dark purple to orange, gradually lightening towards the horizon. The gradient effect is achieved through a subtle blending of warm tones, creating a sense of depth and dimensionality.\n\nIn the foreground, a landscape of rolling hills stretches across the bottom portion of the image, silhouetted against the bright sky. Two birds fly high in the sky, while a few clouds gather at the horizon, lending texture to the scene. Overall, the picture conveys a sense of awe and wonder, inviting the viewer to appreciate the breathtaking beauty of the sunset."
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
    )
    message = response.choices[0].message
    message_text = message.content

    if "ANSWER_NOT_FOUND" in message_text:
        print("ERROR: Answer not found")
        return "I was unable to find the answer on that website. Please pick another one"
    else:
        print(f"GPT: {message_text}")
        return message_text