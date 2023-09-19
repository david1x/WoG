# A function to validate if the user input can be converted to an integer
def is_it_a_number(input_msg):
    user_input = input(input_msg)
    if user_input.isdigit():
        return int(user_input)
    else:
        print(f"Input is invalid please enter a number.\n")
        user_input = is_it_a_number(input_msg)
        return int(user_input)


if __name__ == '__main__':
    user_geuss = is_it_a_number("Import a number: \n")
    print(user_geuss)