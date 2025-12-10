# Bubble Sort Visualizer 
## Demo video has been submitted via OnQ as Github wont allow large enough files to be uploaded
## Problem Breakdown & Computational Thinking
I chose bubble sort as it is a simple, easy to understand sorting algorithm that uses many steps to complete the list. Its repetetive comparisons and swaps make it easy to visualize through animated bars. 

Decomposition:

Bubble sort can be broken down into smaller steps
1. Start at the first index of the list
2. Compare current value with the next value
3. If first value is greater than the second, swap them
4. Move to the next pair and repeat
5. After each full pass the largest value should be at the end of the list
6. Continue untill sorted


Pattern Recognition:

Bubble sort repeatedly follows a pattern
- Compare adjacent values
- Swap when out of order
- Reduce the unsorted range after each pass


Abstraction:

The details I choose to show the user include:
- The current list state in text
- A description of each step in text. Ex. "Swapping 7 and 6"
- A bar chart demonstrating swaps that change colour according to comparing and swapping
The details I choose not to show the user include:
- Internal loop counters
- Temporary variables used during swaps


Algorithm Design:

Input 
- User inputs a comma separated string of integers. Ex. 4,1,3,2

Processing
- Convert the string to a list
- Run the bubble sort algorithm
- Build bar chart for comparisons and swaps

Output
- A description of each step in text.
- The current list state
- A bar chart demonstrating swaps that change colour according to comparing and swapping

Flow chart is in the screenshots folder and has been submitted via OnQ as GitHub can't show my photos

## Steps to Run:
1. Enter list of numbers separated with commas
2. Click the 'Start Sorting' button to start sorting the list
3. Click the 'Next Step' button to view the sorting process step by step
## Hugging Face Link: https://huggingface.co/spaces/cjaitas/Bubble-Sort-Visualizer
## Christian Aitas. AI Disclaimer: I used ChatGPT-5 in order to get help for the GUI aspects of the assignment as I was unfamilliar with Hugging Face.  
