import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the .env file
load_dotenv()

# Read the key
api_key = os.getenv("OPENAI_API_KEY")
print("API Key found:", bool(api_key))

# Initialize client
client = OpenAI(api_key=api_key)

# Test a simple API call
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello, who are you?"}]
)

print(response.choices[0].message.content)
