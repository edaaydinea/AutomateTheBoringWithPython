def comma_code(items):
    if len(items) == 0:
        return ''  # Return an empty string for an empty list
    elif len(items) == 1:
        return items[0]  # Return the single item without any formatting
    else:
        return ', '.join(items[:-1]) + ', and ' + items[-1]

# Example usage:
spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma_code(spam))  # Output: 'apples, bananas, tofu, and cats'

# Test case with an empty list:
empty_list = []
print(comma_code(empty_list))  # Output: ''
