import os
import requests
from openai import OpenAI
from django.http import HttpResponse
import json
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
from rest_framework import status



# words = input("Enter some words you'd like your story to be about: ")

def generate_story(words):
        # words = input("Enter some words you'd like your story to be about: ")
    # Call the OpenAI API to generate the story
        response = get_short_story(words)
    # Format and return the response
        return format_response(response)

def get_short_story(words):
    system_prompt = f""" You are a short story generator. Write a short story using the following words: {words}.
    Do not go beyond one paragraph.
    """
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role": "user",
        "content": system_prompt
    }],
    temperature=0.8,
    max_tokens=1000
    )

    # Return the API response
    return response

def format_response(response):
    # Extract the generated story from the response
    story = response.choices[0].message.content
    # Remove any unwanted text or formatting
    story = story.strip()
    # Return the formatted story
    return story

# print(generate_story("cat, book, computer, sun, water"))

















# words = input("Enter some words you'd like your story to be about: ")

# def generate_story(words):
#         # words = input("Enter some words you'd like your story to be about: ")
#     # Call the OpenAI API to generate the story
#     print("Coming from line 11", words)
#     response = get_short_story(words)
#     print('Coming from story_gen ', response)
#     # Format and return the response
#     # return format_response(response)
#     return response





# def get_short_story(request):
#     # Assuming the words are passed as a parameter in the request body
#     words = request.POST.get('words', '')
#     # Construct the request data
#     data = {
#         "prompt": f"You are a short story generator. Write a short story using the following words: {words}. Do not go beyond one paragraph.",
#         "temperature": 0.8,
#         "max_tokens": 1000
#     }

#     # Construct the request headers with your OpenAI API key
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer YOUR_OPENAI_API_KEY"
#     }

#     # Make the POST request to the OpenAI API
#     try:
#         response = requests.post(
#             "https://api.openai.com/v1/engines/davinci/completions",
#             json=data,
#             headers=headers
#         )

#         # Check if the request was successful (status code 200)
#         if response.status_code == 200:
#             story = response.json()["choices"][0]["text"].strip()
#             return HttpResponse(story, content_type='text/plain')
#         else:
#             # Handle error response from the OpenAI API
#             return HttpResponse("Failed to generate story", status=500, content_type='text/plain')
#     except Exception as e:
#         # Handle any exceptions that may occur during the request
#         return HttpResponse(str(e), status=500, content_type='text/plain')















    
# def get_short_story(request):
#     print(request.body)
#     if request.method == 'POST':
#         # try:
#         body = json.loads(request.body)
#         words = body.get('words', '')
#         system_prompt = f""" You are a short story generator. Write a short story using the following words: {words}.
#         Do not go beyond one paragraph.
#         """
#         print(words)
#         response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[{
#             "role": "user",
#             "content": system_prompt
#         }],
#         temperature=0.8,
#         max_tokens=1000
#         )

#         story = response.choices[0].message.content.strip
#         print(story)
#     # data = json.loads(story)
#     # print(story["choice 1"])

#     # Return the API response
#     # return response
#     # print('API response: ', response)
#         return HttpResponse(story)
#     else:
#         return HttpResponse('Method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)






















    
# def format_response(response):
#     # Extract the generated story from the response
#     print(response)
#     story = response.choices[0].message.content
#     print(story)
#     data = json.loads(story)
#     # Remove any unwanted text or formatting
#     print(data["choice 1"])
#     story = story.strip()
#     # Return the formatted story
#     # return story
#     return data
    
# print(generate_story("cat, book, computer, sun, water"))
