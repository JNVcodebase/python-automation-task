import os
import shutil
import time

# Function to check if file is older than given number of days
def is_file_old(file_path, days):
    file_age = time.time() - os.path.getmtime(file_path)
    return file_age > days * 86400  # 86400 seconds in a day

# Function to move old files to archive
def archive_old_files(source_dir, archive_dir, days):
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)  # Create archive directory if it doesn't exist

    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        if os.path.isfile(file_path) and is_file_old(file_path, days):
            # Move old file to archive directory
            shutil.move(file_path, os.path.join(archive_dir, filename))
            print(f"Moved: {filename} to archive")

# Specify your source directory and archive directory
source_directory = "/path/to/your/source/directory"
archive_directory = "/path/to/your/archive/directory"
days_old = 30  # Move files older than 30 days

# Call the function to start the task
archive_old_files(source_directory, archive_directory, days_old)
