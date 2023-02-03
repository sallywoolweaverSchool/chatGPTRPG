import requests
import cv2
import numpy as np
import json
import os
from dotenv import load_dotenv

class Dalle:
    QUERY_URL = "https://api.openai.com/v1/images/generations"

    load_dotenv()
    

    def generate_image(self, prompt, api_key):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + api_key
        }

        model = "image-alpha-001"
        data = {
    "model": model,
    "prompt": prompt,
    "num_images": 1,
    "size": "1024x1024",
    "response_format": "url"
}

        resp = requests.post(self.QUERY_URL, headers=headers, json=data)

        if resp.status_code != 200:
            raise ValueError("Failed to generate image "+resp.text)

        response_text = json.loads(resp.text)
        return response_text['data'][0]['url']

    def display_image(self, image_url):
        # Read the image from the URL
        resp = requests.get(image_url)
        image = np.asarray(bytearray(resp.content), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        # Display the image
        cv2.imshow("Image", image)
        # Wait until a key is pressed
        cv2.waitKey(0)
        # Destroy the window
        cv2.destroyAllWindows()

    def save_image(self, image_url, file_path):
        # Read the image from the URL
        resp = requests.get(image_url)
        image = np.asarray(bytearray(resp.content), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        # Save the image
        cv2.imwrite(file_path, image)
        #print("image saved")
        
    def __init__(self, pr):
        api_key = os.environ.get("API_KEY")
        prompt = pr
        self.QUERY_URL = "https://api.openai.com/v1/images/generations"
        image_url = self.generate_image(prompt, api_key)
        self.save_image(image_url, "generated_image.jpg")
        self.display_image(image_url)
        
