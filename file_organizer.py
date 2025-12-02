import os
import shutil

downloads_folder = "C:\\Users\\HP\\OneDrive\\Pictures\\2025-06-07"
destinations = {
    "Images":[".jpg", ".png",".jpeg"],
    "Documents": [".pdf", ".docx",],
    "Videos": [".mp4",".m4a"],
    "Audio": [".mp3"],
    "Animations": [".webp",".gif",".webm"],
    "Web": [".svg"],
    "Camera": [".heic"],
    "Unknown": [".MOV"],
}

# Create folders if they don't exist
for folder in destinations:
    os.makedirs(os.path.join(downloads_folder,folder),exist_ok=True)

#move files
for file in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, file)
    if os.path.isfile(file_path):
        ext = os.path.splitext(file)[1].lower()
        for folder,exts in destinations.items():
            if ext in exts:
                shutil.move(file_path,os.path.join(downloads_folder, folder,file))
print("Organized successfully✅✅✅✅✅✅✅✅")