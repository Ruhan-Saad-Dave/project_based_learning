def add_newline_every_30_characters(input_string):
    output = ''
    for i in range(0, len(input_string), 30):
        output += input_string[i:i+30] + '\n'
    return output

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    result = add_newline_every_30_characters(user_input)
    print("Result:")
    print(result)