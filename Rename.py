import os


def rename_images(folder_path):
    # Get a list of all .jpg files in the specified folder
    files = [file for file in os.listdir(folder_path) if file.lower().endswith('.jpg')]

    # Optional: Sort the files in some way (alphabetically, by date, etc.)
    # files.sort()

    # Rename each file
    for i, file in enumerate(files):
        # Define the new file name
        new_file_name = f"{i + 1}.jpg"

        # Construct the full file paths
        old_file_path = os.path.join(folder_path, file)
        new_file_path = os.path.join(folder_path, new_file_name)

        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed '{file}' to '{new_file_name}'")


# Replace '/path/to/your/folder' with the actual path to your folder containing the images
rename_images('/path/to/your/folder')
