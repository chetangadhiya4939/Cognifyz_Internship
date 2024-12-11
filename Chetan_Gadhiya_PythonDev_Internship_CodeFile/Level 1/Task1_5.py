def palindrome():
    str = input("Enter string: ")
    pan = str[::-1]
    
    if (pan == str):
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
palindrome()