import os

file_path = "D:/key/serviceAccountKey.json"
if os.path.exists(file_path):
    print("File exists!")
else:
    print("File not found at", file_path)
