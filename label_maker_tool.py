import os
import json


def generate_labels(root_folder):
    labels = []
    folder_counter = 0

    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)

        if os.path.isdir(folder_path):
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                labels.append([file_path, folder_counter])

            folder_counter += 1

    return labels


root_folder = "path/to/root/folder"
labels = generate_labels(root_folder)

json_data = {
    "labels": labels
}

json_file_path = "labels.json"

with open(json_file_path, "w") as json_file:
    json.dump(json_data, json_file)

print("JSON file created successfully!")
