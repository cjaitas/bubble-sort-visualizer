import gradio as gr

# -------------------------------------------------
# Bubble Sort Algorithm (with step-by-step tracing)
# -------------------------------------------------
def bubble_sort_visual(arr):
    steps = []
    arr = arr.copy()

    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):

            # Record comparison step
            steps.append({
                "action": f"Comparing {arr[j]} and {arr[j + 1]}",
                "list": arr.copy()
            })

            # If left > right → swap
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                # Record swap step
                steps.append({
                    "action": f"Swapped {arr[j]} and {arr[j + 1]}",
                    "list": arr.copy()
                })

    return steps


# -------------------------------------------------
# Function that runs when user presses the button
# -------------------------------------------------
def run_bubble_sort(input_list):
    # Validate and convert input
    try:
        arr = [int(x.strip()) for x in input_list.split(",")]
    except:
        return "❌ Error: Please enter integers separated by commas.", ""

    steps = bubble_sort_visual(arr)

    # Convert steps to readable text output
    output_text = ""
    for step in steps:
        output_text += f"{step['action']}\nList: {step['list']}\n\n"

    final_sorted = steps[-1]["list"] if steps else arr

    return output_text, final_sorted


# -------------------------------------------------
# Gradio User Interface
# -------------------------------------------------
with gr.Blocks() as demo:
    gr.Markdown("""
    # 🔵 Bubble Sort Visualizer
    Enter numbers separated by commas (example: `5, 3, 8, 1`)

    This tool will show every comparison and swap performed by the Bubble Sort algorithm.
    """)

    input_box = gr.Textbox(label="Input List")
    sort_button = gr.Button("Run Bubble Sort")

    output_steps = gr.Textbox(label="Step-by-step Output", lines=20)
    final_output = gr.Textbox(label="Final Sorted List")

    sort_button.click(
        fn=run_bubble_sort,
        inputs=input_box,
        outputs=[output_steps, final_output]
    )

# App will auto-launch on HuggingFace
if __name__ == "__main__":
    demo.launch()

    run_button.click(fn=run_visualizer, inputs=input_box, outputs=gallery)

demo.launch()
