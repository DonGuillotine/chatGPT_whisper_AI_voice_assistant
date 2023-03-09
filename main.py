import gradio as gr


# Main method goes here
def decipher(audio):
    print(audio)
    return "Decipher Me"


# Using Gradio's audio Interface
interface = gr.Interface(fn=decipher, inputs=gr.Audio(source="microphone", type="filepath"), outputs="text").launch()
interface.launch()