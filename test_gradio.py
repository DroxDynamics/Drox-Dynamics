import gradio as gr

with gr.Blocks() as demo:
    with gr.Tabs():
        with gr.TabItem("Tab 1", icon="settings"):
            gr.Textbox(label="Textbox in Tab 1")

demo.launch() 