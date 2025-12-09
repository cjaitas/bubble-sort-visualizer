import gradio as gr

# -------------------------------------------------
# Create a bar-chart as HTML (no external plotting libs)
# -------------------------------------------------
def create_bar_html(values, highlight_indices=None, swap=False):
    if not values:
        return "<div>No data</div>"

    max_val = max(values)
    min_val = min(values)
    span = max_val - min_val if max_val != min_val else 1

    bar_html_parts = []
    for i, v in enumerate(values):
        height = 30 + int(170 * ((v - min_val) / span))
        color = "#888"
        if highlight_indices and i in highlight_indices:
            color = "#2ecc71" if swap else "#e74c3c"

        bar_html_parts.append(f"""
        <div style="display:inline-block; text-align:center; margin:2px;">
            <div style="background:{color}; width:28px; height:{height}px; border-radius:4px;"></div>
            <div style="margin-top:6px; font-size:12px;">{v}</div>
        </div>
        """)

    return f"""
    <div style="padding:8px; border:1px solid #ddd; border-radius:6px; display:inline-block;">
      {''.join(bar_html_parts)}
    </div>
    """


# -------------------------------------------------
# Bubble Sort Algorithm with HTML + colored text steps
# -------------------------------------------------
def bubble_sort_visual(arr):
    steps = []
    arr = arr.copy()

    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):

            steps.append({
                "action": f'<span style="color:#e74c3c;">Comparing {arr[j]} and {arr[j+1]}</span>',
                "list": arr.copy(),
                "html": create_bar_html(arr.copy(), [j, j+1], swap=False)
            })

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append({
                    "action": f'<span style="color:#2ecc71;">Swapped {arr[j]} and {arr[j+1]}</span>',
                    "list": arr.copy(),
                    "html": create_bar_html(arr.copy(), [j, j+1], swap=True)
                })

    return steps


# -------------------------------------------------
# INIT RUN: Generate steps & return first step
# -------------------------------------------------
def start_sort(input_list):
    try:
        arr = [int(x.strip()) for x in input_list.split(",") if x.strip() != ""]
    except:
        return "❌ Error: Invalid input", "", "<div></div>", [], 0

    steps = bubble_sort_visual(arr)

    import re
    first = steps[0]

    # remove HTML tags like <span style="...">
    action_plain = re.sub(r"<[^>]+>", "", first["action"])

    text = f"Step 1:\n{action_plain}\nList: {first['list']}"


    return text, first["list"], first["html"], steps, 1


# -------------------------------------------------
# NEXT STEP BUTTON
# -------------------------------------------------
def next_step(steps, index):
    if index >= len(steps):
        return "Sorting complete!", steps[-1]["list"], steps[-1]["html"], index

    step = steps[index]

    import re
    action_plain = re.sub(r"<[^>]+>", "", step["action"])

    text = f"Step {index+1}\n{action_plain}\nList: {step['list']}"

    return text, step["list"], step["html"], index + 1


# -------------------------------------------------
# Gradio UI
# -------------------------------------------------
with gr.Blocks() as demo:
        gr.Markdown("""
        # Bubble Sort Visualizer
        **Click "Next Step" to watch the bars move step-by-step.**  
        🔴 Red = Comparing  🟢 Green = Swapping
        """)
    
        input_box = gr.Textbox(label="Input List (e.g. 5, 3, 8, 1)")
        start_button = gr.Button("Start Sorting")
        next_button = gr.Button("Next Step")
    
        out_text = gr.Textbox(label="Step Output", lines=3)
        out_list = gr.Textbox(label="Current List")
        out_html = gr.HTML(label="Visualization")
    
        steps_state = gr.State([])
        index_state = gr.State(0)
    
        start_button.click(
            fn=start_sort,
            inputs=input_box,
            outputs=[out_text, out_list, out_html, steps_state, index_state]
        )
    
        next_button.click(
            fn=next_step,
            inputs=[steps_state, index_state],
            outputs=[out_text, out_list, out_html, index_state]
        )

if __name__ == "__main__":
    demo.launch()
