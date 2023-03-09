import gradio as gr
import openai 
from decouple import config


openai.api_key=config("OPENAI_API_KEY")


# Main method goes here
def decipher(audio):
    print(audio)

    # Using openAI's speech to text model
    audio_file = open(audio, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print(transcript)
    return transcript["text"]


# Using Gradio's audio Interface
interface = gr.Interface(fn=decipher, inputs=gr.Audio(source="microphone", type="filepath"), outputs="text").launch()
interface.launch()