import time  # Import the time module
import tkinter as tk
import time
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sys  # Import the sys module
from dnc_n import *
from dnc import *
from bruteforce_n import *
from bruteforce import *
from matplotlib.animation import FuncAnimation


# Define a color scheme
bg_color = "#f0f0f0"
text_color = "#333333"
button_color = "#e0e0e0"
frame_color = "#d0d0d0"


def parse_input(input_str, iterations_str):
    control_points_str = input_str.strip("[]").split("), (")
    control_points = [tuple(map(float, point.strip("()").split(", ")))
                      for point in control_points_str]
    iterations = int(iterations_str)
    return control_points, iterations


def plot_bezier_curve():
    control_points, iterations = parse_input(
        entry_control_points.get(), entry_iterations.get())

    # Measure the processing time for the divide-and-conquer method
    start_time_dnc = time.time()
    if len(control_points) == 3:
        bezier_points_dnc = generate_bezier(*control_points, iterations)
    else:
        bezier_points_dnc = bezier_points_with_dnc_n(
            control_points, iterations)
    processing_time_dnc = (time.time() - start_time_dnc) * \
        1000  # Convert to milliseconds

    # Measure the processing time for the brute force method
    start_time_brute = time.time()
    if len(control_points) == 3:
        bezier_points_brute = bezier_points_with_bruteforce(
            control_points, iterations)
    else:
        bezier_points_brute = bezier_points_with_bruteforce_n(
            control_points, iterations)
    # Convert to milliseconds
    processing_time_brute = (time.time() - start_time_brute) * 1000

    # Clearing previous figures
    for widget in frame_graphs.winfo_children():
        widget.destroy()

    # Creating the subplot for the brute force method
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.plot(*zip(*control_points), 'ro--', label='Control Points')
    line1, = ax1.plot([], [], 'b-', label='Bezier Curve (Brute Force)')
    ax1.scatter(*zip(*bezier_points_brute), c='b',
                marker='o')  # Add dots for each point
    ax1.set_title(
        f'Brute Force Method\nProcessing Time: {processing_time_brute:.2f} ms')
    ax1.legend()

    # Creating the subplot for the divide-and-conquer method
    ax2.plot(*zip(*control_points), 'ro--', label='Control Points')
    line2, = ax2.plot([], [], 'g-', label='Bezier Curve (DNC)')
    ax2.scatter(*zip(*bezier_points_dnc), c='g',
                marker='o')  # Add dots for each point
    ax2.set_title(
        f'Divide and Conquer Method\nProcessing Time: {processing_time_dnc:.2f} ms')
    ax2.legend()

    # Define the initialization function for the animation
    def init():
        line1.set_data([], [])
        line2.set_data([], [])
        return (line1, line2)

    # Define the update function for the animation
    def animate(i):
        line1.set_data(*zip(*bezier_points_brute[:i+1]))
        line2.set_data(*zip(*bezier_points_dnc[:i+1]))
        return (line1, line2)

    # Calculate the number of points
    num_points = max(len(bezier_points_brute), len(bezier_points_dnc))

    # Set the interval to decrease as the number of points increases
    interval = max(1000 // num_points, 5)

    # Create the animation with the dynamically set interval
    ani = FuncAnimation(fig, animate, init_func=init,
                        frames=num_points, interval=interval, blit=True)

    # Embedding the plot in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=frame_graphs)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


# Setting up the main window
root = tk.Tk()
root.title('Graph Plotter')
root.configure(bg=bg_color)

# Create a style for the frames
style = ttk.Style()
style.configure('Custom.TFrame', background=frame_color)

# Creating frames for inputs and graphs using the custom style
frame_inputs = ttk.Frame(root, padding="10", relief=tk.RIDGE,
                         borderwidth=2, style='Custom.TFrame')
frame_inputs.pack(padx=10, pady=10, fill=tk.X)
frame_graphs = ttk.Frame(root, padding="10", style='Custom.TFrame')
frame_graphs.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Creating input fields and submit button for Bézier curve
label_control_points = ttk.Label(
    frame_inputs, text='Control Points:', background=frame_color, foreground=text_color)
label_control_points.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
entry_control_points = ttk.Entry(frame_inputs, width=40)
entry_control_points.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

label_iterations = ttk.Label(
    frame_inputs, text='Iterations:', background=frame_color, foreground=text_color)
label_iterations.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
entry_iterations = ttk.Entry(frame_inputs)
entry_iterations.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

button_submit_bezier = ttk.Button(
    frame_inputs, text='Plot Bezier Curve', command=plot_bezier_curve, style='TButton')
button_submit_bezier.grid(
    row=2, column=0, columnspan=2, pady=5, sticky=tk.W+tk.E)

# Apply custom styling
style = ttk.Style()
style.configure('TButton', background=button_color,
                foreground=text_color, padding=5)
style.configure('TFrame', background=frame_color)
style.configure('TLabel', background=frame_color, foreground=text_color)

root.mainloop()
