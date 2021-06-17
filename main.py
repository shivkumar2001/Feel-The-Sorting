import Tkinter as tk

import ttk
import random
import colors as c

# Importing algorithms 
from bubbleSort import bubble_sort
from mergeSort import merge_sort
from counting_Sort import counting_sort
from insertion_Sort import insertion_sort
from selection_Sort import selection_sort
from quick_Sort import quick_sort
from heap_Sort import heap_sort


# Main window 
window = tk.Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(1000, 700)
window.config(bg = c.WHITE)
#
algorithm_name = tk.StringVar()
algo_list = ['Bubble Sort','Merge Sort','Insertion Sort','Selection Sort','Quick Sort','Heap Sort','Counting Sort']
#
speed_name = tk.StringVar()
speed_list = ['Fast', 'Medium', 'Slow']
#
data = []
#
# This function will draw randomly generated list data[] on the canvas as vertical bars
def drawData(data, colorArray):
   # print(data)
    canvas.delete("all")
    #print(colorArray)
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    #normalizedData = [i / max(data) for i in data]
    
    #print(normalizedData)

    for i, height in enumerate(data):
       # print (i,height)
        x0 = i * x_width + offset + spacing
        y0 = canvas_height-height
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()

## This function will generate array with random values every time we hit the generate button
def generate():
    global data

    data = []
    for i in range(0, 100):
        random_value = random.randint(1, 150)
        data.append(random_value)
    #print(data)
    drawData(data, [c.BLUE for x in range(len(data))])

## This function will set sorting speed
def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.001
#
## This funciton will trigger a selected algorithm and start sorting
def sort():
    global data
    timeTick = set_speed()
    
    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Selection Sort':
        selection_sort(data,drawData, timeTick)
    elif algo_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == 'Heap Sort':
        heap_sort(data,drawData,timeTick)
    elif algo_menu.get() == 'Counting Sort':
        counting_sort(data,drawData, timeTick)    
#
#
#### User interface here ###
UI_frame =tk.Frame(window, width= 900, height=300, bg=c.WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)
#
### dropdown to select sorting algorithm 
l1 = tk.Label(UI_frame, text="Algorithm: ", bg=c.WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)
##
## dropdown to select sorting speed 
l2 =tk.Label(UI_frame, text="Sorting Speed: ", bg=c.WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)
##
## sort button 
b1 = tk.Button(UI_frame, text="Sort", command=sort, bg=c.LIGHT_GRAY)
b1.grid(row=2, column=1, padx=5, pady=5)
#
## button for generating array 
b3 = tk.Button(UI_frame, text="Generate Array", command=generate, bg=c.LIGHT_GRAY)
b3.grid(row=2, column=0, padx=5, pady=5)
#
## canvas to draw our array 
canvas = tk.Canvas(window, width=800, height=400, bg=c.WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)


window.mainloop()
