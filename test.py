import time

def write_file(file_number):
    filename = f"file{file_number}.txt"
    with open(filename, "w") as file:
        file.write(f"This is file {file_number}")

file_number = 1

while True:
    write_file(file_number)
    file_number += 1
    time.sleep(120)  # Sleep for 2 minutes
