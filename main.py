import pandas as pd
import math
import tkinter as tk
from tkinter import filedialog

def split_csv_file(input_csv, rows_to_split):
    with open(input_csv) as data_file:
        data = pd.read_csv(data_file)

    data_size = len(data)
    # print(f"Input file has a total of {data_size} rows")

    file_need_to_create = math.ceil(data_size / rows_to_split)
    # print(f"Number of files to create: {file_need_to_create}")

    output_file_number = 1
    start_row = 0

    for x in range(0, file_need_to_create):
        end_row = start_row + rows_to_split
        split = data[start_row:end_row]
        split.to_csv(f"split{output_file_number}.csv", index=False)
        output_file_number += 1
        start_row += rows_to_split

def browse_file():
    file_path = filedialog.askopenfilename(title="Select CSV file")
    entry_path.delete(0, tk.END)
    entry_path.insert(0, file_path)

def run_splitter():
    input_csv = entry_path.get()
    rows_to_split = int(entry_rows.get())
    split_csv_file(input_csv, rows_to_split)

# Create the main application window
app = tk.Tk()
app.title("CSV Splitter")

# Add widgets to the window
label_path = tk.Label(app, text="Select CSV File:")
label_path.grid(row=0, column=0, padx=10, pady=10)

entry_path = tk.Entry(app, width=50)
entry_path.grid(row=0, column=1, padx=10, pady=10)

button_browse = tk.Button(app, text="Browse", command=browse_file)
button_browse.grid(row=0, column=2, padx=10, pady=10)

label_rows = tk.Label(app, text="Rows to split:")
label_rows.grid(row=1, column=0, padx=10, pady=10)

entry_rows = tk.Entry(app)
entry_rows.grid(row=1, column=1, padx=10, pady=10)

button_run = tk.Button(app, text="Run Splitter", command=run_splitter)
button_run.grid(row=1, column=2, padx=10, pady=10)

# Start the main event loop
app.mainloop()
