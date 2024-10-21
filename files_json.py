import os
import json

def load_json_from_folder():
    folder = input("Enter the folder name where the JSON file is located: ")
    filename = "richardzhemi_adoptions.json"
    file_path = 'C:/Users/RICHARD ZHEMI/OneDrive/Documents/files_assignment/richardzhemi_adoptions.json'
    
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            print("File loaded successfully.")
            return data
    except FileNotFoundError:
        print(f"Error: {filename} not found in folder {folder}. Please check the path.")
    except json.JSONDecodeError:
        print("Error: Failed to decode the JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

data = load_json_from_folder()
