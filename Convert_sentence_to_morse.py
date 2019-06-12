
import json
import sys


def main():

    print("Welcome to Morse command prompt")
    input_string = input("Enter the sentence: ")  # Getting input from user

    print("\nMorse code for {} is".format(input_string))

    input_string = input_string.lower()

    # open json file as object
    with open('moorse-code', 'r') as f:
        data = json.load(f)

    # Morse coe for sentence
    morse_list = []

    for character in input_string:
        if character != ' ':
            morse_list.append(data[character])
        else:
            morse_list.append(data["space"])
    print(''.join(morse_list))


if __name__ == "__main__":
    while 1:
        try:
            main()
        except KeyboardInterrupt:
            print("\nQuitting the command")
            sys.exit()
        except KeyError:
            print("Error: Unused charcter")

