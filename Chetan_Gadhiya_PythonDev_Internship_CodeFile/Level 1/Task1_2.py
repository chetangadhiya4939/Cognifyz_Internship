print("Welcome to Temperature Conversion System!")
print("Please refer the number for conversion")
print("1.Celcius to Fahrenheit")
print("2.Fahrenheit to Celcius")

n = int(input("Enter Choice for the conversion : "))

def cel_fer():
    cel_value = float(input("Enter Celcius Value : "))
    fer_value = (9/5)*cel_value + 32
    print(f"Fahrenheit of {cel_value} is : {fer_value}")

def fer_cel():
    fer_value = float(input("Enter Fahrenheit Value : "))
    cel_value = (fer_value - 32)*(5/9)
    print(f"Fahrenheit of {fer_value} is : {cel_value}")


match n:
    
    case 1:
        cel_fer()
    case 2:
        fer_cel()
    case _:
        print("Enter proper n value 1 or 2")
            
    
