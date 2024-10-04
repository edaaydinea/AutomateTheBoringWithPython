import re


def mad_libs(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()

    # Find placeholders
    placeholders = re.findall(r'\b(ADJECTIVE|NOUN|ADVERB|VERB)\b', text)

    # Replace each placeholder with user input
    for placeholder in set(placeholders):
        user_input = input(f'Enter a {placeholder.lower()}: ')
        text = re.sub(r'\b' + placeholder + r'\b', user_input, text)

    # Output results
    print("\nGenerated Mad Libs:\n")
    print(text)

    # Save to output file
    with open(output_file, 'w') as file:
        file.write(text)
    print(f'Results saved to {output_file}')


if __name__ == '__main__':
    mad_libs('input.txt', 'output.txt')
