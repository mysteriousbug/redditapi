import tkinter as tk
from tkinter import ttk

def start_job():
    # Function to simulate a job with progress
    for i in range(101):
        progress_var.set(i)  # Update the progress bar
        root.update_idletasks()  # Update the GUI
        # Simulate some work (you can replace this with your actual job)
        import time
        time.sleep(0.1)

root = tk.Tk()
root.title("Job Progress")

frame = ttk.Frame(root, padding=10)
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Label for product paragraph
product_label = ttk.Label(frame, text="Product Paragraph:")
product_label.grid(column=0, row=0, sticky=tk.W)

# Text box for product paragraph
product_textbox = tk.Text(frame, height=5, width=40)
product_textbox.grid(column=0, row=1, columnspan=2, padx=5, pady=5, sticky=(tk.W, tk.E))

# Label for additional text box (optional)
text_label = ttk.Label(frame, text="Additional Text:")
text_label.grid(column=0, row=2, sticky=tk.W)

# Text box for additional input (optional)
text_textbox = tk.Text(frame, height=3, width=40)
text_textbox.grid(column=0, row=3, columnspan=2, padx=5, pady=5, sticky=(tk.W, tk.E))

# Button to start the job
start_button = ttk.Button(frame, text="Start Job", command=start_job)
start_button.grid(column=0, row=4, columnspan=2, pady=10)

# Progress bar
progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(frame, length=300, variable=progress_var, mode="determinate")
progress_bar.grid(column=0, row=5, columnspan=2, pady=10)

root.mainloop()
