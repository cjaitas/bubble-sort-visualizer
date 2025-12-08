import gradio as gr
import time

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

                # Record before swap
                steps.append({
                    "list": arr.copy(),
                    "highlight": (j, j+1),
                    "action": f"Swapping {arr[j]} and {arr[j+1]}"
                })

                # Perform swap
                arr[j], arr[j+1] = arr[j+1], arr[j]

                # Record after swap
                steps.append({
                    "list": arr.copy(),
                    "highlight": (j, j+1),
                    "action": f"After swap → {arr}"
                })

    return steps


# -----------------------------
# Bubble Sort Code (Displayed)
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
# Frame Rendering (Blue Theme)
# -----------------------------
def render_frame(step):
    arr = step["list"]
    highlight = step["highlight"]
    action = step["action"]

    html = """
    <div style='display:flex; justify-content:center; gap:8px;'>
    """

    for i, num in enumerate(arr):

        # highlight swapped/compared bars
        if i in highlight:
            color = "#007BFF"      # bright blue
            border = "3px solid #003F88"
        else:
            color = "#66B2FF"      # lighter blue
            border = "1px solid #003F88"

        height = num * 12  # scale bar height

        html += f"""
        <div style="
            width: 35px;
            height: {height}px;
            background: {color};
            border: {border};
            border-radius: 6px;
            display:flex;
            align-items:flex-end;
            justify-content:center;
            color:white;
            font-weight:bold;
        ">{num}</div>
        """

    html += "</div>"

    # Add action text
    html += f"""
    <p style="text-align:center; color:#003F88; font-size:18px; font-weight:bold; margin-top:10px;">
        {action}
    </p>
    """

    return html


# -----------------------------
# MAIN FUNCTION — Animation Loop
# -----------------------------
def run_visualizer(input_list):
    try:
        arr = [int(x.strip()) for x in input_list.split(",")]
    except:
        return "❌ Error: Enter integers separated by commas."

    steps = bubble_sort_steps(arr)

    frames = []
    for step in steps:
        frames.append(render_frame(step))

    return frames


# -----------------------------
# GRADIO UI — BLUE THEME
# -----------------------------
with gr.Blocks(theme=gr.themes.Soft(primary_hue="blue")) as demo:

    gr.Markdown("""
    # 🔵 Bubble Sort Visualizer
    Enter numbers separated by commas (example: **5, 3, 8, 1**).
    Watch the list sort step-by-step with animated swaps.
    """)

    input_box = gr.Textbox(label="Input List")
    run_button = gr.Button("Run Visualization")

    gallery = gr.Gallery(label="Visualization", show_label=True, columns=1, height=420)
    code_display = gr.Code(value=algorithm_code, language="python", label="Bubble Sort Code")

    run_button.click(fn=run_visualizer, inputs=input_box, outputs=gallery)

demo.launch()
