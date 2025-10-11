from google import genai
import os

# Client is the main object; it handles authentication and API access.
# It's recommended to set the API key in an environment variable (GEMINI_API_KEY).
# client = genai.Client()
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
# Example with a placeholder API key for demonstration (replace with your key or use env var)
client = genai.Client(api_key=GEMINI_KEY)

# Retrieve the list of models (this returns an iterable of Model objects)
models = client.models.list()

# Iterate and print some of the core attributes of the Model object
print("Supported Model Attributes (from client.models.list()):\n")
for model in models:
    # Print the model's name attribute
    print(f"Name: {model.name}")

    # Print the model's description attribute (if available)
    if hasattr(model, 'supported_generation_methods'):
        print(f"Description: {model.description}")

    # Print the model's version attribute (if available)
    if hasattr(model, 'version'):
        print(f"Version: {model.version}")

    # You can inspect the entire object with its dict representation
    # print(model.model_dump_json(indent=2))
    print("-" * 20)