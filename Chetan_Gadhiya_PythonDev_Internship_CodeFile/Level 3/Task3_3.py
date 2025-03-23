import os
import shutil

def organize_files(directory):
    
    if not os.path.exists(directory):
        print("The specified directory does not exist.")
        return
    
    print(f"Organizing files in: {directory}")
    

    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        
    
        if os.path.isdir(file_path):
            continue
        
        
        _, file_extension = os.path.splitext(file_name)
        file_extension = file_extension[1:].lower()  
        if not file_extension:
            continue
        
        
        folder_path = os.path.join(directory, file_extension)
        os.makedirs(folder_path, exist_ok=True)
        
        
        shutil.move(file_path, folder_path)
        print(f"Moved {file_name} to {folder_path}/")
    
    print("File organization complete!")

if __name__ == "__main__":
    
    target_directory = input("Enter the path to the directory to organize: ")
    organize_files(target_directory)
