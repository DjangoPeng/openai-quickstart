import gradio as gr
from run_autogpt import LCAutoGPTRunner

def createAutoGPTUI():

    with gr.Blocks() as demo:
        #create a text box for user input , label is "Your task:"
        #create a button to run the model, label is "Run"
        #create a output box to display the output and download result file, label is "Output"
        gr.Markdown(
            """
            # Hello AutoGPT!
            ### Type your task in the box below and click "Run" to run the model.
            """)
        with gr.Row() as row:
            task = gr.Textbox(lines=3, label="Your task:", min_width=300)
            run = gr.Button(label="Run")
        output = gr.File(label="Output")

        def run_autoGPT(task):
            #run the model and return the result
            file = LCAutoGPTRunner().run(task)

            return file
        
        run.click(run_autoGPT, inputs=[task], outputs=[output])

        demo.launch()
    


if __name__ == "__main__":
    createAutoGPTUI()