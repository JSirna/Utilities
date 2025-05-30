import json
import csv
import os
import tkinter.filedialog

def convert_to_json(filepath):

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file {filepath} does not exist.")

    json_data = []
    outputPath = os.path.splitext(filepath)[0] + '.json'
    count = 0
    try:
        with open(filepath, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                json_data.append(row)
    except Exception as e:
        raise RuntimeError(f"Error reading the CSV file: {e}")

    try:
        with open(outputPath, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)
        print(f"Converted {filepath} to {outputPath}")
    except Exception as e:
        raise RuntimeError(f"Error writing to JSON file: {e}")
    
if __name__ == "__main__":
    currentPath = os.path.dirname(os.path.abspath(__file__))
    try:
        file = tkinter.filedialog.askopenfile(mode='r', filetypes=[('CSV files', '*.csv')])
        if file:
            filepath = file.name
            convert_to_json(filepath)
        else:
            print("No file selected.")
    except Exception as e:
        print(f"An error occurred: {e}")