def convert_to_snake_case(pascal_or_camel_cased_string):
# list comprehension
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]
# strip all underscores that mustve been added because of camel case on pascal case strings
    return ''.join(snake_cased_char_list).strip('_')
def main():
    print(convert_to_snake_case('IAmAPascalToSnakeString'))
    print(convert_to_snake_case('iAmACamelToSnakeString'))
if __name__ == '__main__':
    main()