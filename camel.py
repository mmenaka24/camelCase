def main():
    # take input (camel case) string and initialise output (snake case) string
    camelCase = input("camelCase: ")
    snake_case = ""

    # for each character in input string...
    for char in camelCase:

        # if lowercase, add as normal
        if char.islower():
            snake_case = snake_case + char

        # otherwise (ie, if uppercase), change to _lowercasechar
        else:
            snake_case = snake_case + "_" + char.lower()

    # print string in snake case
    print("snake_case: " + snake_case)


main()
