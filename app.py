import gradio as gr

# Create a bar-chart as HTML 
def create_bar_html(values, highlight_indices=None, swap=False):
    """
    Generates an HTML bar chart representing the current list.
    Highlights two indices in red (compare) or green (swap).
    """

    # If the list is empty, display a message instead of bars.
    if not values:
        return "<div>No data</div>"

    # Scale bar heights relative to min/max values
    max_val = max(values)
    min_val = min(values)

    # Avoid division by zero if all values are equal
    span = max_val - min_val if max_val != min_val else 1

    bar_html_parts = []

    # Build each bar element
    for i, v in enumerate(values):
        # Scale height between ~30px and ~200px
        height = 30 + int(170 * ((v - min_val) / span))

        # Default color is grey
        color = "#888"

        # If this bar is being compared or swapped, highlight it
        if highlight_indices and i in highlight_indices:
            color = "#2ecc71" if swap else "#e74c3c"

        # Build HTML for each bar
        bar_html_parts.append(f"""
        <div style="display:inline-block; text-align:center; margin:2px;">
            <div style="background:{color}; width:28px; height:{height}px; border-radius:4px;"></div>
            <div style="margin-top:6px; font-size:12px;">{v}</div>
        </div>
        """)

    # Wrap bars in a container
    return f"""
    <div style="padding:8px; border:1px solid #ddd; border-radius:6px; display:inline-block;">
        {''.join(bar_html_parts)}
    </div>
    """

# Bubble Sort Algorithm — generates a list of visual steps
def bubble_sort_visual(arr):
    """
    Runs bubble sort on a copy of the input and records each step as:
    - A text description (HTML)
    - The list state at that moment
    - A visualization of the list
    """
    
    steps = []          # Stores all steps for later replay
    arr = arr.copy()    # Work on a copy so original input isn't modified
    n = len(arr)

    for i in range(n):
        # Inner loop compares adjacent values
        for j in range(0, n - i - 1):

            # Record comparison
            steps.append({
                "action": f'<span style="color:#e74c3c;">Comparing {arr[j]} and {arr[j+1]}</span>',
                "list": arr.copy(),
                "html": create_bar_html(arr.copy(), [j, j+1], swap=False)
            })

            # If out of order, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                # Record swap
                steps.append({
                    "action": f'<span style="color:#2ecc71;">Swapped {arr[j]} and {arr[j+1]}</span>',
                    "list": arr.copy(),
                    "html": create_bar_html(arr.copy(), [j, j+1], swap=True)
                })

    return steps

# First Step Handler — runs bubble sort + returns step 1
def start_sort(input_list):
    """
    Converts the user's input string into a list, starts bubble sort,
    and sends back the first recorded step.
    """
    try:
        # Convert string to list "5, 3, 1" → [5, 3, 1]
        arr = [int(x.strip()) for x in input_list.split(",") if x.strip() != ""]
    except:
        # Return error state if conversion fails
        return "Error: Invalid input", "", "<div></div>", [], 0

    # Generate all steps of bubble sort
    steps = bubble_sort_visual(arr)

    # Get the first step
    first = steps[0]

    # Remove HTML tags from the description so text box stays clean
    import re 
    action_plain = re.sub(r"<[^>]+>", "", first["action"])

    # Build formatted output text
    text = f"Step 1:\n{action_plain}\nList: {first['list']}"

    return text, first["list"], first["html"], steps, 1


# Next Step Handler — Move forward one step at a time when the user clicks "Next Step".
def next_step(steps, index):
    """
    Loads the next recorded step from the bubble sort.
    """
    # If we've reached the end of all steps:
    if index >= len(steps):
        return "Sorting complete!", steps[-1]["list"], steps[-1]["html"], index

    # Grab the current step
    step = steps[index]

    import re
    # Remove HTML styling from action text
    action_plain = re.sub(r"<[^>]+>", "", step["action"])

    # Build readable output text
    text = f"Step {index + 1}\n{action_plain}\nList: {step['list']}"

    # Move to the next step index
    return text, step["list"], step["html"], index + 1


# Gradio UI Layout
with gr.Blocks() as demo:

    # Title + description
    gr.Markdown("""
        # Bubble Sort Visualizer  
        **Click "Next Step" to watch the bars move step-by-step.**  
        🔴 Red = Comparing  🟢 Green = Swapping
    """)

    # Inputs
    input_box = gr.Textbox(label="Input List (e.g. 5, 3, 8, 1)")
    start_button = gr.Button("Start Sorting")
    next_button = gr.Button("Next Step")

    # Outputs
    out_text = gr.Textbox(label="Step Output", lines=3)
    out_list = gr.Textbox(label="Current List")
    out_html = gr.HTML(label="Visualization")

    # Hidden states that store steps & index
    steps_state = gr.State([])
    index_state = gr.State(0)

    # Start sorting
    start_button.click(
        fn=start_sort,
        inputs=input_box,
        outputs=[out_text, out_list, out_html, steps_state, index_state]
    )

    # Move to next step
    next_button.click(
        fn=next_step,
        inputs=[steps_state, index_state],
        outputs=[out_text, out_list, out_html, index_state]
    )


# Launch app
if __name__ == "__main__":
    demo.launch()
