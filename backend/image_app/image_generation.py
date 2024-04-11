import os
from django.http import JsonResponse
from openai import OpenAI
import webbrowser


# POST
 
# https://api.openai.com/v1/images/generations

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])


# def get_generated_images(text):
#     response = client.images.generate(
#         model="dall-e-3",
#         prompt="text",
#         n=1,
#         size="1024x1024"
#         )
    
#     images = response['outputs']['images']
#     print(images)
#     return images
def generate_image(text):
    response = get_generated_images(text)

# Call the API
def get_generated_images(text):
    system_prompt = f"""{text} """
    response = client.images.generate(
    model="dall-e-3",
    prompt=system_prompt,
    size="1024x1024",
    quality="standard",
    n=1,
)

# Show the result that has been pushed to an url
# webbrowser.open(response.data.url)
    image_url = response.data[0].url
    webbrowser.open(image_url)