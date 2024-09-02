import os
import shutil

# Define the base paths for sorting
DOWNLOADS_FOLDER = '/home/khushwant/Downloads'
MEDIA_FOLDER = os.path.join(DOWNLOADS_FOLDER, 'Media')
FILES_FOLDER = os.path.join(DOWNLOADS_FOLDER, 'Files')



# Define your directory paths
FILE_FOLDER = '/home/khushwant/Downloads/Files'
MEDIA_FOLDER = '/home/khushwant/Downloads/Media'
IMAGE_FOLDER = os.path.join(MEDIA_FOLDER, 'Images')
VIDEO_FOLDER = os.path.join(MEDIA_FOLDER, 'Videos')
AUDIO_FOLDER = os.path.join(MEDIA_FOLDER, 'Audio')

# Create directories if they don't exist
folders = [FILE_FOLDER, MEDIA_FOLDER, IMAGE_FOLDER, VIDEO_FOLDER, AUDIO_FOLDER]

for folder in folders:
    try:
        if not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)
    except FileExistsError:
        print(f"The directory '{folder}' already exists.")

# Continue with the rest of your script


# Create directories if they don't exist
os.makedirs(VIDEO_FOLDER, exist_ok=True)
os.makedirs(AUDIO_FOLDER, exist_ok=True)
os.makedirs(IMAGE_FOLDER, exist_ok=True)
os.makedirs(FILES_FOLDER, exist_ok=True)

# Mapping of file extensions to their destination folders
file_mapping = {
    ('.mp4', '.avi', '.flv', '.mov', '.mkv'): VIDEO_FOLDER,
    ('.mp3', '.wav', '.aac'): AUDIO_FOLDER,
    ('.jpg', '.jpeg', '.png', '.gif'): IMAGE_FOLDER,
    ('.zip', '.tar', '.gz', '.xlsx', '.pth', '.tgz', '.tar.xz'): FILES_FOLDER,
}

# Function to handle file moving
def move_file(src, dest_folder):
    file_name = os.path.basename(src)
    dest = os.path.join(dest_folder, file_name)

    # Check if the destination file already exists
    if os.path.exists(dest):
        # Modify the file name to avoid overwriting
        base_name, extension = os.path.splitext(file_name)
        counter = 1
        while os.path.exists(dest):
            new_name = f"{base_name}_{counter}{extension}"
            dest = os.path.join(dest_folder, new_name)
            counter += 1

    try:
        shutil.move(src, dest)
        print(f"Moved: {src} to {dest}")
    except Exception as e:
        print(f"Error moving {src}: {e}")

# Function to sort files based on their extensions
def sort_files():
    for file_name in os.listdir(DOWNLOADS_FOLDER):
        file_path = os.path.join(DOWNLOADS_FOLDER, file_name)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Move files based on extension
        moved = False
        for extensions, folder in file_mapping.items():
            if file_name.lower().endswith(extensions):
                move_file(file_path, folder)
                moved = True
                break

        # Optionally handle files that do not match known extensions
        if not moved:
            move_file(file_path, FILES_FOLDER)

# Run the sorting
sort_files()
