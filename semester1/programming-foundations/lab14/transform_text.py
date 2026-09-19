import sys


def transform(line):
    result = ""
    for character in line:
        if character == "&":
            character = ""
        if character.isdigit():
            if character == "9":
                character = "0"
            else:
                character = chr(ord(character) + 1)
        character = character.upper()
        result += character
    return result


def main():
    for line in sys.stdin:
        line = line.rstrip("\n")
        print(transform(line))


if __name__ == "__main__":
    main()
