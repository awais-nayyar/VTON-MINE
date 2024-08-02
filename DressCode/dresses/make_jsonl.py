import os
import json

# Define the directory paths
directories = ["dense", "images", "keypoints", "label_maps", "skeletons"]

# Dictionary to store file paths
file_paths = {}

# Function to get all files in a directory and its subdirectories
def get_all_files(directory):
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

# Iterate over each directory and get file paths
for directory in directories:
    file_paths[directory] = get_all_files(directory)

# Save the file paths to a JSONL file
with open("dataset.jsonl", "w") as f:
    for directory, paths in file_paths.items():
        for path in paths:
            entry = {directory: path}
            json.dump(entry, f)
            f.write("\n")
