import string
from collections import Counter

def file_manipulation(file_name):
    #enter file name with specific extension should be in same folder.

    try :
        with open("file_name", "w") as file:
            
            print("What you want to add? and write 'STOP' to finish: ")
            
            while True:
                user = input()
                if user == "STOP":
                    break
                #writing into file.
                file.write(user + '\n')
        print(f"Content has been added in {file_name}")
        
        with open("file_name", "r") as file:
            content = file.read()
            print("File modified and Reading content : ")
            print(content)
            
        #to remove punctuation (all the special characters).
        #this will make the string for the content you have added in the file and after punctuation will be removed.
        translator = str.maketrans("","", string.punctuation)
        #after punctuation will be removed, this is used for lower case.
        cleaned_text = content.translate(translator).lower()
        #this is used to split the string elements from the space between 2 words.
        words = cleaned_text.split()
        #It counts number of each word.
        word_counts = Counter(words)
        
        print("words according to Alphabetical order : ")
        #sorted(word_counts.items()) is for sorting items according to words' alphabetical order and count number.
        for word, count in sorted(word_counts.items()):
            print(f"{word}: {count}")
        
    except FileNotFoundError:
        print("Error: File not found")

file_name = input("Enter file name : ")
file_manipulation(file_name)