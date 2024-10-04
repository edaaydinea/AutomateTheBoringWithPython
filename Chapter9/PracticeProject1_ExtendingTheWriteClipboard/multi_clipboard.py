import shelve
import sys


def multi_clipboard(command, keyword=None, value=None):
    shelf_file = 'clipboard_shelf'

    with shelve.open(shelf_file) as shelf:
        if command == 'save':
            if keyword and value:
                shelf[keyword] = value
                print(f'Saved: {keyword} -> {value}')
            else:
                print('Please provide a keyword and a value to save.')

        elif command == 'delete':
            if keyword:
                if keyword in shelf:
                    del shelf[keyword]
                    print(f'Deleted: {keyword}')
                else:
                    print(f'Keyword "{keyword}" not found.')
            else:
                # Delete all keywords
                shelf.clear()
                print('All keywords deleted.')

        elif command == 'load':
            if keyword in shelf:
                print(f'{keyword} -> {shelf[keyword]}')
            else:
                print(f'Keyword "{keyword}" not found.')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: multi_clipboard.py <command> [<keyword>] [<value>]')
    else:
        multi_clipboard(*sys.argv[1:])


# Example Usage:
# python multi_clipboard.py save hello 'Hello, World!'
# python multi_clipboard.py load hello
# python multi_clipboard.py delete hello