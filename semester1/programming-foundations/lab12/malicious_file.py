import sys


def values_generator():
    for line in sys.stdin:
        values = line.replace(",", "").replace("\t", "").rstrip("\n").split("|")
        if len(values) != 10:
            raise ValueError("Expected exactly ten fields per row")
        yield values


def row_generator():
    values = []
    generator = values_generator()
    for gen_values in generator:
        values.extend(gen_values)
        while len(values) < 10:
            next_gen_values = next(generator, None)
            if next_gen_values is None:
                raise ValueError("Incomplete row: expected ten fields")
            values[-1] += next_gen_values[0]
            values.extend(next_gen_values[1:])
        if len(values) != 10:
            raise ValueError("Expected exactly ten fields per row")
        yield values
        values = []


def main():
    for row in row_generator():
        print(",".join(row))


if __name__ == "__main__":
    main()
