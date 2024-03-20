import sys

def values_generator():
    for line in sys.stdin:
        values = line.replace(',','').replace('\t','').rstrip('\n').split('|')
        yield values

def row_generator():
    values = []
    generator = values_generator()
    for gen_values in generator:
        values.extend(gen_values)
        while len(values) != 10:
            next_gen_values = next(generator)
            values[-1] += next_gen_values[0]
            values.extend(next_gen_values[1:])
        yield values
        values = []
def main():
    for row in row_generator():
        print(','.join(row))

if __name__ == '__main__':
    main()