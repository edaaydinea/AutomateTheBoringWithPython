import os
import re


def regex_search(directory, regex):
    # List all .txt files in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                for line in file:
                    if re.search(regex, line):
                        print(f'Match found in {filename}: {line.strip()}')


if __name__ == '__main__':
    dir_path = input('Enter the directory path: ')
    user_regex = input('Enter the regular expression: ')
    regex_search(dir_path, user_regex)

# Example usage:
# Enter the directory path: C:\Users\Al\Documents
# Enter the regular expression: \d{3}-\d{3}-\d{4}
# Match found in test.txt: 555-555-5555
# Match found in test.txt: 123-456-7890
