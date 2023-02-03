import requests
import pyttsx3
from gtts import gTTS
from dalleimages import Dalle
import threading
import pygame
API_KEY = "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"
PROMPT = "Generate an origin story for a fighter in a RPG game. It should be at least 500 words. Give the main character a name. It should be PG-13"

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

def save_story(story):
    with open("story.txt", "w") as file:
        file.write(story)
    
def dis_story(summarized_story):
    Dalle(summarized_story)   
    
def speak_textPYTT(story):
    engine = pyttsx3.init()
    engine.say(story)
    engine.runAndWait()
    print('finished talking')

def speak_text(story):
    print("test")
    tts = gTTS(text=story, lang='en')
    tts.save("story.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("story.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(1000)
    print('finished talking')
    
if __name__ == "__main__":
    story = generate_story()
    print(story)
    summarized_story = summarize_story(story)
    text_thread = threading.Thread(target=speak_text, args=(story,))
    text_thread.start()
    dis_story(summarized_story)
    text_thread.join()
