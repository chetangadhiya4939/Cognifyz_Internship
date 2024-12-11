def str_reverse(user_in):
    return user_in[::-1]


# taking Inputs form the User.
user_in = input("Enter an Entry You want to reverse : ")

# travels from 0 to end with decreasing with -1.
rev = str_reverse(user_in)  # slicing operation
print(f"Your reversed output is : {rev}")
