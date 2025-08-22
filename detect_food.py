import requests
import json

# Your info
API_KEY = "WhkO46oGArsxkjHLp95p"
MODEL_ENDPOINT = "https://detect.roboflow.com/indian_food-pwzlc/2"

# Image to test
IMAGE_PATH = "test.jpg"

# Open the image file
with open(IMAGE_PATH, "rb") as img_file:
    response = requests.post(
        MODEL_ENDPOINT,
        params={"api_key": API_KEY},
        files={"file": img_file}
    )

# Parse results
predictions = response.json()
print(json.dumps(predictions, indent=2))
