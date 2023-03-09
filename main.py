import gradio as gr
import openai
from decouple import config


openai.api_key = config("OPENAI_API_KEY")

# The Models Job or role
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
]


# Main method goes here
def decipher(audio):
    global messages

    # Using openAI's speech to text model
    audio_file = open(audio, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    messages.append({"role": "user", "content": transcript["text"]})

    response =  openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    system_message = response["choices"][0]["message"]["content"]

    print(response)

    return transcript["text"]


# Using Gradio's audio Interface
interface = gr.Interface(fn=decipher, inputs=gr.Audio(
    source="microphone", type="filepath"), outputs="text").launch()
interface.launch()
