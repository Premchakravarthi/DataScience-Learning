from google import genai
gemini_api_key = "AIzaSyA0bLoU0MCekqZLuUD2ZG6QkFMgu0YILMs"
Client = genai.Client(api_key= gemini_api_key)

response = Client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain how AI works in a few words",
)

print(response.text)