import sys

def generate(line):
    new = ""
    for x in line:
        if x == '&':
            x = ''
        if x.isdigit():
            if x == '9':
                x = '0'
            else :
                x = chr(ord(x)+1)
        x = x.upper()
        new += x
    return new


def main():
    for line in sys.stdin:
        line = line.rstrip('\n')
        print(generate(line))



if __name__ == '__main__':
    main()