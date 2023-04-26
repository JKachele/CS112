try:
    string = "1"
    char = string[0]
    print(char)
    if not char.isalpha():
        # raise ValueError("Value must be alpha")
        print("Value must be alpha")
except TypeError:
    print("Type Error")
else:
    print("No Errors!")
