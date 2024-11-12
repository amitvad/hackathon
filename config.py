# Import the Secret Manager client library.
from google.cloud import secretmanager

# Create the Secret Manager client.
client_sm = secretmanager.SecretManagerServiceClient()

# Access the secret version.
response = client_sm.access_secret_version(request={"name": "projects/69346013441/secrets/MONGODB_URL/versions/1"})
response_gemini_apikey =  client_sm.access_secret_version(request={"name": "projects/69346013441/secrets/APIKEY_GEMINIFLASH/versions/1"})
gemini_api = response_gemini_apikey.payload.data.decode("UTF-8")
mongo_uri = response.payload.data.decode("UTF-8")
# Access the environment variables
#MONGODB_URI = mongo_uri
#GOOGLE_API_KEY = gemini_api