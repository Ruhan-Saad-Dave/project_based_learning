#This file is used for testing of code concepts.

def write_to_file(filename):
    with open(filename, 'w') as file:
        while True:
            word = input("Enter a word:")
            if word.lower() == 'stop':
                break
            file.write(word + '\n')

def read_from_file(filename):
    word_list = []
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            word_list.append(line.strip())
            count += 1
        print(count)
    return word_list

def main():
    filename = 'ram.txt'
    write_to_file(filename)
    word_list = read_from_file(filename)
    print(word_list)

main()
