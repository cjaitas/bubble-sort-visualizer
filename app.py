import gradio as gr

# -----------------------------
# Bubble Sort Visualization Data
# -----------------------------
def bubble_sort_steps(arr):
    steps = []
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):

            # Show comparison
            steps.append({
                "list": arr.copy(),
                "highlight": (j, j+1),
                "action": f"Comparing {arr[j]} and {arr[j+1]}"
            })

            if arr[j] > arr[j+1]:

                # Before swap
                steps.append({
                    "list": arr.copy(),
                    "highlight": (j, j+1),
                    "action": f"Swapping {arr[j]} and {arr[j+1]}"
                })

                # Perform swap
                arr[j], arr[j+1] = arr[j+1], arr[j]

                # After swap
                steps.append({
                    "list": arr.copy(),
                    "highlight": (j, j+1),
                    "action": f"After swap → {arr}"
                })

    return steps


# -----------------------------
# Code Shown to User
# -----------------------------
algorithm_code = """
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
"""


# -----------------------------
# Blue-themed HTML Renderer
# -----------------------------
def render_frame(step):
    arr = step["list"]
    highlight = step["highlight"]
    action = step["action"]

    html = """
    <style>
        .bar-container {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-top: 10px;
        }
        .bar {
            width: 40px;
            border-radius: 6px;
            display: flex;
            align-items: flex-end;
            justify-content: center;
            color: white;
            font-weight: bold;
            font-size: 16px;
        }
    </style>
    <div class='bar-container'>
    """

    for i, num in enumerate(arr):

        # highlight compared/swapped bars
        if i in highlight:
            color = "#007BFF"  # strong blue
            border = "3px solid #003F88"
        else:
            color = "#66B2FF"  # light blue
            border = "1px solid #003F88"

        height = num * 12  # scale visually

        html += f"""
        <div class='bar' style="
            height:{height}px;
            background:{color};
            border:{border};
        ">
            {num}
        </div>
        """

    html += "</div>"

    # Add action text
    html += f"""
    <p style="text-align:center; font-size:20px; color:#003F88;">
        {action}
    </p>
    """

    return html


# -----------------------------
# Generate all animation frames
# -----------------------------
def run_visualizer(input_list):
    try:
        arr = [int(x.strip()) for x in input_list.split(",")]
    except:
        return ["❌ Error: Enter integers separated by commas."]

    steps = bubble_sort_steps(arr)

    return [render_frame(step) for step in steps]


# -----------------------------
# GRADIO UI (No themes used)
# -----------------------------
with gr.Blocks() as demo:

    gr.Markdown("""
    # 🔵 Bubble Sort Visualizer
    Enter a list of numbers (example: `5, 3, 8, 1`)  
    Watch swaps and comparisons animated in blue.
    """)

    input_box = gr.Textbox(label="Input List")
    run_button = gr.Button("Run Visualization")

    gallery = gr.Gallery(label="Sorting Steps", columns=1, height=450)
    code_display = gr.Code(value=algorithm_code, language="python", label="Bubble Sort Code")

    run_button.click(fn=run_visualizer, inputs=input_box, outputs=gallery)

demo.launch()


    run_button.click(fn=run_visualizer, inputs=input_box, outputs=gallery)

demo.launch()
