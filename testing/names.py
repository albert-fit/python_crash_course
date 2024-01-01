from name_function import get_formatted_name

print ('Enter "q" at any time to quit.')
while True:
    first = input("\n Please give me a first name: ")
    if first == 'q':
        break
    last = input("\n Please give me your last name:")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")