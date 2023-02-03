import requests
from dalleimages import Dalle
API_KEY = "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"
PROMPT = "Generate an origin story for a fighter in a RPG game. It should be at least 500 words. Give the main character a name."

def generate_story():
    response = requests.post(
        "https://api.openai.com/v1/engines/text-davinci-002/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "prompt": PROMPT,
            "max_tokens": 1024,
            "n": 1,
            "stop": None,
            "temperature": 0.5,
        },
    )
    response_json = response.json()
    return response_json["choices"][0]["text"]

def summarize_story(story):
    response = requests.post(
        "https://api.openai.com/v1/engines/text-davinci-002/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
             "prompt": "Summerize in 15 words this story: "+story,
            "max_tokens": 1024,
            "n": 1,
            "stop": None,
            "temperature": 0.5,
        }
    )
    response_json = response.json()
    return response_json["choices"][0]["text"]

if __name__ == "__main__":
    story = generate_story()
    print(story)
    summarized_story = summarize_story(story)
    print("summ" + summarized_story)
    #Dalle("generate an image of a fighter in an RPG game")
    Dalle(summarized_story)
