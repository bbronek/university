import sys,string
from itertools import product

ascii = string.ascii_lowercase

def password_generator(line):
    for x in product(ascii,repeat=line):
        yield x



def main():

    for line in sys.stdin:
        line = line.rstrip('\n')
        line = int(line)
        gen = password_generator(line)
        for g in gen:
            print(''.join(g))



if __name__ == '__main__':
    main()