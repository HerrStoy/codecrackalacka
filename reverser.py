# Reverse a string!

str_list = []

def reverse_str(strinput):
    index = 0
    for i in strinput:
        letter = strinput[index-1]
        str_list.append(letter)
        index -= 1

    print("".join(str_list))


reverse_str("This is fun!")
