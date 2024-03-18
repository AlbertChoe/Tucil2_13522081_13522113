import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import time
from tkinter import messagebox

# Import your bezier functions
from dnc_n import bezier_points_with_dnc_n
from bruteforce_n import bezier_points_with_bruteforce_n

# Define colors for UI
bg_color = "#f0f0f0"
text_color = "#333333"
button_color = "#e0e0e0"
frame_color = "#d0d0d0"


def parse_input(input_str, iterations_str):
    if not input_str.startswith("(") or not input_str.endswith(")") or "),(" not in input_str:
        messagebox.showerror(
            "Input Error", "Error Control Point: Invalid format")
        return None, None
    try:
        control_points_str = input_str.split("),(")
        control_points = [tuple(map(float, point.strip("()").split(",")))
                          for point in control_points_str]
    except ValueError as e:
        messagebox.showerror("Input Error", f"Error Control Point: {e}")
        return None, None
    try:
        iterations = int(iterations_str)
        return control_points, iterations
    except ValueError as e:
        messagebox.showerror("Input Error", f"Error Iteration : {e}")
        return None, None


def plot_bezier_curve(method):
    input_str = entry_control_points.get()
    iterations_str = entry_iterations.get()
    control_points, iterations = parse_input(input_str, iterations_str)

    if control_points is None or iterations is None:
        print(
            "Invalid input. Please check the format of the control points and iterations.")
        return

    # Clear existing graphs
    for widget in frame_graphs.winfo_children():
        widget.destroy()

    if method == "brute":
        plot_with_brute_force(control_points, iterations)
    elif method == "dnc":
        plot_with_dnc(control_points, iterations)


def plot_with_brute_force(control_points, iterations):
    fig, ax = plt.subplots(figsize=(5, 5))

    start_time_brute = time.time()
    bezier_points = bezier_points_with_bruteforce_n(control_points, iterations)
    end_time_brute = time.time()
    time_taken_brute = (end_time_brute - start_time_brute) * 1000
    print(f'Bruteforce\nTime: {time_taken_brute:.5f} ms')
    print(bezier_points)
    ax.plot(*zip(*control_points), 'ro--', label='Control Points')
    bezier_lines_brute = []
    for i in range(1, len(bezier_points) + 1):  # Include the last point in the range
        line, = ax.plot(*zip(*bezier_points[:i]), 'b-',
                        label='Bezier Curve' if i == len(bezier_points) else None)
        ax.scatter(*zip(*bezier_points[:i]), c='g', marker='o')
        bezier_lines_brute.append(line)

    def update_brute(frame):
        for i, line in enumerate(bezier_lines_brute):
            line.set_visible(i <= frame)
        return bezier_lines_brute

    ani_brute = FuncAnimation(fig, update_brute, frames=range(
        len(bezier_points)), interval=500/iterations, blit=True)
    ax.set_title(f'Bruteforce\nTime: {time_taken_brute:.5f} ms')
    ax.legend()
    # Embed the graph into the Tkinter GUI
    canvas = FigureCanvasTkAgg(fig, master=frame_graphs)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


def plot_with_dnc(control_points, iterations):
    fig, ax = plt.subplots(figsize=(5, 5))

    start_time_dnc = time.time()
    a = bezier_points_with_dnc_n(control_points, iterations)
    end_time_dnc = time.time()
    time_taken_dnc = (end_time_dnc - start_time_dnc) * \
        1000  # Convert to milliseconds
    print(f'dnc\nTime: {time_taken_dnc:.5f} ms')
    print(a)
    ax.plot(*zip(*control_points), 'ro--', label='Control Points')
    bezier_lines_dnc = []
    for i in range(iterations + 1):
        bezier_points_dnc = bezier_points_with_dnc_n(control_points, i)
        bezier_points_flat = [
            item for sublist in bezier_points_dnc for subsublist in sublist for item in subsublist]
        bezier_points_flat = [control_points[0]] + \
            bezier_points_flat + [control_points[-1]]
        ax.scatter(*zip(*bezier_points_flat), c='g', marker='o')
        line, = ax.plot(*zip(*bezier_points_flat), 'b-',
                        label='Bezier Curve' if i == iterations else None)
        bezier_lines_dnc.append(line)

    def update_dnc(frame):
        if frame == iterations:
            for line in bezier_lines_dnc:
                line.set_visible(False)
            bezier_lines_dnc[-1].set_visible(True)
        else:
            for i, line in enumerate(bezier_lines_dnc):
                line.set_visible(i == frame)
        return bezier_lines_dnc

    ani_dnc = FuncAnimation(fig, update_dnc, frames=range(
        iterations + 1), interval=500, blit=True)
    ax.set_title(f'Divide and Conquer Method\nTime: {time_taken_dnc:.5f} ms')
    ax.legend()

    # Embed the graph into the Tkinter GUI
    canvas = FigureCanvasTkAgg(fig, master=frame_graphs)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


# Tkinter GUI setup
root = tk.Tk()
root.title('Graph Plotter')
root.configure(bg=bg_color)
root.geometry("700x800")

style = ttk.Style()
style.configure('Custom.TFrame', background=frame_color)

frame_inputs = ttk.Frame(root, padding="10", relief=tk.RIDGE,
                         borderwidth=2, style='Custom.TFrame')
frame_inputs.pack(padx=10, pady=10, fill=tk.X)

frame_graphs = ttk.Frame(root, padding="10", style='Custom.TFrame')
frame_graphs.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Inputs for control points and iterations
label_control_points = ttk.Label(
    frame_inputs, text='Control Points(x,y),(x,y),.. :', background=frame_color, foreground=text_color)
entry_control_points = ttk.Entry(frame_inputs, width=40)
label_iterations = ttk.Label(
    frame_inputs, text='Iterations:', background=frame_color, foreground=text_color)
entry_iterations = ttk.Entry(frame_inputs)

# Layout for inputs
label_control_points.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
entry_control_points.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
label_iterations.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
entry_iterations.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

# Method selection (Brute Force or Divide and Conquer)
method_var = tk.StringVar(value="brute")
radio_brute = ttk.Radiobutton(
    frame_inputs, text='Brute Force', variable=method_var, value='brute')
radio_dnc = ttk.Radiobutton(
    frame_inputs, text='Divide and Conquer', variable=method_var, value='dnc')
radio_brute.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
radio_dnc.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

# Plot button
button_submit_bezier = ttk.Button(
    frame_inputs, text='Plot Bezier Curve', command=lambda: plot_bezier_curve(method_var.get()))
button_submit_bezier.grid(
    row=3, column=0, columnspan=2, pady=5, sticky=tk.W+tk.E)

style.configure('TButton', background=button_color,
                foreground=text_color, padding=5)
style.configure('TFrame', background=frame_color)
style.configure('TLabel', background=frame_color, foreground=text_color)


def on_close():
    root.quit()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
