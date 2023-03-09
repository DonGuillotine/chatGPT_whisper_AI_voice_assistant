import gradio as gr
import openai
from decouple import config


openai.api_key = config("OPENAI_API_KEY")

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
]


# Main method goes here
def decipher(audio):

    # Using openAI's speech to text model
    audio_file = open(audio, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    response =  openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    print(response)

    return transcript["text"]


# Using Gradio's audio Interface
interface = gr.Interface(fn=decipher, inputs=gr.Audio(
    source="microphone", type="filepath"), outputs="text").launch()
interface.launch()
