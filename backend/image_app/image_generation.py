import os
from django.http import JsonResponse
from openai import OpenAI
import base64
import time
import webbrowser
import requests
import io
from PIL import Image
import boto3
from storyline_proj.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME


# POST
 
# https://api.openai.com/v1/images/generations

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

# s3 = boto3.client(
#     's3',
#     aws_access_key_id=env.get("AWS_ACCESS_KEY_ID"),
#     aws_secret_access_key=env.get("AWS_SECRET_ACCESS_KEY")
# )

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


# def generate_image(text):
#     response = get_generated_images(text)

# Call the API
# def get_generated_images(text):
#     system_prompt = f"""{text} """
#     response = client.images.generate(
#     model="dall-e-3",
#     prompt=system_prompt,
#     size="1024x1024",
#     quality="standard",
#     n=1,
# )

def get_generated_images(text):
    system_prompt = f"""{text} """
    response = client.images.generate(
    model="dall-e-3",
    prompt=system_prompt,
    size="1024x1024",
    quality="standard",
    n=1,
)
    print(response)

# Show the result that has been pushed to a url
# webbrowser.open(response.data.url)
    image_url = response.data[0].url
    webbrowser.open(image_url)
    return JsonResponse({'image_url':image_url})
    


def save_image(image_url):
    try:
        # image_url = temp_image
        response = requests.get(image_url)
        image_data = io.Bytes(response.content)
        print('IMAGE URL:', image_url)
        
        # Fetch the image data from the provided URL
        # response = requests.get(image_url)
        # image_data = io.BytesIO(response.content)
        
        # Open image using PIL
        image = Image.open(image_data)
        
        # # Convert the image to JPEG format
        # output = io.BytesIO()
        # image.save(output, format='JPEG')
        # jpeg_data = output.getvalue()
        
        # # Create a unique filename
        # filename = f"{int(time.time())}.jpeg"
        
        # Upload image to S3
        # s3.put_object(Body=jpeg_data, Bucket='dalle-image-storage', Key=filename, ContentType='image/jpeg')
        
        # Get the URL of the uploaded image
        # image_url = f"https://dalle-image-storage.s3.amazonaws.com/{filename}"
        
        # return  image_url
        return JsonResponse({'success': True})
    except Exception as e:
        print('Error saving image:', e)
        return JsonResponse({'error': 'An error occurred while saving the image'}, status=500)